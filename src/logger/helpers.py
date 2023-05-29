import logging
import os


def logging_config():
    # create a directory for logging
    log_dir = "log"
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger("slack-bot")
    logger.setLevel(level=logging.DEBUG)
    fh = logging.FileHandler(filename="log/logs.log")
    fh_formatter = logging.Formatter('%(asctime)s %(levelname)s %(lineno)d:%(filename)s(%(process)d) - %(message)s')
    fh.setFormatter(fh_formatter)
    logger.addHandler(fh)