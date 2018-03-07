import coloredlogs
import logging

class Logger(object):

    def __init__(self):
        logger = logging.getLogger(__name__)
        coloredlogs.install(level='DEBUG', logger=logger)
        self.logger = logger

    def write(self, msg, level):
        try:
            if level == 'debug':
                self.logger.debug(msg)
            elif level == 'info':
                self.logger.info(msg)
            elif level == 'warning':
                self.logger.warning(msg)
            elif level == 'error':
                self.logger.error(msg)
            elif level == 'critical':
                self.logger.critical(msg)
            else:
                raise AttributeError('No appropriate log level was passed in')
        except AttributeError as e:
            self.write(e, 'critical')
        except Exception as e:
            self.write(e, 'critical')
