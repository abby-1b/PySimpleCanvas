import math
sin, cos, tan, tanh = math.sin, math.cos, math.tan, math.tanh

def normalize(t):
    return t

def cap_dist(t, c=1):
    l = len(t)
    if l == 0:
        return []
    elif l == 1:
        return [max(min(t, c), -c)]
    elif l == 2:
        d = math.sqrt(t[0]*t[0] + t[1]*t[1])
        if d > c:
            return [t[0] / d, t[1] / d]
        return t

def add(a, b):
    return [a[0] + b[0], a[1] + b[1]]