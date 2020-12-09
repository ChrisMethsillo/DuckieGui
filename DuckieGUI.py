from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

from lib.map_chooser import *
from lib.speed_chooser import *

class MainWindow(QMainWindow):
    #Main Window
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.mapchooser=MapWindow()
        self.speedchooser=SpeedWindow()
        
        #Estructura de la ventana principal
        self.x=200
        self.y=200

        self.setWindowIcon(QIcon('img\icon.png'))
        self.label=QLabel(self)
        self.label.setText("Mapa escogido: \""+self.mapchooser.map[0]+"\"")
        self.label.setGeometry(10,self.y-30,self.x,30)
        
        self.setWindowTitle("DuckieGUI")
        self.setFixedSize(self.x, self.y)

        #Definimos los botones para la ejecucion de la simulacion
        #button_map: Ejecuta la funcion para la seleccion del mapa de simulacion
        self.button_map = QPushButton(self, text="Escoger Mapa")
        self.button_map.setGeometry(int(self.x/2-55),int(self.y/2-50),110,30)
        self.button_map.clicked.connect(self.map_select)

    def map_select(self):#Esta funcion se encarga de selecionar el mapa de la simulacion
        self.mapchooser.show()

if __name__ == "__main__":  
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
