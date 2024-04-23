from pr2_municipio import *
from clase_ABB import *

def ConvertLine(s: str) -> Municipio:
    """
    Converts a CSV text line into a Municipio object.
    """
    m = Municipio()
    # Sets data for the Municipio object using the SetLinea method
    # The SetLinea method takes the entire text line as a single argument
    m.SetLinea(s)  # Passing the entire text line directly to the SetLinea method
    return m

def ReadFile(name: str) -> (bool, list):
    """
    Reads a file with data on Spanish municipalities.

    Parameters
    ----------
    name : str
        The name of the file to read.

    Returns
    -------
    (bool, list)
        True/False, depending on whether the file was successfully opened.
        List of Municipio objects read from the file.
    """
    opened = False
    towns = []
    try:
        f = open(name, encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found: {name}")
    else:
        opened = True
        f.readline()  # Skip header
        for line in f:
            j = ConvertLine(line)
            towns.append(j)
        f.close()
    return opened, towns

def MinorCodine(a: Municipio, b: Municipio) -> bool:
    """
    Compares the INE codes of two municipalities (Municipio).

    Parameters
    ----------
    a : Municipio
        The first municipality to compare.
    b : Municipio
        The second municipality to compare.

    Returns
    -------
    bool
        True, if the INE code of municipality a is less than the INE code of municipality b, otherwise False.
    """
    return a.GetCodine() < b.GetCodine()

def MinorName(a: Municipio, b: Municipio) -> bool:
    """
    Compares the names of two municipalities (Municipio).

    Parameters
    ----------
    a : Municipio
        The first municipality to compare.
    b : Municipio
        The second municipality to compare.

    Returns
    -------
    bool
        True, if the name of municipality a is alphabetically less than the name of municipality b, otherwise False.
    """
    return a.GetNombre() < b.GetNombre()

def SmallerInhabitants(a: Municipio, b: Municipio) -> bool:
    """
    Compares the population in 2022 of two municipalities (Municipio).

    Parameters
    ----------
    a : Municipio
        The first municipality to compare.
    b : Municipio
        The second municipality to compare.

    Returns
    -------
    bool
        True, if the population of municipality a in 2022 is less than the population of municipality b, otherwise False.
    """
    return a.GetPoblacion(2022) < b.GetPoblacion(2022)

def search_and_display(abb, name):
    """
    Wyszukuje i wyświetla dane dla podanej nazwy gminy.
    """
    found, municipio = abb.Buscar(name)
    if found:
        print(f"Buscar: {name}")
        print(municipio)  # Asumimos que Municipio tiene un método __str__ adecuado
    else:
        print(f"Buscar: {name}")
        print("No encontrado\n")

def main():
    # filename = "EvolMunicipios2022.csv"
    filename = "EvolMunicipios_small.csv"
    file_opened, municipality_list = ReadFile(filename)
    
    if not file_opened:
        print(f"Failed to open file: {filename}")
        return
    
    
    abb = ABB()
    

    for municipio in municipality_list:
        abb.Insertar(municipio.GetNombre(), municipio)
    

    print(" ABB TREE :")
    abb.ImprimirArbol()
    
    print("DUPA_DUPA_DUPA_DUPA_DUPA_DUPA_DUPA")

    cities_to_search = ["Lugo", "Albatera", "Burjassot", "Benidorm", "Bilbao"]
    

    for city in cities_to_search:
        search_and_display(abb, city)
    # for municipio in municipality_list:
    #     print(f"Kod INE: {municipio.GetCodine()}, Nazwa: {municipio.GetNombre()}, Populacja 2022: {municipio.GetPoblacion(2022)}")

    # criteria = [
    #     (MinorCodine, "Code"),
    #     (MinorName, "Name"),
    #     (SmallerInhabitants, "Population in 2022")
    # ]
    # summary_steps = {criterion_name: {"Selection Sort": 0, "Quick Sort": 0, "Times faster QS": 0} for _, criterion_name in criteria}

    # for criterion, criterion_name in criteria:
    #     print(f"\nSorting by: {criterion_name}")
        
    #     selection_list = municipality_list.copy()
    #     quicksort_list = municipality_list.copy()
        
    #     selection_steps = OrdSeleccion(selection_list, criterion)
    #     quicksort_steps = OrdQuicksort(quicksort_list, criterion)
        
    #     print("Selection Sort:")
    #     print(f"Number of steps: {selection_steps}")
    #     for municipio in selection_list:
    #         print(municipio)
        
    #     print("\nQuick Sort:")
    #     print(f"Number of steps: {quicksort_steps}")
    #     for municipio in quicksort_list:
    #         print(municipio)
        
    #     summary_steps[criterion_name]["Selection Sort"] = selection_steps
    #     summary_steps[criterion_name]["Quick Sort"] = quicksort_steps
    #     summary_steps[criterion_name]["Times faster QS"] = round(selection_steps / quicksort_steps, 2) if quicksort_steps != 0 else "n/a"

    # # Displaying the summary
    # print("\nSummary of results (steps performed by algorithms):")
    # print("Criterion", "Selection Sort", "Quick Sort", "Times faster QS", sep="\t")
    # for criterion_name in criteria:
    #     crit = criterion_name[1]
    #     print(f"{crit}", summary_steps[crit]["Selection Sort"], summary_steps[crit]["Quick Sort"], summary_steps[crit]["Times faster QS"], sep="\t\t\t")       

if __name__ == '__main__':
    main()