#!/usr/bin/python
# -*-coding:utf-8-*-
from initialize_logging import init_logging_and_get_logger

from sub_module.another_file import add

logger = init_logging_and_get_logger(__name__)


def run():
    test = "test"
    logger.debug("OH NO EVERYTHONG CHAGED")
    logger.info("About to run add")
    logger.warning(f"About to run add {test}")
    add(2, 3)


if __name__ == "__main__":
    run()


# Changes
# * Put all script code into a single entrypoint function, e.g. run()
# * Add if __name__ == "__main__" to protect code from being execued on import
# * Move all top-level entrypoints to an "entrypoints" folder
#   * For temporary backwards-compatibility during transition, leave files of same name
#     in the top-level, which import & run script code
# * Add entrypoints configuration in setup.cfg
