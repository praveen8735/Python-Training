import paramiko


class CustomSSHClient:
    def __init__(self, host, port, user, pwd):
        self.host = host
        self.port = port
        self.user = user
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.user, pwd)

    def check_output(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        output = stdout.read()
        response = output if output else stderr.read()  # ? :
        return response.decode('ascii')   # bytes into unicode

    def __del__(self):
        """destructor"""
        self.ssh.close()


if __name__ == '__main__':
   ssh = CustomSSHClient('ravijaya.info', 22, 'training', 'training')
   op = ssh.check_output('lscpu')
   print(op)