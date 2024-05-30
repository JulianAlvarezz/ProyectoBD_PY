#Rutina para generar de forma aleatoria múltiples datos con python
import random

def generarDatosPluviometrico():
    listaDatos=[]
    for i in range(1000):
        municipio=random.choice(['Bello', 'Envigado', 'Sabaneta', 'Itagui', 'Belen', 'Medellin'])
        lluviasXhora=random.choice(['3000','4500', '5000', '10000', '1000', '20000'])
        lluviasXsemana=random.choice(['3000','4500', '5000', '10000', '1000', '20000'])
        lluviasXmes=random.choice(['3000','4500', '5000', '10000', '1000', '20000'])
        precipitacion=random.choice(['3000','4500', '5000', '10000', '1000', '20000'])
        id=random.randint(0,1000000)
        pluviometrico=[municipio,lluviasXhora,lluviasXsemana,lluviasXmes,precipitacion,id]
        
        listaDatos.append(pluviometrico)
    return listaDatos
print(generarDatosPluviometrico())

