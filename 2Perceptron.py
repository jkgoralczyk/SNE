def f(inputs,weights,m):
    x = 0.0
    for i in range (m):
        x += (weights[i] * inputs[i]) 
    if x >= 0:
        return 1
    else:
        return 0 

def z(t):
    if (t % 5 + 1) <= 3:
        return 1.0
    else:
        return 0.0

def main():
    u = []
    u.append([
        0,0,0,0,0,
        0,1,1,0,0,
        0,0,1,0,0,
        0,0,1,0,0,
        0,0,1,0,0,1
    ])
    u.append([
        0,0,1,1,0,
        0,0,0,1,0,
        0,0,0,1,0,
        0,0,0,0,0,
        0,0,0,0,0,1
    ])
    u.append([
        0,0,0,0,0,
        1,1,0,0,0,
        0,1,0,0,0,
        0,1,0,0,0,
        0,1,0,0,0,1
    ])
    u.append([
        0,0,0,0,0,
        0,1,1,1,0,
        0,1,0,1,0,
        0,1,1,1,0,
        0,0,0,0,0,1
    ])
    u.append([
        0,0,0,0,0,
        0,0,0,0,0,
        1,1,1,0,0,
        1,0,1,0,0,
        1,1,1,0,0,1
    ])

    for c in [1.0, 0.1, 0.01]:
        w  = list(range(26))
        w[:] = [1.0] *26
        t = 1
        counter = 0.0

    while (counter < 5.0):
        zt = z(t)
        yt = f(u[t % 5], w, len(w))
        for i in range(26):
            w[i] = w[i] + c * (zt - yt) * u[t % 5][i]
        t += 1
        if (zt == yt):
            counter += 1.0
        else:
            counter = 0.0
        print("counter: {} time: {}".format(c,t))
        print("-------------")
        for i in range(len(w)):
            print("weight {} : {}".format(i,w[i]))
        print("-------------\n")
            
main()