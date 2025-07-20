import logging
import os

def setup_logger(log_file='automation.log'):
    log_path = os.path.join(os.getcwd(), log_file)

    logging.basicConfig(
        filename=log_path,
        filemode = 'a',
        format = '[%(asctime)s] %(message)s',
        level=logging.INFO
    )
    return logging.getLogger()