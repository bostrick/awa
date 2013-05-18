
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    #import pdb; pdb.set_trace()
    config = Configurator(settings=settings)
#    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('set_current_slide', '/set_slide')
    config.add_route('raise_hand', '/raise_hand')
    config.add_route('lower_hand', '/lower_hand')
    config.add_route('grab', '/grab')
    config.add_route('ungrab', '/ungrab')
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()

import wsgi

