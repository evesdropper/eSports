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
def write_object(obj):
    with open(f"{repr(obj)}.txt", "wb") as f:
            pickle.dump(obj, f)

def read_object(file):
    pickle.load(open(file, 'rb'))

# exceptions