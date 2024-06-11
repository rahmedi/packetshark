import socket

print("Write Ip Address")
IPA = input("Ip >")
print("Write Port")
PORTA = int(input("Port >"))

print(f"Ip Is: {IPA} Port Is: {PORTA}")

def Seleksiyon():
    while True:
        print("Welcome To Yev Group PacketShark")
        print("Modes Is TCP and UDP")
        kuesciyon = input("Select Mode ->").strip().lower()

        if kuesciyon == 'tcp':
            print("DPL(DataPacketLoop) or RM(RawMessage) Choose One:")
            tcpmodeselection = input("Select Mode -->").strip().lower()
            if tcpmodeselection in ['dpl', 'datapacketloop']:
                print("Write Loop Number")
                tcpdpl = int(input("Write Loop Number --->"))

                DPLS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                DPLS.connect((IPA, PORTA))

                for i in range(tcpdpl):
                    try:
                        tcpdplpack = b'GET / HTTP/1.1\r\nHost: ' + IPA.encode() + b'\r\n\r\n'
                        DPLS.sendall(tcpdplpack)
                    except Exception as e:
                        print(f"Error: {e}")

                response = DPLS.recv(50).decode()
                status_line = response.split('\r\n')[0]
                status_code = status_line.split(' ')[1]
                print(f"HTTPRC: {status_code}")
                print(f"{tcpdpl} Packet Sended")
                DPLS.close()

            elif tcpmodeselection in ['rm', 'rawmessage']:
                RMtcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                RMtcp.connect((IPA, PORTA))
                print("Raw Message")
                rmmsg = input("Message --->")
                RMtcp.sendall(rmmsg.encode())
                RMtcp.close()

        elif kuesciyon == 'udp':
            print("DPL(DataPacketLoop) or RM(RawMessage) Choose One:")
            udpmodeselection = input("Select Mode -->").strip().lower()
            if udpmodeselection in ['dpl', 'datapacketloop']:
                print("Write Loop Number")
                udpdpl = int(input("Write Loop Number --->"))

                UDPLS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                for x in range(udpdpl):
                    try:
                        udpdplpack = b'GET / HTTP/1.1\r\nHost: ' + IPA.encode() + b'\r\n\r\n'
                        UDPLS.sendto(udpdplpack, (IPA, PORTA))
                    except Exception as e:
                        print(f"Error: {e}")
                UDPLS.close()


            elif udpmodeselection in ['rm', 'rawmessage']:
                RMudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                print("Write Message")
                rmumsg = input("Message --->")
                RMudp.sendto(rmumsg.encode(), (IPA, PORTA))
                RMudp.close()
            else:
                print("Select A Mode")
        else:
            print("Select A Mode")

Seleksiyon()

input("Press Enter For Exit")
