import inspect
import logging


class LoggingSetup:

    def sample_logger(loglevel=logging.DEBUG):
        # Create logger
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        # Create console handler [ch] and set level(in our case) to DEBUG
        ch = logging.StreamHandler()
        ch.setLevel(loglevel)

        # Format your logger
        formatter = logging.Formatter('%(levelname)s - %(asctime)s: %(name)s - %(message)s')
        # Add your logger format to ch
        ch.setFormatter(formatter)

        # Add ch to logger
        logger.addHandler(ch)
        return logger
