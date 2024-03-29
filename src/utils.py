# Utils
"""
Custom Exceptions and Helper Functions
"""
import pickle
import os

# file management
def join(path, file):
    return os.path.join(path, file)

def clean_dirs(dir):
    for file in os.listdir(dir):
        os.remove(join(dir, file))

# serialization
def write_object(obj, dir):
    with open(join(dir, f"{repr(obj)}.txt"), "wb") as f:
            pickle.dump(obj, f)

def read_object(obj, dir):
    load = pickle.load(open(join(dir, f"{repr(obj)}.txt"), "rb"))
    return load

# exceptions
class ESportsException(Exception):
    """
    Custom Exception
    """
    pass