import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print("Hora de ir a casa!")
else:
    horaTrabajo = (18 - int(hora))
    minutosTrabajo = (59 - int(minutos))
    print("Quedan ", horaTrabajo, ":", minutosTrabajo, " para ir a casa")

