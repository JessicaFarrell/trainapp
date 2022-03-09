import file_reader
from station import Station
from view import Gui
from controller import controller
from model import Model
from view import *


## Reading in files given 
connections_list = file_reader.CSV_reader("londonconnections.csv")
lines_list = file_reader.CSV_reader("londonlines.csv")
stations_list = file_reader.CSV_reader("londonstations.csv")


## This creates each station using the below attributes and puts them 
## into a list
stations = []
for station_info in stations_list:
    new_station = Station(station_info['id'],
                          station_info['latitude'], 
                          station_info['longitude'],
                          station_info['name'],
                          station_info['display_name'],
                          station_info['zone'],
                          station_info['total_lines'],
                          station_info['rail']
                          )
                          
    stations.append(new_station)

## this creates a model class with the information given
## see model.py for class defintion

model = Model(stations, connections_list, lines_list)
graph = model.get_graph()






## get all of the starting points and destinations to add to the combo boxes.
from_stations = []
to_stations = []
for station1, station2AndDistance in graph.items():
    for station2, distance in station2AndDistance.items():
        if station1 not in from_stations:
            from_stations.append(station1)
            from_stations = sorted(from_stations)
        if station2 not in to_stations:
            to_stations.append(station2)
            to_stations = sorted(to_stations)

## this creates a controller class
controller = controller(from_stations, to_stations, model)



