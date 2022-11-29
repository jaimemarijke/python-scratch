from initialize_logging import get_logger

logger = get_logger(__name__)


def add(x, y):
    logger.debug("adding {x} and {y}")
    raise Exception("Oh no")
    return x + y
