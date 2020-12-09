from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
import subprocess

class MapWindow(QWidget):
    #Main Window
    def __init__(self, *args, **kwargs):
        super(MapWindow, self).__init__(*args, **kwargs)
        #Estructura de la ventana principal
        self.x=400
        self.y=200
        self.map=("","")

        self.setWindowIcon(QIcon('img\icon.png'))
        self.label=QLabel(self)
        self.label.setText("Mapa escogido: \""+self.map[0]+"\"")
        self.label.setGeometry(10,self.y-30,self.x,30)
        
        self.setWindowTitle("DuckieGUI")
        self.setFixedSize(self.x, self.y)

        #Definimos los botones para la ejecucion de la simulacion
        #button_map: Ejecuta la funcion para la seleccion del mapa de simulacion
        self.button_map = QPushButton(self, text="Escoger Mapa")
        self.button_map.setGeometry(int(self.x/2-55),int(self.y/2-50),110,30)
        self.button_map.clicked.connect(self.map_select)

    def map_select(self):#Esta funcion se encarga de selecionar el mapa de la simulacion
        self.map= QFileDialog.getOpenFileName(self, "Select Map","", "Archivos soportados (*.yaml)")
        self.label.setText("Mapa escogido: \""+self.map[0]+"\"")
 




