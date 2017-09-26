def radiationExposure(start, stop, step):
    if start - stop >= 0:
        return 0
    else:
        return float(f(start))*step + radiationExposure(start+step,stop,step)