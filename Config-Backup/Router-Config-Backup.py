import paramiko
from getpass import getpass
import time
import os


def ssh_call(ip,port,username,password,cmds):
      print('Connecting to ...%s' %ip)
      ssh=paramiko.SSHClient()
      ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      ssh.connect(ip,port,username,password)
      connection = ssh.invoke_shell()
      time.sleep(5)
      for c in cmds:
          connection.send(c)
          time.sleep(3)
          if connection.recv_ready():
             sp_detail = connection.recv(9999)
             for line in sp_detail.decode('utf8').strip().split('\r\n'):
                 output=open(os.path.join(ip+'.txt'),'a')
                 output.write('\n')
                 output.write(line)
                 output.close()
          return connection.close()
def main():
    with open('cmds.txt') as c:
        cmds = c.readlines()
    with open('hosts.txt') as f:
        hosts = f.readlines()
        for ips in hosts:
            if not ips:
                break
            ip = ips.strip()
            port = 22
            username='admin'
            password =getpass('Enter passwprd:')
            ssh_call(ip,port,username,password,cmds)

if __name__ == '__main__':
    main()
