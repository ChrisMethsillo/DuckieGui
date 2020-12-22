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
        self.speedchooser=SpeedWindow(self)
        self.camerachooser=CamWindow(self)

        self.img=QLabel(self)
        self.pixmap = QPixmap('img\icon.png')
        self.img.setPixmap(self.pixmap)
        self.img.setGeometry(140,10,430,320)

        
        #Estructura de la ventana principal
        self.x=480
        self.y=420

        self.setWindowIcon(QIcon('img\icon.png'))
        self.label=QLabel(self)
        self.label.setText("Chosen map:")
        self.label.setGeometry(140,self.y-100,self.x,30)

        self.label2=QLabel(self)
        self.label2.setText("Camera: "+self.camerachooser.cameralabel)
        self.label2.setGeometry(140,self.y-80,self.x,30)

        self.label3=QLabel(self)
        self.label3.setText("Linear speed: "+ str(self.speedchooser.linearVelocity))
        self.label3.setGeometry(140,self.y-60,self.x,30)

        self.label4=QLabel(self)
        self.label4.setText("Angular speed: "+str(self.speedchooser.angularVelocity))
        self.label4.setGeometry(140,self.y-40,self.x,30)
        
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

        self.button_speed = QPushButton(self, text="Select initial camera")
        self.button_speed.setGeometry(10,90,110,30)
        self.button_speed.clicked.connect(self.camera_select)

        self.button_run = QPushButton(self, text="Start simulation")
        self.button_run.setGeometry(10,self.y-70,110,30)
        self.button_run.clicked.connect(self.run_simulation)


    def map_select(self):#Esta funcion se encarga de selecionar el mapa de la simulacion
        self.map=QFileDialog.getOpenFileName(self, "Select Map","", "Archivos soportados (*.yaml)")
        i=-1
        flag=True
        tex=''
        while flag:
            if len(self.map[0])==0:
                break
            elif self.map[0][i]=="/":
                tex=self.map[0][i+1:]
                flag=False
            else:
                i-=1
        self.label.setText("Chosen map: "+tex)
 
    def velocity_select(self):
        self.speedchooser.show()
        linearspeed=self.speedchooser.linearVelocity
        bend=self.speedchooser.angularVelocity
        

    def camera_select(self):
        self.camerachooser.show()
        self.label2.setText("Camera: "+self.camerachooser.cameralabel)

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
    

