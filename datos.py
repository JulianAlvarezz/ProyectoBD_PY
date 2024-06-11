import pandas as pd
import matplotlib.pyplot as plt
 
x=["enero","febrero","marzo","abril","marzo","junio","julio","agosto","septiembre","octubre","novimebre","diciebre"]
y=[45,76,12,20,80,50,78,98,100,110,120,130]
data={
    'mes':x,
    'nivel':y
}
archivoHTML=pd.DataFrame(data).to_html()
archivo=open("./data/prueba3.XLSX","w")
archivo.write(archivoHTML)
archivo.close()

#colores=["#2A5C30","#185286","#9E6114","#A9BB0D","#BB0D15","#2A5C30","#185286","#9E6114","#A9BB0D","#BB0D15"]
#x1=["enero","febrero","marzo","abril","marzo","junio","julio","agosto","septiembre","octubre","novimebre","diciebre"]
#y1=[50,60,70,80,90,100,110,120,130,140,150,150]
#plt.plot(x,y,marker='o',linestyle="--",color="g", label="Medellin")#b,g,r,c,m,y,k
#plt.plot(x1,y1,marker='4',linestyle="-",color="b", label="Bello")#b,g,r,c,m,y,k
#plt.bar(x,y,color=colores)
#plt.pie(y,labels=x)#torta
#plt.xlabel("Mes del año")
#plt.ylabel("Estudiantes Nuevos")
#plt.title("ESTUDIANTES MATRICULADOS")

#plt.show()



# Leer el archivo Excel usando openpyxl
#tabla = pd.read_excel("./data/prueba3.xlsx", engine='openpyxl')
# Mostrar todas las filas del DataFrame
#print(tabla.to_string())#muetra toda la data
#print ("\n")
#print(tabla.head())#Mostrando los primeros 5 registros
#print ("\n")
#print(tabla.tail())#Mostrando los ultimos 5 registros
#print("\n")
#print(tabla.describe())#Obtenemos un nuevo DataFrame con estadísticas de nuestros datos
#print("\n")
