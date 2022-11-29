from initialize_logging import init_logging_and_get_logger


logger = init_logging_and_get_logger(__name__)


def add(x, y):
    logger.debug("adding {x} and {y}")
    raise Exception("Oh no")
    return x + y
