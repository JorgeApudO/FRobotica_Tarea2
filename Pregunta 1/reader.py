import matplotlib.pyplot as plt

volts = [4,8,12]

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

    plt.plot(tiempo,entrada_motor1)
    plt.xlabel("Tiempo")
    plt.ylabel("Volts")
    plt.title("Entrada Volts")
    name_fig = 'gráficos/Entrada_' + str(volt) + 'V_M1_G4.png'
    plt.savefig(name_fig)
    plt.clf()

    plt.plot(tiempo,entrada_motor2)
    plt.xlabel("Tiempo")
    plt.ylabel("Volts")
    plt.title("Entrada Volts")
    name_fig = 'gráficos/Entrada_' + str(volt) + 'V_M2_G4.png'
    plt.savefig(name_fig)
    plt.clf()

    plt.plot(tiempo,salida_motor1)
    plt.xlabel("Tiempo")
    plt.ylabel("RPM")
    plt.title("Salida Velocidad")
    name_fig = 'gráficos/Salida_' + str(volt) + 'V_M1_G4.png'
    plt.savefig(name_fig)
    plt.clf()

    plt.plot(tiempo,salida_motor2)
    plt.xlabel("Tiempo")
    plt.ylabel("RPM")
    plt.title("Salida Velocidad")
    name_fig = 'gráficos/Salida_' + str(volt) + 'V_M2_G4.png'
    plt.savefig(name_fig)
    plt.clf()

