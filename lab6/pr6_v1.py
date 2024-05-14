from pr2_municipio import Municipio

def load_municipios(filename:str)->(bool, list):
	opened = False
	municipios = {}
	try:
		f = open(filename, encoding="utf-8")
	except FileNotFoundError:
		print(f"File not found: {filename}")
	else:
		opened = True
		with open(filename, 'r', encoding='utf-8') as file:
			lines = file.readlines()
			for line in lines[1:]:  # Skip the header line
				municipio = Municipio()
				municipio.SetLinea(line)
				municipios[municipio.GetCodine()] = municipio
		f.close()
	return opened, municipios

def load_provinces(filename:str)->(bool, list):
	opened = False
	provinces = {}
	try:
		f = open(filename, encoding="utf-8")
	except FileNotFoundError:
		print(f"File not found: {filename}")
	else:
		opened = True
		with open(filename, 'r', encoding='utf-8') as file:
			lines = file.readlines()
			for line in lines[1:]:
				line = line.rstrip("\n")
				provinces[line.split(";")[0]] = line.split(";")[1]
		f.close()
		return opened, provinces

def main():
	# filename = "EvolMunicipios2022.csv"
	filename = "EvolMunicipios_small.csv"
	file_opened, municipios = load_municipios(filename)



	if not file_opened:
		print(f"File {filename} could not be opened.")
		return
	
	# for codine, municipio in municipios.items():
	# 	print(f"{codine}: {municipio.GetNombre()}")
	# 	print(f"{municipio}")

	provinces_filename = "provincias.csv"
	file_opened, provinces = load_provinces(provinces_filename)
	if not file_opened:
		print(f"File {filename} could not be opened.")
		return
	
	# print(provinces)
 
	province_code = input("Enter the province code: ")



	province_name = provinces.get(province_code, "Unknown")
	print(f"Province: {province_name}")
	for codine, municipio in municipios.items():
		if codine.startswith(province_code):
			print(municipio.GetNombre())
			print(municipio.GetPoblacion(2022))

	return

if __name__ == '__main__':
	main()