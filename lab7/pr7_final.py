import csv

from grafo import Grafo

def read_bus_stops(filename):
	paradas = []
	with open(filename, 'r', encoding='utf-8') as file:
		for line in file:
			parada = line.strip()
			if parada:  # Check if the line is not empty
				paradas.append(parada)
	return paradas

def create_bus_routes(paradas, filename):
	graph = Grafo(len(paradas))
	for i in range(len(paradas)):
		graph.AsignarInfoNodo(i, paradas[i])

	with open(filename, 'r', newline='', encoding='utf-8') as file:
		reader = csv.reader(file, delimiter=';')
		next(reader)
		for row in reader:
			vertice0 = row[1]
			vertice1 = row[2]

			vertice0Id = graph.IndiceNodo(vertice0)
			vertice1Id = graph.IndiceNodo(vertice1)
			graph.AsignarArco(vertice0Id, vertice1Id, 1)
			graph.AsignarArco(vertice1Id, vertice0Id, 1)
	return graph

def possible_destinations(graph, destination) -> list:
	visited = set()
	dist = graph.BFS(destination, visited)
	return dist

def show_route_info(possibleOriginsDistList, graph):
	for i in range(len(possibleOriginsDistList)):
		if possibleOriginsDistList[i] != -1 and possibleOriginsDistList[i] != 0:
			print(f"{graph.InfoNodo(i)} --> escalas = {possibleOriginsDistList[i]-1}")
	return


def main():
	paradasFilename = "paradas_buses_cv.dat"
	paradas = read_bus_stops(paradasFilename)
	routesFilename = "rutas_buses_cv.csv"
	g = create_bus_routes(paradas, routesFilename)

	destination = input("type the destination: ")
	destinationId = g.IndiceNodo(destination)
	originsIds = possible_destinations(g, destinationId)
	show_route_info(originsIds, g)
	return

if __name__ == '__main__':
	main()