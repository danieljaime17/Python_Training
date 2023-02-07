cantidad = float(input("Introduzca un valor a invertir: "))

interes = float(input("Introduzca el interes: "))

años = float(input("Introduzca los años: "))

print("Capital final: " + str( round( cantidad * ( interes / 100 + 1 ) ** años )))