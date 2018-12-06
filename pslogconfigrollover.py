import logging
from logging.handlers import RotatingFileHandler
from time import sleep

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
fmt = logging.Formatter(fmt_str)  # what?

fh = RotatingFileHandler('messages.log', backupCount=5, maxBytes=32)
fh.setFormatter(fmt)

logger = logging.getLogger('rossum')
logger.setLevel(logging.DEBUG)

logger.addHandler(fh)

if __name__ == '__main__':
    for item in range(1, 11):
        logger.debug('dummy log message : {}'.format(item))
        sleep(.5)
