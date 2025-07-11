import time
import re
import pytest
from context_logger.context_logger import ContextLogger


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


def test_context_logger_debug():
    dummy = DummyLogger()
    with ContextLogger(dummy, "test-event", log_level="DEBUG"):
        pass
    assert dummy.records[0][0] == "DEBUG"
    assert dummy.records[0][1].startswith("Started test-event")
    assert dummy.records[1][0] == "DEBUG"
    assert dummy.records[1][1].startswith("Finished test-event")
    assert "elapsed:" in dummy.records[1][1]


def test_context_logger_info():
    dummy = DummyLogger()
    with ContextLogger(dummy, "info-event", log_level="INFO"):
        pass
    assert dummy.records[0][0] == "INFO"
    assert dummy.records[1][0] == "INFO"


def test_context_logger_elapsed_time():
    dummy = DummyLogger()
    with ContextLogger(dummy, "timed-event", log_level="DEBUG"):
        time.sleep(0.05)
    finish_msg = dummy.records[1][1]
    match = re.search(r"elapsed: ([0-9.]+) ms", finish_msg)
    assert match, "Elapsed time not found in finish message"
    elapsed = float(match.group(1))
    assert elapsed >= 50, f"Elapsed time too short: {elapsed} ms"


def test_context_logger_invalid_level():
    dummy = DummyLogger()
    with pytest.raises(ValueError):
        ContextLogger(dummy, "bad", log_level="NOTALEVEL")
