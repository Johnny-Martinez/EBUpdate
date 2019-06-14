import logging
import time


# By default only warning messages or higher are logged unless explicitly set in level.

# Create format String for formatting messages
LOG_FORMAT = '%(levelname)s %(asctime)s %(message)s'
logging.basicConfig(filename='log_file', level=logging.DEBUG,
                    format=LOG_FORMAT, filemode='w')


# LOG_FORMAT = '%(levelname)s %(asctime)s %(message)s'
# logging.basicConfig(filename='log_file', level=logging.DEBUG,
#                     format=LOG_FORMAT, filemode='w')

logger = logging.getLogger()

logger.debug('DEBUG MESSAGE')
logger.info('INFO message')
logger.warning('WARNING message')
logger.error('ERROR message')
logger.critical('CRITICAL message')
print(logger.level)
