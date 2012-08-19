#!/usr/bin/env python
import sys
sys.path.append('../modules/')

from scapy.all import sniff
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        output = self.sniff_int()
        print output.sprintf("{IP:%IP.src%:%TCP.sport% -> %IP.dst%:%TCP.dport%\n}")
        self.write('blah')

    def arp_monitor_callback(self, pkt):
        return pkt.sprintf("{IP:%IP.src%:%TCP.sport% -> %IP.dst%:%TCP.dport%\n}")

    def sniff_int(self):
        #output = sniff(prn=self.arp_monitor_callback, filter='tcp', count=1)
        output = sniff(filter='tcp', count=1)
        return output

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

