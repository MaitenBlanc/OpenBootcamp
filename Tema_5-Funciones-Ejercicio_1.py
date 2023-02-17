def anioBisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                print("El año ", anio, " es bisiesto")
            else:
                print("El año ", anio, " no es bisiesto")
        else:
            print("El año ", anio, " es bisiesto")
    else:
        print("El año ", anio, " no es bisiesto")

anioBisiesto(1904)
anioBisiesto(2003)
anioBisiesto(2023)
anioBisiesto(2024)
