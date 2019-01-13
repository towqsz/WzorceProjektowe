import threading


class Singleton(type):
    _instances = {}
    _lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class F1(metaclass=Singleton):
    pass

class F2(metaclass=Singleton):
    pass

class S1_F1(F1):
    pass

class S2_F1(F1):
    pass

class S1_F2(F2):
    pass

class S2_F2(F2):
    pass

class T1_S1F1(S1_F1):
    pass

class T2_S1F1(S1_F1):
    pass

class T1_S2F1(S2_F1):
    pass

class T2_S2F1(S2_F1):
    pass

