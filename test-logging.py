import logging
import sys

import threads_traceids
from app_utils import another_way

old_factory = logging.getLogRecordFactory()

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(threadName)s- traceId=%(traceId)s - %(name)s - %(levelname)s -'
                              ' %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)
traceIdValue = " "


def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.traceId = threads_traceids.get_trace_id()
    return record


logging.setLogRecordFactory(record_factory)
threads_traceids.add_trace_id("fsdfbfsfssfs")

logger = logging.getLogger("test-logging")
logger.info("hello world")
logger.info("hello world 2")
logger.info("hello world 3")
another_way()
