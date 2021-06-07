import logging
logging.basicConfig(format="%(asctime)s %(levelname)s %(filename)s %(message)s", filename='file.log',
                    level=logging.DEBUG, filemode='a', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger('LOG')
