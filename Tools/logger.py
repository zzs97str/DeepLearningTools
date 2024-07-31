import logging

'''%(asctime)s:  a timestamp that indicates when the log message was generated. 
    name: The name of the logger that created the log record. 
    levelname: The severity level of the log message (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
    message: The actual message to be logged. This is the content you want to log.
    funcName: The name of the function where the logging call was made. 
    %s is used to specify the location where a string value should be inserted.
    '''

# Configure the logging module here; any subsequent configurations will be ineffective
logging.basicConfig(filename="your_log_path.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s',
                    level=logging.INFO,
                    filemode='w')

# create a logger object
logger = logging.getLogger(__name__)

# Debug level logs, used for printing debugging information, the lowest level
logger.debug('Debug, used to print some debugging information, the lowest level')
# Info level logs, used for printing normal operation information
logger.info('Info, used to print some normal operation information')
# Warning level logs, used for printing warning messages
logger.warning('Warning, used to print warning messages')
# Error level logs, generally used for printing error messages
logger.error('Error, generally used to print some error messages')
# Critical level logs, used for printing critical error messages, the highest level
logger.critical('Critical, used to print critical error messages, the highest level')
