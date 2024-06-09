import pandas as pd

from data.generators.generadorCalidadAire import generarDatosCalidadAire
from helpers.generarTabla import crearTablaHTML

#1. PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME 

def construirDataFrameCalidadAire():
    #traigo los datos generados en el mock
    datosCalidadAire=generarDatosCalidadAire()
    
    #construyo el dataframe
    calidadAireDF=pd.DataFrame(datosCalidadAire, columns=['comuna', 'poblacionTotal', 'muestra', 'ICA', 'fecha', 'nombre', 'id'])  
    
    # Limpiando DF
    # 1. Limpiando Reemplazando valores
    calidadAireDF.replace('-', pd.NA, inplace=True)
    calidadAireDF.replace('sin', pd.NA, inplace=True)

    # 2. Limpiando Eliminando valores
    #calidadAireDF.replace('sin', pd.NA, inplace=True)
    #calidadAireDF.dropna(inplace=True)

    #probando
    #print("\n")
    #print(calidadAireDF)
    #crearTablaHTML(calidadAireDF,"calidadAire")

    # Filtrando datos según el valor de ICA
    filtroICAPositivo = calidadAireDF.query("(ICA >= 20) and (ICA < 50)")
    filtroICAModerado = calidadAireDF.query("(ICA >= 50) and (ICA < 70)")
    filtroICAPeligroso = calidadAireDF.query("(ICA >= 70)")

    # Conteo
    cuentaPositivo = filtroICAPositivo.groupby('comuna')['ICA'].count()
    cuentaModerado = filtroICAModerado.groupby('comuna')['ICA'].count()
    cuentaPeligroso = filtroICAPeligroso.groupby('comuna')['ICA'].count()
    
    print("Conteo de ICA positivo por comuna: ", cuentaPositivo)
    print("Conteo de ICA moderado por comuna: ", cuentaModerado)
    print("Conteo de ICA peligroso por comuna: ", cuentaPeligroso)
    
    # Creando DataFrames para los conteos
    cuentaPositivoDF = cuentaPositivo.reset_index().rename(columns={'ICA': 'Conteo ICA Positivo'})
    cuentaModeradoDF = cuentaModerado.reset_index().rename(columns={'ICA': 'Conteo ICA Moderado'})
    cuentaPeligrosoDF = cuentaPeligroso.reset_index().rename(columns={'ICA': 'Conteo ICA Peligroso'})
    
    # Creando tablas HTML
    crearTablaHTML(cuentaPositivoDF, "conteoICA_Positivo")
    crearTablaHTML(cuentaModeradoDF, "conteoICA_Moderado")
    crearTablaHTML(cuentaPeligrosoDF, "conteoICA_Peligroso")
    
    #cuentaPositivoDF=pd.DataFrame(datosCalidadAire, columns=['comuna', 'poblacionTotal', 'muestra', 'ICA', 'fecha', 'nombre', 'id'] )
    #crearTablaHTML(cuentaPositivoDF, "cuentaPositivo")
    
    # Suma
    sumaPositivo = filtroICAPositivo.groupby('comuna')['ICA'].sum()
    sumaModerado = filtroICAModerado.groupby('comuna')['ICA'].sum()
    sumaPeligroso = filtroICAPeligroso.groupby('comuna')['ICA'].sum()
    
    
    # Creando DataFrames para las sumas
    sumaPositivoDF = sumaPositivo.reset_index().rename(columns={'ICA': 'Suma ICA Positivo'})
    sumaModeradoDF = sumaModerado.reset_index().rename(columns={'ICA': 'Suma ICA Moderado'})
    sumaPeligrosoDF = sumaPeligroso.reset_index().rename(columns={'ICA': 'Suma ICA Peligroso'})

    # Creando tablas HTML
    crearTablaHTML(sumaPositivoDF, "sumaICA_Positivo")
    crearTablaHTML(sumaModeradoDF, "sumaICA_Moderado")
    crearTablaHTML(sumaPeligrosoDF, "sumaICA_Peligroso")

    # Promedio
    promedioPositivo = sumaPositivo / cuentaPositivo
    promedioModerado = sumaModerado / cuentaModerado
    promedioPeligroso = sumaPeligroso / cuentaPeligroso

    print("Promedio ICA Positivo por Comuna: ", promedioPositivo)
    print("Promedio ICA Moderado por Comuna: ", promedioModerado)
    print("Promedio ICA Peligroso por Comuna: ", promedioPeligroso)
    
    promedioPositivoDF = promedioPositivo.reset_index().rename(columns={'ICA':'Promedio ICA Positivo'})
    promedioModeradoDF = promedioModerado.reset_index().rename(columns={'ICA':'Promedio ICA Moderado'})
    promedioPeligrosoDF = promedioPeligroso.reset_index().rename(columns={'ICA':'Promedio ICA Peligroso'})
    
    crearTablaHTML(promedioPositivoDF, "promedioICA_Positivo")
    crearTablaHTML(promedioModeradoDF, "promedioICA_Moderado")
    crearTablaHTML(promedioPeligrosoDF, "promedioICA_Peligroso")

construirDataFrameCalidadAire()