import pickle

with open("file.txt", "rb") as f:
    x = pickle.load(f)
    print(x)
