import pickle

def save_file(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)

def load_file(path):
    with open(path, 'rb') as f:
        return pickle.load(f)
