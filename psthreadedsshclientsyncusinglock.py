import xml.etree.ElementTree as et
from pssshclient import CustomSSHClient
import threading

target_file = 'sshresponse.log'


class ThreadedSSHHandler(CustomSSHClient):
    def __init__(self, host, port, user, pwd, job):
        super().__init__(host, port, user, pwd)
        self.job = job
        self.t_name = threading.current_thread().name
        self.__task_runner()

    def __task_runner(self):
        payload = self.check_output(self.job)
        caption = '{} ran {} @ {}'.format(self.t_name, self.job, self.host)

        with open(target_file, 'a') as fw:
            # critical section
            fw.write(caption.center(80, '-') + '\n')
            fw.write(payload + '\n')


class ThreadedSSHClient:
    def __init__(self, host_file):
        self.host_file = host_file
        self.__spawn_threads()

    def __spawn_threads(self):
        threads = []

        for host_config in self.__parse_host_file():
            t = threading.Thread(target=ThreadedSSHHandler, args=host_config)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    def __parse_host_file(self):
        etree = et.parse(self.host_file)

        for host_tag in etree.getiterator('host'):
            config = [host_tag.get('name'), int(host_tag.get('port'))]

            for host_info in host_tag:
                config.append(host_info.text)

            yield config


if __name__ == '__main__':
    ThreadedSSHClient('hosts.xml')
