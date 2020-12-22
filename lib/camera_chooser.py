from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
import subprocess

class CamWindow(QWidget):
    #Main Window
    def __init__(self,mainwindow, *args, **kwargs):
        super(CamWindow, self).__init__(*args, **kwargs)
        #Estructura de la ventana principal
        self.x=430
        self.y=240
        self.cameralabel='Duckiebot'
        self.window=mainwindow

        self.camera='human'
        self.distortion="0"
        self.collision="0"
        self.roadline="0"

        self.setWindowIcon(QIcon('img\icon.png'))
        self.setWindowTitle("Choose camera")
        self.setFixedSize(self.x, self.y)

        #Definimos los botones para la ejecucion de la simulacion
        #button_top: Ejecuta la funcion para la seleccion del topa de simulacion
        self.button_top = QPushButton(self, text="Top view (Z key)")
        self.button_top.setGeometry(10,20,200,30)
        self.button_top.clicked.connect(self.top_camera)
        
        self.button_db = QPushButton(self, text="Duckiebot view (X key)")
        self.button_db.setGeometry(10,60,200,30)
        self.button_db.clicked.connect(self.human_camera)

        self.button_fish = QPushButton(self, text="Fish eye view (C key)")
        self.button_fish.setGeometry(10,100,200,30)
        self.button_fish.clicked.connect(self.fish_camera)

        self.button_collision = QPushButton(self, text="Top view with collision boxes (V key)")
        self.button_collision.setGeometry(220,20,200,30)
        self.button_collision.clicked.connect(self.collision_box)

        self.button_road = QPushButton(self, text="Activate road lines")
        self.button_road.setGeometry(220,60,200,30)
        self.button_road.clicked.connect(self.roadline_set)


        self.button_accept = QPushButton(self, text="Accept")
        self.button_accept.setGeometry(160,170,110,30)
        self.button_accept.clicked.connect(self.close)

        self.label=QLabel(self)
        self.label.setText("Chosen view: "+self.cameralabel)
        self.label.setGeometry(10,self.y-30,self.x,30)

        self.label2=QLabel(self)
        self.label2.setText("You can change the cameras in the simulator using the keys")
        self.label2.setGeometry(68,140,self.x,30)



    def top_camera(self):
        self.camera="top_down"
        self.distortion="0"
        self.collision="0"
        self.cameralabel='top view'
        self.label.setText("Chosen view: "+self.cameralabel)
        self.window.label2.setText("Camera: "+self.cameralabel)

    def human_camera(self):
        self.camera="human"
        self.distortion="0"
        self.collision="0"
        self.cameralabel='Duckiebot'
        self.label.setText("Chosen view: "+self.cameralabel)
        self.window.label2.setText("Camera: "+self.cameralabel)

    def fish_camera(self):
        self.camera="human"
        self.distortion="1"
        self.collision="0"
        self.cameralabel='Fish Eye'
        self.label.setText("Chosen view: "+self.cameralabel)
        self.window.label2.setText("Camera: "+self.cameralabel)

    def collision_box(self):
        self.camera="human"
        self.distortion="0"
        self.collision="1"
        self.cameralabel='Collision box'
        self.label.setText("Chosen view: "+self.cameralabel)
        self.window.label2.setText("Camera: "+self.cameralabel)

    def roadline_set(self):
        if self.roadline=="0":
            self.roadline="1"
            self.button_road.setText("Deactivate road lines")
        else:
            self.roadline="0"
            self.button_road.setText("Activate road lines")



 