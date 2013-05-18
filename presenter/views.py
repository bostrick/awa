
import logging; log = logging.getLogger("presenter")
DEBUG=log.debug; INFO=log.info; WARN=log.warning; ERROR=log.error
logging.basicConfig(level=logging.DEBUG)

from pyramid.view import view_config

import os
from fcntl import flock, LOCK_EX, LOCK_UN

COOKIE='presenter_user'

class App(object):

    dir_name = "/var/tmp/presenter"
    nusers = 13

    files = {
        'slide': os.path.join(dir_name, "slide"),
        'hand': os.path.join(dir_name, "hand"),
        'user': os.path.join(dir_name, "user"),
    }

    def __init__(self):

        if not os.path.exists(self.dir_name): 
            INFO("making %s" % self.dir_name)
            os.makedirs(self.dir_name)

    def _get_file(self, name, dflt=None):

        fname = self.files.get(name)
        if not os.path.exists(fname):
            return dflt

        with open(fname, "r") as f: 
            value = f.read().strip()
            if not len(value.strip()):
                return dflt
            return value

    # so we're fast and loose with race conditions, but at least 
    # we will at least prevent file corruption
    def _set_file(self, name, value):

        fname = self.files.get(name)
        with open(fname, "w") as f: 
            flock(f, LOCK_EX)
            f.write(value)
            flock(f, LOCK_UN)

        return value

    def get_current_slide(self):
        return self._get_file("slide", "index.html")

    def set_current_slide(self, value):
        return self._set_file("slide", value)

    def get_hands(self):
        return set(self._get_file("hand", "").split(","))

    def _set_hands(self, hands):
        self._set_file("hand", ",".join(map(str, hands)))

    # race condition!
    def raise_hand(self, hand):

        INFO("raise hand %s" % str(hand))

        hands = self.get_hands()
        hands.add(hand)
        self._set_hands(hands)

    # race condition!
    def lower_hand(self, hand=None):

        INFO("lower hand %s" % str(hand))

        if hand:
            hands = self.get_hands()
            if hand in hands:
                hands.remove(hand)
            self._set_hands(hands)
        else:
            self._set_hands([])

    # race condition!
    def get_user(self):
        u = self._get_file("user", "1")
        self._set_file("user", str(int(u)+1))
        return int(u)%self.nusers

_app = App()

def get_req_user(req):

    u = req.cookies.get(COOKIE)
    if not u:
        u = _app.get_user()
        req.response.set_cookie("presenter_user", str(u))
    return int(u)

def set_req_user(req, value):

    INFO("becoming presenter")
    req.response.set_cookie(COOKIE, str(value))
    return value

@view_config(route_name='home', renderer='json')
def home(req):

    h = {
        'user': get_req_user(req),
        'slide': _app.get_current_slide(),
        'status': 0,
    }

    if h["user"] == -1:
        h["hands"] = list(_app.get_hands())

    return h

@view_config(route_name='grab', renderer='json')
def grab(req):

    u  = set_req_user(req, -1)
    s = _app.get_current_slide()

    return { 'status': 0, 'slide': s, 'user': int(u) }

@view_config(route_name='ungrab', renderer='json')
def ungrab(req):

    u  = get_req_user(req)
    s = _app.get_current_slide()

    req.response.set_cookie(COOKIE, '')

    return { 'status': 0, 'slide': s,  'user': u }

@view_config(route_name='set_current_slide', renderer='json')
def set_current_slide(req):

    u  = get_req_user(req)
    slide = req.POST.getone("slide")
    if slide:
        INFO("setting slide to %s" % slide)
        s = _app.set_current_slide(slide);
    return { 'status': 0, 'slide': s, 'user': int(u) }

@view_config(route_name='raise_hand', renderer='json')
def raise_hand(req):

    u  = get_req_user(req)
    if u == -1:
        return { 'status': -1 }

    INFO("raising hand %s" % u)

    _app.raise_hand(u)
    return { 'status': 0, }

@view_config(route_name='lower_hand', renderer='json')
def lower_hand(req):


    u  = get_req_user(req)
    hand = req.POST.getone("hand")
    
    INFO("lowering hand %s" % hand)

    if hand:
        _app.lower_hand(hand)
    else:
        _app.lower_hand()

    return { 'status': 0, }

