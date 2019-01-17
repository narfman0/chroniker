import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.FileHandler("{0}/{1}.log".format(".", "chroniker")),
        logging.StreamHandler(),
    ],
)


def create_logger(name):
    return logging.getLogger(name)
