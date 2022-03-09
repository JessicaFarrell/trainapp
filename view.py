from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

## Gui class using TKinter module
##
## Gui for selecting start and destinations 
## and calculating shortest route to display

## displays a graph representation of the stations, 
## defines the layout and look of the GUI
class Gui(Frame):
## this function sets up the appearance of the GUI, such as the buttons,
# labels and drop downs
    def __init__(self, master=None):
        
        Frame.__init__(self, master)
        #display of app
        self.master.title("TrainApp")
        
        self.canvas_frame = Frame(self.master, width=400, height=300)
        self.hbar = Scrollbar(self.canvas_frame, orient=HORIZONTAL)
        self.vbar = Scrollbar(self.canvas_frame, orient=VERTICAL)


        #add some labels
        self.from_station_label = ttk.Label(self.master, text="Station From:")
        self.to_station_label = ttk.Label(self.master, text="Station To:")
        
        self.from_station_label.pack() #grid(column = 0, row = 0)
        # Add a combobox widget
        self.station_from_combo = ttk.Combobox(self.master)
        #combo['values'] = (1,2,3,4,5, "Text")
        self.station_from_combo.pack() #.grid(column = 1, row = 0)
        
        self.to_station_label.pack() #grid(column=2, row = 0)
        self.station_to_combo = ttk.Combobox(self.master)
        
        #combo2['values'] = (1,2,3,4,5, "Text")
        self.station_to_combo.pack() #grid(column = 3, row = 0)
        self.find_route_button = ttk.Button(self.master)
        self.find_route_button.pack() #grid(column = 4, row = 0)
        
        self.route_text_frame = Frame(self.master)
        self.route_text_box = Text(self.route_text_frame, height =3, width =50)
        self.route_text_scroll_bar = Scrollbar(self.route_text_frame)
        self.route_text_scroll_bar.config(command=self.route_text_box.yview)
        self.route_text_box.config(yscrollcommand=self.route_text_scroll_bar.set)
        self.route_text_box.configure(state='disabled')
        self.route_text_scroll_bar.pack(side=RIGHT, fill=BOTH)
        self.route_text_box.pack()
        self.route_text_frame.pack(expand=True)
        image_path = os.path.join(os.path.abspath(os.getcwd()), "LondonNetwork.gif")

        self.graph_image = ImageTk.PhotoImage(Image.open(image_path))
        self.canvas = Canvas(self.canvas_frame, xscrollcommand=self.hbar.set,
                             yscrollcommand=self.vbar.set,
                             width=300,
                             height=200,
                             bg='white')
        self.canvas.create_image(self.graph_image.width(),self.graph_image.height(), image=self.graph_image)
        self.hbar["command"] = self.canvas.xview
        self.vbar["command"] = self.canvas.yview
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.vbar.pack(side=RIGHT, fill=Y)
        self.hbar.pack(side=BOTTOM, fill=X)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)#grid(column=0, row=1)
        self.canvas_frame.pack(expand=True, fill=BOTH)
      
        
        
        
## This sets the text in the textbox
    def set_route_text_box_text(self, text):
        #self.route_text_box["text"] = text
        self.route_text_box.configure(state='normal')
        self.route_text_box.delete(0.0,END)
        self.route_text_box.insert(0.0, text)
        self.route_text_box.configure(state='disabled')

## This sets the to and from station names for combo boxes
    def set_station_names_combo(self, from_stations, to_stations):
        self.station_from_combo["values"] = from_stations
        self.station_to_combo["values"] = to_stations

## This sets the function to call when the find route button is pressed    
    def set_button_function(self, function):
        self.find_route_button["command"] = function

## This sets 'find route' text on the button
    def set_button_text(self, text):
        self.find_route_button["text"] = text

## This gets the text from the combo box       
    def get_from_station_name(self):
        return self.station_from_combo.get()

## This gets the text from the combo box    
    def get_to_station_name(self):
        return self.station_to_combo.get()

## This starts the GUI
    def start_main_loop(self):
        self.mainloop()
          




