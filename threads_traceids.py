import threading
from threading import Lock

trace_ids = dict()

trace_ids_dict_lock = Lock()


def add_trace_id(trace_id: str):
    with trace_ids_dict_lock:
        thread_name = threading.get_native_id()
        trace_ids[thread_name] = trace_id


def delete_trace_id():
    with trace_ids_dict_lock:
        thread_name = threading.get_native_id()
        trace_ids[thread_name] = ""


def get_trace_id() -> str:
    with trace_ids_dict_lock:
        thread_name = threading.get_native_id()
        return trace_ids[thread_name]
