import inspect

def control_2d_WASD(d, position="pos", velocity="vel", acceleration=1, friction=0.9):
    g = dict(inspect.getmembers(inspect.stack()[1][0]))["f_globals"]
    if "w" in g["keys_pressed"]: d[velocity][1] -= acceleration
    if "a" in g["keys_pressed"]: d[velocity][0] -= acceleration
    if "s" in g["keys_pressed"]: d[velocity][1] += acceleration
    if "d" in g["keys_pressed"]: d[velocity][0] += acceleration
    
    d[velocity][0] *= friction
    d[velocity][1] *= friction

    d[position][0] += d[velocity][0]
    d[position][1] += d[velocity][1]
