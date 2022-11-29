import logging
from initialize_logging import get_logger


logger = get_logger(__name__)
logger.setLevel(logging.DEBUG)

logger.debug("hi I am here")

