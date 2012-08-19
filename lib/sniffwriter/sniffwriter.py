class SniffWriter:
    def arp_monitor_callback(self, pkt):
        return pkt.sprintf("{IP:%IP.src%:%TCP.sport% -> %IP.dst%:%TCP.dport%\n}")

    def sniff_int(self):
        #output = sniff(prn=self.arp_monitor_callback, filter='tcp', count=1)
        output = sniff(filter='tcp', count=1)
        return output

