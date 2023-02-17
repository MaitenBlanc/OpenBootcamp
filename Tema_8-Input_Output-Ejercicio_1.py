f = open('fichero.txt', 'w')
f.write('Mi primer fichero\n')
f.close()

f = open('fichero.txt', 'r+')
f.readline()
f.write('Otra línea en el fichero\n')

f.seek(0)
print(f.read())
f.close()