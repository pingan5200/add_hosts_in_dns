# 代码功能：远程连接服务器,执行查看命令

import paramiko
# from xxx import *   # TODO


HOST = "192.168.92.133"
PWD = "123456"
USER = "root"
PORT = 22


def connect(host=HOST, user=USER, pwd=PWD):
    """连接服务器"""
    try:
        # 开启客户端
        client = paramiko.SSHClient()
        # 允许连接不在known_hosts文件上的主机
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务端,需要密码
        client.connect(host, username=user, password=pwd)  
        # print(client)
    except Exception as e:
        print(e)
    return client


def send_cmd(client, cmd):
    """发送命令，取得返回值
    """
    try:
        # 返回3个文件结果
        stdin, stdout, stderr = client.exec_command(cmd)
        return stdout
    # except Exception as e:
    except paramiko.SSHException as e:
        print(e)
        # client.close()


def main():
    client = connect()
    print('paramiko is start....')
    # cmd = "ls -l"
    if client:
        # 产生生成器
        n = (i for i in range(4, 9))
        print(type(n))
        for i in n:
            cmd = f"echo '192.168.92.13{i}   host{i}' >> /etc/hosts"
            stdout = send_cmd(client, cmd)
            # print(stdout.read().decode())
        client.close()
        print('paramiko is success....')

if __name__ == '__main__':
    main()