from typing import Literal
from datetime import datetime
from contextlib import ContextDecorator

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class ContextLogger(ContextDecorator):
    def __init__(
        self,
        logger,
        action: str,
        log_level: LogLevel = "DEBUG",
    ):
        self.logger = logger
        self.action = action
        if log_level == "DEBUG":
            self.log_func = self.logger.debug
        elif log_level == "INFO":
            self.log_func = self.logger.info
        elif log_level == "WARNING":
            self.log_func = self.logger.warning
        elif log_level == "ERROR":
            self.log_func = self.logger.error
        elif log_level == "CRITICAL":
            self.log_func = self.logger.critical
        else:
            raise ValueError(
                f"Invalid log level: {log_level}; "
                "must be one of DEBUG, INFO, WARNING, ERROR, CRITICAL."
            )

    def __enter__(self):
        self.start_time = datetime.now()
        self.log_func(f"Started {self.action}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = datetime.now()
        elapsed = (end_time - self.start_time).total_seconds() * 1000
        self.log_func(f"Finished {self.action} (elapsed: {elapsed:.2f} ms)")
