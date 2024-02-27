from pr2_municipio import *
from pr2_algoritmos import *

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



def SmallestIncrease(a: Municipio, b: Municipio) -> bool: # function to compare population of two municipalities
    return a.GetPoblacion(2022) - a.GetPoblacion(2012) < b.GetPoblacion(2022) - b.GetPoblacion(2012)

def main():
    # File to read
    filename = "EvolMunicipios2022.csv"
    file_opened, municipality_list = ReadFile(filename)
    
    if not file_opened:
        print(f"Failed to open file: {filename}")
        return

	# dictionary to store the summary of steps
    summary_steps = {"Selection Sort": 0, "Quick Sort": 0, "Times faster QS": 0}

    print(f"\nSorting by: Increase in population from 2012 to 2022")
    
	# copy the list to avoid modifying the original list
    selection_list = municipality_list.copy()
    quicksort_list = municipality_list.copy()
    
	# sort the lists
    selection_steps = OrdSeleccion(selection_list, SmallestIncrease)
    quicksort_steps = OrdQuicksort(quicksort_list, SmallestIncrease)
    
    print("Selection Sort:")
    print(f"Number of steps: {selection_steps}")
    # number of cities to print
    number_of_printed_cities = 10
    # creating a list of the top ten cities with the highest increase in population in order to print them
    selection_list_top_ten = selection_list[-number_of_printed_cities:]
    # printing the top ten cities
    for index in range(number_of_printed_cities):
        # the list is sorted in ascending order, so we print the cities in reverse order
        # we have to subtract the index from the number of printed cities to get the correct index
        # we also have to subtract 1 from the index to get the correct index
        name = selection_list_top_ten[number_of_printed_cities - index - 1].GetNombre()
        number = selection_list_top_ten[number_of_printed_cities - index - 1].GetCodine()
        increase = selection_list_top_ten[number_of_printed_cities - index - 1].GetPoblacion(2022) - selection_list_top_ten[number_of_printed_cities - index - 1].GetPoblacion(2012)
        print(number, name, increase)
    
    print("\nQuick Sort:")
    print(f"Number of steps: {quicksort_steps}")
    # creating a list of the top ten cities with the highest increase in population in order to print them
    qiucksort_list_top_ten = quicksort_list[-number_of_printed_cities:]
    # printing the top ten cities
    for index in range(number_of_printed_cities):
        # the list is sorted in ascending order, so we print the cities in reverse order
        # we have to subtract the index from the number of printed cities to get the correct index
        # we also have to subtract 1 from the index to get the correct index
        name = qiucksort_list_top_ten[number_of_printed_cities - index - 1].GetNombre()
        number = qiucksort_list_top_ten[number_of_printed_cities - index - 1].GetCodine()
        increase = qiucksort_list_top_ten[number_of_printed_cities - index - 1].GetPoblacion(2022) - qiucksort_list_top_ten[number_of_printed_cities - index - 1].GetPoblacion(2012)
        print(number, name, increase)
    
	# save the summary of steps in a dictionary
    summary_steps["Selection Sort"] = selection_steps
    summary_steps["Quick Sort"] = quicksort_steps
    summary_steps["Times faster QS"] = round(selection_steps / quicksort_steps, 2) if quicksort_steps != 0 else "n/a"

    # Displaying the summary
    print("\nSummary of results (steps performed by algorithms):")
    print("Criterion", "Selection Sort", "Quick Sort", "Times faster QS", sep="\t")

    print(summary_steps["Selection Sort"], summary_steps["Quick Sort"], summary_steps["Times faster QS"], sep="\t\t\t")     

if __name__ == '__main__':
    main()
