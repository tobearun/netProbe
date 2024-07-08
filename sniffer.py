from intro import show_splash_screen
from scapy.layers.inet import IP
from scapy.sendrecv import sniff


def call_back(packet):
    if IP in packet:
        ip_source = packet[IP].src
        ip_destination = packet[IP].dst
        print(f"IP Packet: {ip_source} -> {ip_destination}")

if __name__=="__main__":
    show_splash_screen()
    sniff(prn=call_back, count=1)
