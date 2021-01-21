import os
import pickle

with open(os.path.join(os.path.dirname(__file__), "NaverBlog.pkl"), "rb") as f:
    data = pickle.load(f)

print(data)