#!/usr/bin/env python
import sys
sys.path.append('../modules/')
sys.path.append('../lib')

from sniffwriter import sniffwriter
from scapy.all import sniff
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        sniffwriter.SniffWriter.sniff_int()
        self.write('blah')

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

