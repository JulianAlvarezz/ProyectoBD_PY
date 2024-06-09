#Funcion generica para convertir un DF en HTML
def crearGraficoHTML(dataFrame,nombreGrafico):
    
    #convertir el DF en HTML
    archivoHTML=dataFrame.to_html()
    
    #abrimos el archivo HTML en una ruta especifica
    with open(f"./tables/{nombreGrafico}.html","w") as archivo:
    
        #escribimos la informacion en el archivo
        archivo.write('''
            
                <html>
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                </head>
                <body>
            ''')
        archivo.write(archivoHTML)
        archivo.write(
            '''
            </body>
            </html>
            '''
        )