import pickle

with open("Результат.txt", "rb") as f:
    x = pickle.load(f)
    print(x)
