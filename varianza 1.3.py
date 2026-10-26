
# funcion de varianza de datos no agrupados

def varianza(datos:list):
    cantidad_de_dato = len(datos)
    varianza_datos = sum(datos) / cantidad_de_dato 

    print(f"varianza:{varianza_datos}")

    print("|x|x-q|x-q)^2|")
    for dato in range(0,cantidad_de_dato):
        datos_tabla1= datos[dato] - varianza_datos

        datos_tabla2= (datos[dato] - varianza_datos) **2 # esta llo multiplica a la potencia de 2

        print(f"|{datos[dato]}|{datos_tabla1}|{datos_tabla2}|")

data = [15,5,8,10,7]

varianza(data)