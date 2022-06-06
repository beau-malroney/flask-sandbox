import logging, logging.handlers, os

# # Log file location
# logfile = '/tmp/debug.log'
# # Define the log format
# log_format = (
#     '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s')

##########################
#LOG LEVEL VALUES
##########################
#Level - Numeric value
#CRITICAL - 50
#ERROR    - 40
#WARNING  - 30
#INFO     - 20
#DEBUG    - 10
#NOTSET   - 0
##########################
#LOG DIRECTORY PATH
logs_directory = "logs"

#File and Console Logging
def init_logging(append=False, console_loglevel=logging.DEBUG, loggerName=__name__):
    #Validate/Create logs_directory to store log files
    path = os.path.join(os.getcwd(),logs_directory)
    if not os.path.exists(path):
        os.makedirs(path)
    #File Logging Info
    log_file = os.path.join(path,f"{os.getenv('FLASK_CONFIG')}.log")
    if append:
        filemode_val = 'a'
    else:
        filemode_val = 'w'
    logging.basicConfig(level=logging.DEBUG,
                        format=f"[%(asctime)s] [{os.getenv('FLASK_CONFIG')} : %(levelname)-8s --:-- %(name)-10s] --> %(message)s",
                        filename=log_file,
                        filemode=filemode_val)
    # define a Handler which writes to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(console_loglevel)
    # set a format which is simpler for console use
    formatter = logging.Formatter("%(name)-10s --> %(message)s")
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)
    # logging.getLogger('').addHandler(logging.FileHandler(log_file))
    return logging.getLogger(loggerName) 

def name_logger(name):
    return logging.getLogger(name)