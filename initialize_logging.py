import logging.config


def init_logging_and_get_logger(caller_name):
    # This initial config has to be run once before getting module-level loggers.
    # It configures a root-level logger, which sets defaults for all other loggers
    logging.config.fileConfig(
        "logging.ini",
        # Without this setting, all existing loggers are disabled unless they or their
        # ancestor are explicitly named in the configuration
        disable_existing_loggers=False,
    )

    return logging.getLogger(caller_name)
