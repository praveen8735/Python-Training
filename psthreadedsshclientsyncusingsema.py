import xml.etree.ElementTree as et
from pssshclient import CustomSSHClient
import threading
import logging
from time import sleep

logging.basicConfig(format='%(asctime)s : %(threadName)s : %(message)s')
target_file = 'sshresponse.log'


class ThreadedSSHHandler(CustomSSHClient):
    def __init__(self, host, port, user, pwd, job, lock):
        super().__init__(host, port, user, pwd)
        self.job = job
        self.lock = lock
        self.t_name = threading.current_thread().name
        self.__task_runner()

    def __task_runner(self):
        payload = self.check_output(self.job)
        caption = '{} ran {} @ {}'.format(self.t_name, self.job, self.host)

        logging.warning('checks & waits for the lock')

        with self.lock:
            # critical section
            logging.warning('acquired the lock')

            with open(target_file, 'a') as fw:
                fw.write(caption.center(80, '-') + '\n')
                fw.write(payload + '\n')
                sleep(1)

            logging.warning('releases the lock')


class ThreadedSSHClient:
    """main thread"""

    def __init__(self, host_file):
        self.host_file = host_file
        self.__spawn_threads()

    def __spawn_threads(self):
        threads = []

        threading.BoundedSemaphore
        lock_obj = threading.Semaphore(3)  # sync using binary semaphore

        for host_config in self.__parse_host_file():
            host_config.append(lock_obj)

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
