# --coding:GBK --

import inspect
import ctypes



def _async_raise(tid, exctype):
    """
    线程异常
    :param tid:
    :param exctype:
    :return:
    """
    try:
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
    except:
        pass

def stop_thread(thread):
    """
    线程终止
    :param thread:
    :return:
    """
    _async_raise(thread.ident, SystemExit)
