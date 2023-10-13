import numpy as np

def calculate(list):
    if len(list) < 9 :
        raise ValueError("List must contain nine numbers.")
    if len(list) > 9 :
        raise ValueError("List must contain nine numbers.")
    l = np.array(list).reshape(3,3)
    print(l.shape)
    print(l)
    print(l.ndim)
    calc = {
        "Mean" : [l.mean(axis=0), l.mean(axis=1), l.mean()],
        "Variance" : [l.var(axis=0), l.var(axis=1), l.var()],
        "Standard Deviation" : [l.std(axis=0), l.std(axis=1), l.std()],
        "Min" : (l.min(axis=0), l.min(axis=1), l.min()),
        "Max" : [l.max(axis=0), l.max(axis=1), l.max()],
        "Sum" : [l.sum(axis=0), l.sum(axis=1), l.sum()]
    }
    return calc