import csv

from grafo import Grafo

def read_cities(filename):
	cities = []
	with open(filename, 'r', encoding='utf-8') as file:
		for line in file:
			city = line.strip()
			if city:  # Check if the line is not empty
				cities.append(city)
	return cities

def read_arcs(filename, graph):
	with open(filename, 'r', newline='', encoding='utf-8') as file:
		reader = csv.reader(file, delimiter=';')
		next(reader)
		for row in reader:
			origin = row[0]
			destination = row[1]
			weight = row[2]

			originId = graph.IndiceNodo(origin)
			destinationId = graph.IndiceNodo(destination)
			graph.AsignarArco(originId, destinationId, int(weight))
	return

def main():
	citiesFilename = "ciudades.dat"
	cities = read_cities(citiesFilename)
	# print(cities)
	g = Grafo(len(cities))
	for i in range(len(cities)):
		g.AsignarInfoNodo(i, cities[i])

	# print(g.ImprimirGrafo())
	arcFilename = "arcos_ciudades.csv"
	read_arcs(arcFilename, g)
	print(g.ImprimirGrafo())
	return

if __name__ == '__main__':
	main()