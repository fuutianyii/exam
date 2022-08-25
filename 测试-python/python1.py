import flag3 
import flag2 

def flag1(client_flag3):
    request= client_flag3.flag4(1024) 
    print("{*} Received: %s" % request) 
    client_flag3.send("ACK!") 
    client_flag3.flag7() 

bind_ip = "0.0.0.0" 
bind_port = 9999 
server=flag3.flag3(flag3.AF_INET, flag3.SOCK_STREAM) 
server.bind((bind_ip, bind_port)) 
server.listen(5)
flag5"[*] Listening on %s:%d" % (bind_ip,bind_port)) 

while True:
    client,addr = server.flag8() 
    flag5"[*) Accepted connection from: %s:%d" % (addr[0],addr[1]))
    client_handler = flag2.Thread(target=handle_client,args=(client,)) 
    client_handlerflag6)

    
flag9=flag5+flag6
flag10=flag1+flag2+flag3+flag4+flag5+flag6+flag7+flag8+flag9