import inspect
from context_logger.context_logger import ContextLogger, LogLevel


class ContextLoggerFactory:
    def __init__(self, logger):
        self.logger = logger

    def __call__(self, event: str, log_level: LogLevel = "DEBUG"):
        frame = inspect.currentframe().f_back
        module = inspect.getmodule(frame)
        modulename = module.__name__ if module else "<unknown>"
        funcname = frame.f_code.co_name
        lineno = frame.f_lineno

        return ContextLogger(
            self.logger,
            f"{event} @ {modulename}.{funcname}:{lineno}",
            log_level=log_level,
        )
