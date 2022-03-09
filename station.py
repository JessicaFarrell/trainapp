## Station class 
##
## Describes and defines a train station
## using station_id,latitude,longitude,name,display_name,zone,total_lines,rail

class Station:
    
    def __init__(self, station_id,latitude,longitude,name,display_name,zone,total_lines,rail):
        self.id = station_id
        self.location = (latitude, longitude)
        self.name = name
        self.display_name = display_name
        self.zone = zone
        self.total_lines = total_lines
        self.rail = rail

    
