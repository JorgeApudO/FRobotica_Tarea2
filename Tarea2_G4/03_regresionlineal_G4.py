import numpy as np

def regresion_lineal(X,Y):

    Xt = np.transpose(X)
    A = np.matmul(Xt, X)
    Ainv = np.linalg.pinv(A)
    B = np.matmul(Xt, Y)

    return np.matmul(Ainv, B)


volts = [4,8,12]
estimaciones = [[],[]]

for volt in volts:

    name = 'datos/Escalón_' + str(volt) + 'V.txt'
    archivo = open(name, 'r')
    text = archivo.readlines()
    archivo.close()

    entrada_motor1 = []
    entrada_motor2 = []
    salida_motor1 = []
    salida_motor2 = []
    tiempo = []

    for line in text:
        line = line.strip('\n')
        line = line.split(',')
        if len(line) == 9:
            entrada_motor1.append(float(line[6]))
            entrada_motor2.append(float(line[7]))
            salida_motor1.append(float(line[4]))
            salida_motor2.append(float(line[5]))
            tiempo.append(len(tiempo))

    Y1 = np.array(salida_motor1[1:])
    Y2 = np.array(salida_motor2[1:])

    X1 = np.array([salida_motor1[:-1], entrada_motor1[1:]])
    X1 = np.transpose(X1)
    X2 = np.array([salida_motor2[:-1], entrada_motor2[1:]])
    X2 = np.transpose(X2)

    Theta1 = regresion_lineal(X1, Y1)
    Theta2 = regresion_lineal(X2, Y2)
    estimaciones[0].append(Theta1)
    estimaciones[1].append(Theta2)


print("Estimaciones")
print()
i=0
for motor in estimaciones:
    i+=1
    v=0
    for dato in motor:
        v+=4
        print(f"Motor {i}, Voltaje {v}")
        print(f"Theta 1: {dato[0]}, Theta 2: {dato[1]}")
    
