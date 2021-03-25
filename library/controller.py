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

def update_speed(d, position="pos", velocity="vel", friction=0.9, v_friction=True):
    if v_friction:
        try:
            d[velocity] = [a * friction for a in d[velocity]]
            d[position] = [d[position][a] + d[velocity][a] for a in range(len(d[position]))]
        except:
            setattr(d, velocity, [a * friction for a in getattr(d, velocity)])
            setattr(d, position, [getattr(d, position)[a] + getattr(d, velocity)[a] for a in range(len(d[position]))])
    else:
        b_v = d[velocity][1]
        try:
            d[velocity] = [a * friction for a in d[velocity]]
            d[velocity][1] = b_v
            d[position] = [d[position][a] + d[velocity][a] for a in range(len(d[position]))]
        except:
            setattr(d, velocity, [a * friction for a in getattr(d, velocity)])
            setattr(d, velocity, [(b_v if i == 1 else b_v) for i, a in enumerate(getattr(d, velocity))])
            setattr(d, position, [getattr(d, position)[a] + getattr(d, velocity)[a] for a in range(len(d[position]))])
