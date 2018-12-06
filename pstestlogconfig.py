from pslogconfig import logger
from time import sleep


for item in range(1, 11):
    logger.debug('dummy log message : {}'.format(item))
    sleep(.5)
