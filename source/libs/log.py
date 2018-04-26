import logbook, sys

class Logging:
    def __init__(self, name, **kwargs):
        '''
        Provides logging for our functions
        '''
        level = kwargs.pop('level', 'DEBUG')
        if level == 'DEBUG':
            level = logbook.DEBUG
        elif level == 'INFO':
            level = logbook.INFO
        else:
            level = logbook.DEBUG
        logbook.StreamHandler(sys.stdout).push_application()
        self._log = logbook.Logger(name, level = level)

    def debug(self, msg):
        self._log.debug(msg)
    def info(self, msg):
        self._log.info(msg)
    def warn(self, msg):
        self._log.warn(msg)
    def error(self, msg):
        self._log.error(msg)

