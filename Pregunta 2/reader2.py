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

    vel_ant1 = None
    vel_ant2 = None
    tiempo_buscado = None

    for line in text:
        line = line.strip('\n')
        line = line.split(',')
        if len(line) == 9:
            if vel_ant1 == float(0) and vel_ant2 == float(0) and float(line[4]) != float(0) and float(line[5]) != float(0) and tiempo_buscado == None and float(line[1]) != 376735500.0:
                tiempo_buscado = float(line[1])
            vel_ant1 = float(line[4])
            vel_ant2 = float(line[5])

    print(tiempo_buscado)

    tiempo_inicio = tiempo_buscado - 5*1000000
    tiempo_final = tiempo_buscado + 5*1000000

    new_text_M1 = ''
    new_text_M2 = ''

    for line in text:
        line = line.strip('\n')
        line = line.split(',')
        if len(line) == 9:
            if float(line[1]) >= tiempo_inicio and float(line[1]) <= tiempo_final:
                entrada_motor1.append(float(line[6]))
                entrada_motor2.append(float(line[7]))
                tiempo.append(len(tiempo))
                if float(line[1]) < tiempo_buscado:
                    salida_motor1.append(float(0))
                    salida_motor2.append(float(0))
                    new_text_M1 += line[0] + ',' + line[1] + ',' + line[2] + ',' + str(0.0)  + ','  + line[6] + ',' + line[8] + '\n'
                    new_text_M2 += line[0] + ',' + line[1] + ',' + line[3] + ',' + str(0.0)  + ','  + line[7] + ',' + line[8] + '\n'

                else:
                    salida_motor1.append(float(line[4]))
                    salida_motor2.append(float(line[5]))
                    new_text_M1 += line[0] + ',' + line[1] + ',' + line[2] + ',' + line[4] + ','  + line[6] + ',' + line[8] + '\n'
                    new_text_M2 += line[0] + ',' + line[1] + ',' + line[3] + ',' + line[5] + ','  + line[7] + ',' + line[8] + '\n'


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

    
    nombre = 'datos_entregables/02_escalón_' + str(volt) + 'V_M1_G4.txt'
    new_archivo = open(nombre, 'w')
    new_archivo.write(new_text_M1)
    new_archivo.close()


    nombre = 'datos_entregables/02_escalón_' + str(volt) + 'V_M2_G4.txt'
    new_archivo = open(nombre, 'w')
    new_archivo.write(new_text_M2)
    new_archivo.close()