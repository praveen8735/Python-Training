import logging

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
fmt = logging.Formatter(fmt_str)  # what?

fh = logging.FileHandler('access.log') # where?
sh = logging.StreamHandler()
fh.setFormatter(fmt)
sh.setFormatter(fmt)


logger = logging.getLogger('rossum')
logger.setLevel(logging.DEBUG)

logger.addHandler(fh)
logger.addHandler(sh)
