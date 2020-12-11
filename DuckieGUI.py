from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

from lib.speed_chooser import *
from lib.camera_chooser import *
import subprocess

class MainWindow(QMainWindow):
    #Main Window
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.map=('','')
        self.speedchooser=SpeedWindow()
        self.camerachooser=CamWindow()

        self.img=QLabel(self)
        self.pixmap = QPixmap('img\icon.png')
        self.img.setPixmap(self.pixmap)
        self.img.setGeometry(140,10,430,300)

        
        #Estructura de la ventana principal
        self.x=480
        self.y=340

        self.setWindowIcon(QIcon('img\icon.png'))
        self.label=QLabel(self)
        self.label.setText("Chosen map: \""+self.map[0]+"\"")
        self.label.setGeometry(10,self.y-30,self.x,30)
        
        self.setWindowTitle("DuckieGUI")
        self.setFixedSize(self.x, self.y)

        #Definimos los botones para la ejecucion de la simulacion
        #button_map: Ejecuta la funcion para la seleccion del mapa de simulacion
        self.button_map = QPushButton(self, text="Map Select")
        self.button_map.setGeometry(10,10,110,30)
        self.button_map.clicked.connect(self.map_select)

        self.button_speed = QPushButton(self, text="Select speed")
        self.button_speed.setGeometry(10,50,110,30)
        self.button_speed.clicked.connect(self.velocity_select)

        self.button_speed = QPushButton(self, text="Select camera")
        self.button_speed.setGeometry(10,90,110,30)
        self.button_speed.clicked.connect(self.camera_select)


        self.button_run = QPushButton(self, text="Start simulation")
        self.button_run.setGeometry(10,self.y-70,110,30)
        self.button_run.clicked.connect(self.run_simulation)


    def map_select(self):#Esta funcion se encarga de selecionar el mapa de la simulacion
        self.map=QFileDialog.getOpenFileName(self, "Select Map","", "Archivos soportados (*.yaml)")
        self.label.setText("Chosen map: \""+self.map[0]+"\"")
 
    def velocity_select(self):
        self.speedchooser.show()

    def camera_select(self):
        self.camerachooser.show()

    def run_simulation(self):
        linearspeed=self.speedchooser.linearVelocity
        bend=self.speedchooser.angularVelocity
        camera=self.camerachooser.camera
        distortion=self.camerachooser.distortion
        collision=self.camerachooser.collision
        curve=self.camerachooser.roadline

        if self.map[0]=="":
            msg = QMessageBox()
            msg.setWindowIcon(QIcon('img/icon.png'))
            msg.setWindowTitle("Alert")
            msg.setFixedSize(300,150)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Choose a map")
            x = msg.exec_()
        else:
            subprocess.Popen("conda activate gym-duckietown && python gym-duckietown/manual_control.py --env-name Duckietown --map-name "+
            self.map[0]+" --distortion "+distortion+" --draw-curve "+curve+" --draw-bbox "+collision+" --linearspeed "+linearspeed+" --bend "+bend+" --camera "+camera,shell=True)

        
        
if __name__ == "__main__":  
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
