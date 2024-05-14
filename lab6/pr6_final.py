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
	filename = "EvolMunicipios2022.csv"
	# filename = "EvolMunicipios_small.csv"
	file_opened, municipios = load_municipios(filename)

	if not file_opened:
		print(f"File {filename} could not be opened.")
		return

	provinces_filename = "provincias.csv"
	file_opened, provinces = load_provinces(provinces_filename)
	if not file_opened:
		print(f"File {filename} could not be opened.")
		return
 
	valencian_codes = ["03", "12", "46"]
	dict_valencian_communities = {}

	for codine, municipio in municipios.items():
		if codine[:2] in valencian_codes:
			dict_valencian_communities[codine] = municipio

	total_population_2017 = 0
	total_population_2022 = 0
	analised_municipios = 0

	for codine, municipio in dict_valencian_communities.items():
		total_population_2017 += municipio.GetPoblacion(2017)
		total_population_2022 += municipio.GetPoblacion(2022)
		analised_municipios += 1


	diff_population = total_population_2022 - total_population_2017
	precentage_population = (diff_population / total_population_2017) * 100

	# print results

	print("--------------------------")
	print("INCREMENTO DE POBLACION")
	print("--------------------------")
	print(f"- Municipios analizados: {analised_municipios}")
	print("- Provincias:")
	for codine in valencian_codes:
		print(f"\t{provinces.get(codine, 'Unknown')}")
	print(f"- Población 2022: {total_population_2022}")
	print(f"- Población 2017: {total_population_2017}")
	print(f"- Diferencia: {diff_population} {precentage_population:.2f} %")
	return

if __name__ == '__main__':
	main()