#!/usr/bin/python 
#
#  Copyright (c) 2012 Bowe Strickland <bowe@yak.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
"""
"""
__author__  = 'Bowe Strickland <bowe@yak.net>'
__docformat__ = 'restructuredtext'

import logging; log = logging.getLogger(__name__)
DEBUG=log.debug; INFO=log.info; WARN=log.warning; ERROR=log.error
logging.basicConfig(level=logging.INFO)

import os
import sys
from libxml2 import htmlReadFile
from contextlib import contextmanager

from jinja2 import Template

@contextmanager
def indir(dirname):

    cwd = os.getcwd()

    if not os.path.exists(dirname):
        INFO('creating %s' % dirname)
        os.makedirs(dirname)

    os.chdir(dirname)
    yield
    os.chdir(cwd)

class Section(object):

    def __init__(self, parent, node):

        self.parent = parent
        self.mgr = parent and parent.mgr
        self.node = node
        self.subsections = []
        self.id = "_main"

        self.build()

    def build(self):

        ss = self.node.xpathEval('div[@class="section"]')
        self.subsections = [ Section(self, s) for s in ss ]
        
    def analyze(self, page, idmap, pagemap):

        page += 1
        self.page = page

        self.title = self.node.xpathEval("h1|h2|h3|h4|h5|h6")[0]
        self.id = self.node.prop("id")

        if self.id in idmap:
            WARN("id collision: %s" % self.id)

        idmap[self.id] = self
        pagemap[page] = self

        INFO("analyzing %s" % self)

        for s in self.subsections:
            page = s.analyze(page, idmap, pagemap)

        return page

    @property
    def href(self): return self.mgr.html_name % self.page

    def render(self):

        nnext = self.mgr.pagemap.get(self.page+1)
        prev = self.mgr.pagemap.get(self.page-1)
        kw = {
            'next': nnext and nnext.href,
            'prev': prev and prev.href,
            'main_title': self.mgr.title.content,
        }

        if self.subsections:
            content = self._get_toc_content()
            [ s.render() for s in self.subsections ]
        else:
            content=str(self.node)

        txt = self.mgr.tmpl.render(content=content, **kw)
        with open(self.href, "w") as f:
            f.write(txt.encode("utf-8"))

    def _get_toc_content(self):

        cid = "id%d" % self.page
        cnode = self.mgr.contents.xpathEval('.//*[@id="%s"]' % cid)
        if cnode:
            cnode = cnode[0]
            title = str(cnode)
            toc = cnode.next and str(cnode.next) or ""
            return self.mgr.toc_tmpl % (title, toc)

        return ""

    def __str__(self):

        return "<section %s %s>" % (self.page, self.title.content)
        
class Document(object):

    tmpl = "base.html.tmpl"
    compiler = { "cheetahVarStartToken": "@@" }
    html_name = "page_%03d.html"

    toc_tmplo = """
<div class="contents">

<ul class="simple"><li>

%s

</li></ul>
</div>
""".strip() + os.linesep

    toc_tmpl = """
<div class="contents">
<h3>%s</h3>
%s
</div>
""".strip() + os.linesep

    def __init__(self, doc):
    
        INFO("using doc %s" % repr(doc))
        self.doc = doc
        self.mgr = self

        self.max_page = -1
        self.id = "_main"

        self.idmap = { self.id: self,}
        self.pagemap = { 0: self, }

        self.body = doc.xpathEval("//body")[0]
        self.contents = self.body.xpathEval("//*[@id='contents']")[0]
        self.node = self.body.xpathEval("//div[@class='document']")[0]

        self.build()

        with open(self.tmpl) as f:
            INFO("using template %s" % self.tmpl)
            self.tmpl = Template(unicode(f.read(), "utf-8"))

    def build(self):

        ss = self.body.xpathEval('div/div[@class="section"]')
        self.subsections = [ Section(self, s) for s in ss ]

    def analyze(self):

        self.title = self.node.xpathEval("h1|h2|h3|h4|h5|h6")[0]
        self.page = page = 0

        for s in self.subsections:
            page = s.analyze(page, self.idmap, self.pagemap)

        self.max_page = page

    @property
    def href(self): return "index.html"

    def render(self):

        self._update_index_refs()

        with indir("html"):

            for f in "css fonts img js".split():
                INFO("creating symlink %s" % f)
                if not os.path.exists(f):
                    os.symlink("../%s" % f, f)

            kw = {
                'next': self.pagemap[1].href,
                'prev': False, 
                'main_title': self.mgr.title.content,
            }
            txt = self.mgr.tmpl.render(content=str(self.contents), **kw)

            with open(self.href, "w") as f:
                f.write(txt.encode("utf-8"))

            for s in self.subsections:
                s.render()

    def _update_index_refs(self):

        aa = self.contents.xpathEval(".//a")
        for a in aa:
            sid = a.prop("href")[1:]
            s = self.idmap.get(sid)
            if s:
                a.setProp("href", s.href)
            else:
                WARN("could not resolve toc href %s" % sid)

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    import sys

    doc = htmlReadFile(sys.argv[1], None, 0)
    INFO("read %s" % repr(doc))

    d = Document(doc)
    d.analyze()
    d.render()

# vi: ts=4 expandtab


