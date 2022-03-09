from view import Gui

## controller class communicates between the model and the view
## this allows the GUI to function with the information from
## the model


class controller:
## This function sets up model and view, and starts GUI    
    def __init__(self, from_stations, to_stations, model):
        self.from_stations = from_stations
        self.to_stations = to_stations
        self.Gui = Gui()
        self.model = model
        self.Gui.set_station_names_combo(from_stations, to_stations)
        self.Gui.set_button_text("Find Route")
        self.Gui.set_button_function(self.find_route_button_pressed)
        self.Gui.start_main_loop()
    
## Function that is called when 'find route' button is pressed   
    def find_route_button_pressed(self):
        
        print("Start Destintation: ", self.Gui.get_from_station_name())
        print("Final Destination: ", self.Gui.get_to_station_name())
        start_destination = self.Gui.get_from_station_name()
        end_destination = self.Gui.get_to_station_name()
        nodes = sorted(self.from_stations + self.to_stations)
        shortest_path, shortest_distance = self.model.find_shortest_path(start_destination, end_destination, nodes)
        print("Shortest Path: ", shortest_path)
        print("Shortest Distance: ", shortest_distance)
        
        for i in range(0, len(shortest_path) -1):
            from_station = shortest_path[i]
            to_station = shortest_path[i+1]
            shortest_path[i] = shortest_path[i] + " (" + self.model.connections_with_line_names[from_station][to_station] + ") "
            
            
        ## Checks if route is found, and relays appropriate message to GUI text box   
        if shortest_distance != -1:
            shortest_path_text = ", ".join(shortest_path)
            shortest_distance_text = "Estimated Time (minutes): " + str(shortest_distance)
            self.Gui.set_route_text_box_text(shortest_path_text + " // " + shortest_distance_text)
        else:
            apology_message = "Sorry, I could not find a route from " + \
                                start_destination + " -> " + end_destination
            self.Gui.set_route_text_box_text(apology_message)