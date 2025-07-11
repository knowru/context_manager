import re
import pytest
from context_logger.context_logger_factory import ContextLoggerFactory


class DummyLogger:
    def __init__(self):
        self.records = []

    def debug(self, msg):
        self.records.append(("DEBUG", msg))

    def info(self, msg):
        self.records.append(("INFO", msg))

    def warning(self, msg):
        self.records.append(("WARNING", msg))

    def error(self, msg):
        self.records.append(("ERROR", msg))

    def critical(self, msg):
        self.records.append(("CRITICAL", msg))


def test_factory_creates_context_logger_and_logs():
    dummy = DummyLogger()
    factory = ContextLoggerFactory(dummy)
    with factory("my-event", log_level="DEBUG"):
        pass
    assert dummy.records[0][0] == "DEBUG"
    assert dummy.records[1][0] == "DEBUG"
    assert "Started my-event" in dummy.records[0][1]
    assert "Finished my-event" in dummy.records[1][1]
    assert "elapsed:" in dummy.records[1][1]


def test_factory_includes_location():
    dummy = DummyLogger()
    factory = ContextLoggerFactory(dummy)

    def some_func():
        with factory("loc-event", log_level="INFO"):
            pass

    some_func()
    # The event string should include module, function, and line number
    start_msg = dummy.records[0][1]
    assert re.search(r"loc-event @ .*some_func:\d+", start_msg)


def test_factory_invalid_level():
    dummy = DummyLogger()
    factory = ContextLoggerFactory(dummy)
    with pytest.raises(ValueError):
        with factory("bad", log_level="NOTALEVEL"):
            pass
