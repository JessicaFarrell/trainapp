import dijkstra
import graphviz

## Model class functionally makes the graph using the data given, the
## graph includes the times between stations, differing lines and open
## / closed status of the stations
## this graph is utilised by graphviz to make a gif

class Model:
    
## Function sets up information for the graph      
    def __init__(self, stations, connections, lines):
        self.stations = stations
        self.connections = connections
        self.lines = lines
        self.line_colours = {}
        self.connections_with_line_names = {}
        self.graph = self.make_graph()
        self.graphviz_graph = self.make_graphvis_graph()
        
        
## Function makes the graph, using self.connections and self.stations
## the graph is of the form {"watford" : "westferry" : 2}    
    def make_graph(self):
        ## empty graph
        rail_connections = {}
        for connection in self.connections:
            station_from_name = self.get_station_name_by_id(connection["station1"])
            station_to_name = self.get_station_name_by_id(connection["station2"])
            travel_time = int(connection["time"])
            if not self.is_station_closed(station_from_name) or self.is_station_closed(station_to_name):
                print(station_from_name, " OPEN")
                if station_from_name not in rail_connections:
                    rail_connections[station_from_name] = {}
                if station_to_name not in rail_connections:
                    rail_connections[station_to_name] = {}
                if station_from_name not in self.line_colours:
                    self.line_colours[station_from_name] = {}
                if station_to_name not in self.line_colours:
                    self.line_colours[station_to_name] = {}
                if station_to_name not in self.connections_with_line_names:
                    self.connections_with_line_names[station_to_name] = {}
                if station_from_name not in self.connections_with_line_names:
                    self.connections_with_line_names[station_from_name] = {}
                rail_connections[station_from_name][station_to_name] = travel_time
                rail_connections[station_to_name][station_from_name] = travel_time
                self.line_colours[station_from_name][station_to_name] = self.get_line_colour(connection["line_id"])
                self.line_colours[station_to_name][station_from_name] = self.get_line_colour(connection["line_id"])
                self.connections_with_line_names[station_to_name][station_from_name] = self.get_line_name(connection["line_id"])
                self.connections_with_line_names[station_from_name][station_to_name] = self.get_line_name(connection["line_id"])
            else:
                print(station_from_name, " CLOSED")
        return rail_connections

## Function gets the line name from the line ID    
    def get_line_name(self, line_id):
        for line in self.lines:
            if line["line_id"] == line_id:
                return line["name"]

## Function makes the visual graph with weights and colours using self.graph
## and self.line colours    
    def make_graphvis_graph(self):
        d = graphviz.Digraph()
        
        #d.graph_attr.update(size="100,100")
        ## make graphviz of the connections
        for station1, station2AndDistance in self.graph.items():
            for station2, distance in station2AndDistance.items():
                d.edge(station1, station2, weight="1.2", label=str(distance), color="#" + (self.line_colours[station1][station2]))
        d.render("LondonNetwork", format='gif', view=False)
        return d

## Function retrieves all station data from a given station name     
    def get_station(self, name):
        for station in self.stations:
            if station.name == name:
                return station
            else:
                print("Sorry, we could not find station: ", name, ". Please try another station.")
 
## Function finds line colour using line ID
    def get_line_colour(self, line_id):
        for line in self.lines:
            if line["line_id"] == line_id:
                return line["colour"]

## Function retieves data graph
    def get_graph(self):
        return self.graph
    

## Function uses dijkstras to find the shortest path between a start and end 
## point. See Dijkstra.py for more information
    def find_shortest_path(self, start_destination, end_destination, nodes):
        print("From: ", start_destination, " To: ", end_destination)
        if start_destination != end_destination:
        ### DO DIJKSTRA'S HERE...
            shortest_path, shortest_distance = dijkstra.dijkstra([start_destination, end_destination], self.graph, nodes)
            return shortest_path, shortest_distance
        else:
            print("Your start destination is the same as your end destination. Please try again")

## Function determines opne/closed status of station    
    def is_station_closed(self, name):
        for station in self.stations:
            if station.name == name:
                if station.rail == '0':
                    return False
                else:
                    return True

## Function gets name of station from station_id
    def get_station_name_by_id(self, identifier):
        if type(identifier) is not str:
            identifier = str(identifier)
        for station in self.stations:
            if station.id == identifier:
                return station.name
        

## Function gets the station id from station name 
    def get_station_id_by_name(self, name):
        if type(name) is not str:
            name = str(name)
        for station in self.stations:
            if station.name == name:
                return station.id