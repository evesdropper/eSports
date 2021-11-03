# Utils
"""
Custom Exceptions and Helper Functions
"""
import pickle

# serialization
def write_object(obj, file):
    pickle.dump(obj, open(file, 'wb'))

def read_object(file):
    pickle.load(open(file, 'rb'))

# exceptions