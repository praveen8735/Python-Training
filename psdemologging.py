import logging

#print(logging.getLogger())
#print()

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
logging.basicConfig(level=logging.DEBUG, format=fmt_str, filename='error.log')

logging.critical('panic error')
logging.debug('debug messages')
logging.info('confirmation notes')
logging.warning('warning information')
logging.error('an error messages')
