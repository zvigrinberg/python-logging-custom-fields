import logging
import threads_traceids
import threading

logger = logging.getLogger("app_utils")


def print_cube(num):
    threads_traceids.add_trace_id("fdskljl2k42209ujf")
    logger.info("Cube: {}".format(num * num * num))
    threads_traceids.delete_trace_id()


def print_square(num):
    threads_traceids.add_trace_id("kj4kl3094u0u023434")
    logger.info("Square: {}".format(num * num))
    threads_traceids.delete_trace_id()


def another_way():
    logger.info("bla bla 1")
    logger.info("bla bla 2")
    threads_traceids.delete_trace_id()
    threads_traceids.add_trace_id("fdskljl2k42209ujf")
    logger.info("bla bla 3")
    t1 = threading.Thread(target=print_square, args=(10,))
    logger.info("bla bla 4")
    t2 = threading.Thread(target=print_cube, args=(10,))
    logger.info("bla bla 5")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    logger.info("Done")
    logger.info(f"thread traces dunp=>{str(threads_traceids.trace_ids)}")
