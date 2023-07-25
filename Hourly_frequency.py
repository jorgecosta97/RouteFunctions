### Array with the end time and duration of the route.
input_data = [[13, 7],
              [18, 10],
              [8, 7],
              [23, 10],
              [2, 7]] 

def routespertime(indata, t, dt):
    n_routes = 0
    for n in range(0, len(indata)):
        a = indata[n][0]  # start time
        b = indata[n][1]  # duration
        if (a>=t or a-b<0) and (t > a-b-dt %24): n_routes+=1
    return n_routes

print (routespertime(input_data, 17, 1))
