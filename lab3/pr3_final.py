import csv

from pr3_aeropuerto import Aeropuerto



def ReadFile(name: str) -> (bool, list):
	"""
	Reads a file with data on Airports.

	Parameters
	----------
	name : str
		The name of the file to read.

	Returns
	-------
	(bool, list)
		True/False, depending on whether the file was successfully opened.
		List of Strings containing information about airports read from the file.
	"""
	opened = False
	airports = []
	try:
		f = open(name, encoding="utf-8")
	except FileNotFoundError:
		print(f"File not found: {name}")
	else:
		opened = True
		f.readline()  # Skip header
		for line in f:
			airports.append(line[:-1])
		f.close()
	return opened, airports

def AsignarValores(a:Aeropuerto,s:str):
	"""
	Asignar los datos de una cadena s al aeropuerto a

	Parameters
	----------
	a : Aeropuerto
	s : str
		cadena con los campos separados por ";"

	Returns
	-------
	None.

	"""
	datos = s.split(";")
	tmp = Aeropuerto()
	try:
		tmp.SetIATA(datos[4])
		tmp.SetICAO(datos[5])
		tmp.SetDST(datos[10])
	except RuntimeError as e:
		raise e
	else:
		a.SetID(int(datos[0]))
		a.SetNombre(datos[1])
		a.SetCiudad(datos[2])
		a.SetPais(datos[3])
		a.SetIATA(datos[4])
		a.SetICAO(datos[5])
		a.SetLatitud(float(datos[6]))
		a.SetLongitud(float(datos[7]))
		a.SetAltitud(float(datos[8]))
		a.SetTimezone(float(datos[9]))
		a.SetDST(datos[10])
	return
	
def saveAirportsToFile(airports_in_country: list, country: str):
	with open('country_' + country + '.csv', 'w', newline='', encoding='utf-8') as file:
		writer = csv.writer(file)
		# Write the headers to the CSV file
		writer.writerow(["ID;Nombre;Ciudad;Pais;IATA;ICAO;Latitud;Longitud;Altitud;Timezone;DST"])
		# Write the airports to the CSV file
		for airport in airports_in_country:
			writer.writerow([airport.__str__()])

def main():
	# read the file
	filename = "aeropuertos.csv"
	file_opened, string_airport_list = ReadFile(filename)

	if not file_opened:
		print(f"Failed to open file: {filename}")
		return
	
	# create a list of airports
	airports = []

	for airport in string_airport_list:
		# create an airport object
		a = Aeropuerto()
		# assign the values from the string to the airport object
		try:
			AsignarValores(a,airport)
		except RuntimeError as e:
			print(f"Error: {e}")
		else:
			# add the airport object to the list
			airports.append(a)

	# input a country
	while True:
		country = input("Please enter a country: ")
		if country:
			break
		else:
			print("You entered an empty string. Please provide a valid country name.")

	# create a list of airports in the provided country
	airports_in_country = [airport for airport in airports if airport.GetPais() == country]

	# save to csv file
	saveAirportsToFile(airports_in_country, country)

	return
	
if __name__ == '__main__':
	main()