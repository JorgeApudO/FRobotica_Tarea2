import matplotlib.pyplot as plt

volts = [4]

for volt in volts:


    name = 'datos/Escalón_' + str(volt) + 'V.txt'
    archivo = open(name, 'r')
    text = archivo.readlines()
    archivo.close()

    new_text = []

    for line in text:
        line = line.split(',')
        new_text.append(line)
    t_inicio = float(new_text[1][1])
    t_final = float(new_text[len(new_text)-2][1])
    num = len(new_text) - 2

print(num)

print(len(text))


promedio = int((t_final-t_inicio)/num)
print(promedio)

