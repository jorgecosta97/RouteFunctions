import pandas as pd
import math

def routespertime(indata, dt): #indata - array with end time and duration in decimal format; dt - time interval in decimal format 1 => 1 hour
    t = 0
    tp = []
    vn = []
    pc = []
    while t!=24:
        r = 0
        for n in range(0, len(indata)):
            a = indata[n][0]  # end time
            b = indata[n][1]  # duration
            if (a>=t or a-b<0) and (t > a-b-dt %24): r+=1
        f, i = math.modf(t)
        f1, i1 = math.modf(t+dt)
        tp.append(f"{int(i):02}:{int(f*60):02} - {int(i1):02}:{int(f1*60):02}")
        vn.append(r)
        pc.append((r/len(indata))*100)
        t+=dt
    dict = {'time_Period': tp, 'Routes (N.)': vn, 'Routes (%)': pc}
    out = pd.DataFrame(dict)
    return out

