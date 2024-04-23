from pr1_municipio import *
from pr1_algoritmos import *

def ConvertirLinea(s:str)->Municipio:
    """
    Convertir una linea de texto csv en un registro Municipio

    Parameters
    ----------
    s : str
        linea de texto a procesar.

    Returns
    -------
    Municipio
        El municipio con los datos contenidos en s.

    """
    s = s.rstrip("\n") #elimina \n si lo tuviera
    l = list()
    l = s.split(";")
    m = Municipio()
    #seleccionar los datos relevantes de toda la linea
    m = GenerarMunicipio(l[0], l[1], l[2:])
    return m
    
def LeerFichero(nom: str)->(bool,list #de Municipio
                            ):
    """
    Leer el archivo con los datos de los municipios españoles

    Parameters
    ----------
    nom : str
        nombre del archivo.

    Returns
    -------
    (bool,list)
        abierto para lectura correctamente = True/False
        lista de municipios leidos, vacía si no abierto

    """
    abierto = bool()
    pueblos = list()
    try:
        f = open(nom,encoding="utf-8")
    except:
        abierto = False
    else:
        abierto = True
        #Leer cabecera y no hacer nada con ella
        f.readline()
        #Leer las restantes lineas y convertirlas en municipios
        for linea in f:
            j = ConvertirLinea(linea)
            pueblos.append(j)
        f.close()
    return abierto,pueblos

def read_codes_from_file(filename: str) -> list:
    codes = []  # list of codes
    # read from file
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            next(file)  # Skip the first line
            for line in file:
                code = line.split(';')[0]  # split the line by ';' and take the first element
                codes.append(code)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    return codes

def main():
    # Load Spanish municipalities data
    archivo_csv = "EvolMunicipios2022.csv"
    abierto, municipios_espana = LeerFichero(archivo_csv)

    if not abierto: # chceck if file is open
        print(f"Could not open file {archivo_csv}")
        return
    
    # Read codes of municipalities in the Comunidad Valenciana
    identificadores_cv = read_codes_from_file("MunicipiosCV.csv")
    # Initialize counters
    total_municipalities = len(identificadores_cv)
    increasing_population = 0   # how many cites have increased their population
    for ine in identificadores_cv:
        # Search for municipality in the list of Spanish municipalities
		
        posicion, _ = BusquedaSecuencial(municipios_espana, ine)
        
        # Check if municipality is found and if its population has increased in the last 10 years
        if posicion != -1:
            municipio_cv = municipios_espana[posicion]
            # convert string to int
            if int(municipio_cv.poblacion[0]) > int(municipio_cv.poblacion[10]):
                increasing_population += 1
    # Calculate percentage
    percentage = (increasing_population / total_municipalities) * 100
    # Display results
    print("Municipalities sought:", total_municipalities)
    print("Increasing population:", increasing_population)
    print("Percentage:", "{:.2f}%".format(percentage))
    print()
    print("Average number of steps:")


    for algoritmo in [BusquedaSecuencial, BusquedaSecuencialParada, 
                          BusquedaSecuencialCentinela, BusquedaBinaria]:
        steps = 0   # counter of steps of every algorithm
        count = 0   # cicites counter
        for ine in identificadores_cv:
            posicion, pasos = algoritmo(municipios_espana, ine)
            steps += pasos  # add pasos to the steps
            count+=1    # increment counter
        stepsAvg = steps / count    # calculate average steps of every algorithm
        # display results
        print(algoritmo.__name__, " - ", round(stepsAvg, 2))   


    
if __name__ == '__main__':
    main()