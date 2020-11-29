from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
import subprocess

class MainWindow(QMainWindow):
    #Main Window
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #Estructura de la ventana principal
        self.x=600
        self.y=200
        self.map=("","")

        self.setWindowIcon(QIcon('DuckieGUI_icon.png'))
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

        #button_run: Ejecuta la simulacion con el mapa escogido
        self.button_run =QPushButton(self, text="Ejecutar Simulador")
        self.button_run.setGeometry(int(self.x/2-55),int(self.y/2),110,30)
        self.button_run.clicked.connect(self.run_map)

    def map_select(self):#Esta funcion se encarga de selecionar el mapa de la simulacion
        self.map= QFileDialog.getOpenFileName(self, "Select Map","", "Archivos soportados (*.yaml)")
        self.label.setText("Mapa escogido: \""+self.map[0]+"\"")

    def run_map(self):#Se ejecuta la simulacion de duckietown con el mapa escogido
        if self.map[0]=="":
            msg = QMessageBox()
            msg.setWindowIcon(QIcon('DuckieGUI_icon.png'))
            msg.setWindowTitle("Alerta")
            msg.setFixedSize(300,150)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Seleccione un mapa")
            x = msg.exec_()
        else:
            subprocess.Popen("conda activate gym-duckietown && python manual_control.py --env-name Duckietown --map-name "+self.map[0],shell=True)
#Ejecucion del script
if __name__ == "__main__":  
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
