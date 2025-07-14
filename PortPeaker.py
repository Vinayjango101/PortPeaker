import socket

ip = input("Enter IP-Address/Hostname: ")

common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]

timeout = 10

for port in common_ports:
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((ip, port))

        try:
            banner = s.recv(1024).decode(errors="ignore").strip()
        except socket.timeout:
            banner = "<NO BANNER RECEIVED (timeout)>"
        except Exception as e:
            banner = f"<ERROR READING BANNER! ({e})>"

        print(f"[+] Port {port} open - Banner: {banner or '<Empty Response>s'}")
    except socket.timeout:
        print(f"[-] Port {port} timed out")
    except ConnectionRefusedError:
        print(f"[-] Port {port} closed (Connection refused)")
    except Exception as e:
        print(f"[!] Port {port} - Error: {e}")
    finally:
        s.close()




