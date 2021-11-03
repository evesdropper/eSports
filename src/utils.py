# Utils
"""
Custom Exceptions and Helper Functions
"""
import pickle
import os

# file management
def join(path, file):
    return os.path.join(path, file)

# serialization
def write_object(obj, dir):
    with open(join(dir, f"{repr(obj)}.txt"), "wb") as f:
            pickle.dump(obj, f)

def read_object(obj, dir):
    pickle.load(open(join(dir, f"{repr(obj)}.txt"), "rb"))

# exceptions