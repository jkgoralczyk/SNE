import random

# Definicja wartosci epsilon i c
epsilon = 0.00001
c = 0.01

# Funkcja sprawdzajaca warunek stopu
def check_epsilon(x_new, v_old):
    sum = 0.0
    for i in range(len(x_new)):
        sum += abs(x_new[i] - v_old[i])
    if sum < epsilon:
        return False
    return True

# Funkcja obliczajaca pierwszy gradient
def gradient1():

    # Funkcja dla której obliczamy gradient
    print("f(x, y) = 2x^2 + y^2 - 2xy - 2x + 1\n")

    # Generowanie listy 2 losowych liczb zmiennoprzecinkowych z przediału <-5,5>
    x_old = [round(random.uniform(-5, 5), 2) for i in range(2)]
    print(f"Wartosci: {x_old}")
    
    x_new = list(x_old)  
    flag = True
    while(flag):
        x_new[0] = x_old[0] - c * (4 * x_old[0] - 2 * (x_old[1] + 1))
        x_new[1] = x_old[1] - c * (2 * x_old[1] - 2 * x_old[0])
        flag = check_epsilon(x_new, x_old) 
        x_old = list(x_new)

    print(f"Punkt: {x_new}")

    #Obliczanie wartosci minimum
    value_min = 2 * (x_new[0] ** 2) + x_new[1] ** 2 - 2 * x_new[0] * x_new[1] - 2 * x_new[0] + 1
    print(f"Wartość: {value_min}")

# Funkcja obliczajaca drugi gradient
def gradient2():

    # Funkcja dla której obliczamy gradient
    print("f(x, y) = (x^4)/2 - (x^3)/3 - (x^2)/2 + y^2 - 2*y + 1\n")

    # Generowanie listy 2 losowych liczb zmiennoprzecinkowych z przediału <-5,5>
    x_old = [round(random.uniform(-5, 5), 2) for i in range(2)]
    print(f"Wartosci: {x_old}")
    
    x_new = list(x_old)  
    flag = True
    while(flag):
        x_new[0] = x_old[0] - c * ( x_old[0] * ( 2 * (x_old[0] ** 2) - x_old[0] - 1) )
        x_new[1] = x_old[1] - c * ( 2 * ( x_old[1] - 1) )
        flag = check_epsilon(x_new, x_old) 
        x_old = list(x_new)

    print(f"Punkt: {x_new}")

    #Obliczanie wartosci minimum
    value_min = (x_new[0] ** 4) / 2 - (x_new[0] ** 3) / 3 - (x_new[0] ** 2) / 2 + x_new[1] ** 2 - 2 * x_new[1] + 1
    print(f"Wartość: {value_min}")

def main():
    print("\nPierwszy gradient")
    gradient1()
    print("\nDrugi gradient")
    gradient2()

main()

