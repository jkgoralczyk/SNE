import random
import math

# Funkcja f
def f(u, temp):    
    return 1.0 / (1.0 + math.exp(((-1)*u)/temp)) 

# Funkcja wyswietlajaca wektor 
def printVector(x, time):
    for i in range(time):    
        print(f"x_{i}:", end=' ')
        for j in range(0,20):      
            if(x[i][j] == 1.0):        
                print("■ ", end='')      
            else:        
                print("□ ", end='')      
        print("")

# MB
def boltzmann(z, time, temp):

    # Generacja wektora c
    c = []
    for i in range(0,20):
            tmp = []    
            for j in range(0,20):        
                if i != j:            
                    tmp.append((z[i] - 0.5) * (z[j] - 0.5))        
                elif i == j:            
                    tmp.append(0.0)    
            c.append(tmp) 
    
    # Generacja wektora wag w
    w = []
    for i in range(0,20):        
        tmp = []        
        for j in range(0,20):            
            tmp.append(2.0*c[i][j])        
        w.append(tmp) 
    
    # Generacja alfa
    alfa = []
    for i in range(0,20):    
        sum = 0.0    
        for j in range(0,20):        
            sum += c[i][j]    
        alfa.append(sum)

    x = [] 
    for t in range(time): 
        if(t == 0):      
            # Generacja wektora losowego x
            tmp = []      
            for j in range(0,20):       
                tmp.append(random.randint(0, 1))      
            x.append(tmp)    
        elif t > 0:     
            # Generacja nastepnego wektora
            tmp = []      
            for i in range(0,20):        
                u = 0.0        
                for j in range(0,20):          
                    u = u + (w[i][j] * x[t-1][j])        
                u = u - alfa[i]        
                if f(u, t) >= random.uniform(0, 1):          
                    tmp.append(1.0)        
                else:          
                    tmp.append(0.0)      
        x.append(tmp)

    printVector(x, time) 

def main():
    
    # Definicja poczatkowego wektora z
    z = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
         1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

    #Definicja wartosci czasu i temperatur
    time = 5
    temps = [0.01, 0.1, 1, 10]

    for temp in temps:
        print(f"\nTemperatura: {temp}")
        boltzmann(z, time, temp)

main()    
