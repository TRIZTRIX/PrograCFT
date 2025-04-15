#Dar la bienvenida al usuario
print("Bienvenidos a la compañia telefónica ClaroStar")
#Socilitar al cliente ingresar los datos
dia= int (input("Por favor ingrese los minutos hablados durante el día: "))
noche= int (input("Por favor ingrese los minutos hablados durante la noche: "))

# Variables que se van a calcular
costo_dia=0
costo_noche=0
exceso_dia=0
exceso_noche=0

#Calculos de los costos por minuto y excedentes por minuto
if dia <= 100:
    costo_dia = dia * 10

else:
    exceso_dia = dia - 100
    costo_dia = (100 * 10) + (exceso_dia * 15)

if noche <= 80:
    costo_noche = noche * 7

else:
    exceso_noche = noche - 80
    costo_noche = (80 * 7) + (exceso_noche * 13)

#Cálculo del monto total
total = costo_dia + costo_noche

#Muestrar por pantalla los resultados
print(f"Exceso en horario día: {exceso_dia} minutos")
print(f"Exceso en horario noche: {exceso_noche} minutos")
print(f"Total a pagar: {total} CLP") 

#Mostrar por pantalla si el cliente excedió o no con el plan 
if exceso_dia > 0 and exceso_noche > 0:
    print("El cliente excedio los minutos del plan")
elif exceso_dia > 0:
    print("El cliente excedio los minutos del horario diurno")
elif exceso_noche > 0: 
    print("El cliente excedio los minutos del plan nocturno")
else:
    print("El cliente, no excedio los minutos del plan")

