def f(inputs,weights,m):
    x = float(0)
    for i in range (m):
        x += (weights[i] * inputs[i]) 
    if x >=0:
        return 1
    else:
        return 0 

def Not():
    weights = [float(-0.5),float(0.3)]
    inputs = []
    m = 2
    inputs.append(float(int(input("U1: "))))
    inputs.append(float(1))
    print("Wynik: {}".format(f(inputs,weights,m)))

def And():
    weights = [float(0.3),float(0.3),float(-0.5)]
    inputs = []
    m = 3
    inputs.append(float(int(input("U1: "))))
    inputs.append(float(int(input("U2: "))))
    inputs.append(float(1))
    print("Wynik: {}".format(f(inputs,weights,m)))

def Nand():
    weights = [float(-0.4),float(-0.4),float(0.6)]
    inputs = []
    m = 3
    inputs.append(float(int(input("U1: "))))
    inputs.append(float(int(input("U2: "))))
    inputs.append(float(1))
    print("Wynik: {}".format(f(inputs,weights,m)))

def Or():
    weights = [float(0.3),float(0.3),float(-0.2)]
    inputs = []
    m = 3
    inputs.append(float(int(input("U1: "))))
    inputs.append(float(int(input("U2: "))))
    inputs.append(float(1))
    print("Wynik: {}".format(f(inputs,weights,m)))

def main():
    print("1.NOT GATE\n2.AND GATE\n3.NAND GATE\n4.OR GATE")
    x = int(input())
    if (x == 1):
        Not()
    elif (x == 2):
        And()
    elif (x == 3):
        Nand()
    elif (x == 4):
        Or()
    else:
        pass

main()