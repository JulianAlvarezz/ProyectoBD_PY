import pandas as pd

from data.generators.pluviometrico import generarDatosPluviometrico
from helpers.generarTabla import crearTablaHTML

def construirDataFramepluviometrico():
    
    datosPluviometrico=generarDatosPluviometrico()
    pluviometricoDF=pd.DataFrame(datosPluviometrico, columns=(['municipio', 'lluviaXhora', 'lluviaXsemana', 'lluviaXmes', 'precipitacion', 'id']))
    
    print(pluviometricoDF)
    crearTablaHTML(pluviometricoDF,"calidadPluviometrico")
    
construirDataFramepluviometrico()