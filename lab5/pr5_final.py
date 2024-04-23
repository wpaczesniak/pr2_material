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

def ReadFileWithNames(name: str) -> (bool, list):
	opened = False
	namesOfTowns = []
	try:
		f = open(name, encoding="utf-8")
	except FileNotFoundError:
		print(f"File not found: {name}")
	else:
		opened = True
		f.readline()  # Skip header
		for line in f:
			splittedLine = line.split(";")
			j = splittedLine[1].strip()
			namesOfTowns.append(j)
		f.close()
	return opened, namesOfTowns

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

def calculateMeanPopulation(municipality):
	# calculate the mean population of a municipality from 1998 to 2022
	sumPoblacion = 0
	for i in range(1998, 2023):
		sumPoblacion += municipality.GetPoblacion(i)
	return sumPoblacion / 25

def main():
	filename = "EvolMunicipios2022.csv"
	# filename = "EvolMunicipios_small.csv"
	file_opened, municipality_list = ReadFile(filename)
	
	if not file_opened:
		print(f"Failed to open file: {filename}")
		return
	
	
	abb = ABB()
	
	# Reading file with municipalities names
	NamesFilename = "MunicipiosVariasProv.csv"
	file_opened, namesOfTowns = ReadFileWithNames(NamesFilename)

	if not file_opened:
		print(f"Failed to open file: {NamesFilename}")
		return

	# Inserting municipalities into the ABB
	for municipio in municipality_list:
		abb.Insertar(municipio.GetNombre(), municipio)
	
	highPopulationTowns = []

	# Searching for municipalities with mean population >= 50000
	for townName in namesOfTowns:
		searchResult = abb.Buscar(townName)
		if (searchResult[0] and calculateMeanPopulation(searchResult[1]) >= 50000):
			highPopulationTowns.append(searchResult[1].GetNombre())

	# Displaying the results
	print("--------------------------")
	print("INCREMENTO DE POBLACION")
	print("--------------------------")
	print("- Municipios buscados:" , len(namesOfTowns))
	print("- Municipios con población media >= 50000:" , len(highPopulationTowns))
	print("- Nombres:")
	print(highPopulationTowns)

if __name__ == '__main__':
	main()