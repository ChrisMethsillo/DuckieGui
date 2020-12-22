from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
# ===================== CLASE SpeedWindow =========================
class SpeedWindow(QWidget):
    def __init__(self,mainwindow, parent=None):
        super(SpeedWindow, self).__init__(parent)
        self.x, self.y=240, 180
        self.window=mainwindow

        self.linearVelocity="0.44"
        self.angularVelocity="1"
        
        self.setWindowTitle("DuckieBot speed")
        self.setWindowIcon(QIcon("img/icon.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(self.x,self.y)

        self.initUI()

    def initUI(self):
        labelVL = QLabel("Linear speed", self)
        labelVL.move(50, 10)

        frameVL = QFrame(self)
        frameVL.setFrameShape(QFrame.StyledPanel)
        frameVL.setFixedWidth(140)
        frameVL.setFixedHeight(28)
        frameVL.move(50, 30)

        self.lineEditVL = QLineEdit(frameVL)
        self.lineEditVL.setValidator(QDoubleValidator())
        self.lineEditVL.setFrame(False)
      
        self.lineEditVL.setFixedWidth(120)
        self.lineEditVL.setFixedHeight(26)
        self.lineEditVL.move(40, 1)

        # ========================================================

        labelVA = QLabel("Angular speed", self)
        labelVA.move(50, 70)

        frameVA = QFrame(self)
        frameVA.setFrameShape(QFrame.StyledPanel)
        frameVA.setFixedWidth(140)
        frameVA.setFixedHeight(28)
        frameVA.move(50, 90)


        self.lineEditVA = QLineEdit(frameVA)
        self.lineEditVA.setValidator(QDoubleValidator())
        self.lineEditVA.setFrame(False)
     
        self.lineEditVA.setFixedWidth(120)
        self.lineEditVA.setFixedHeight(26)
        self.lineEditVA.move(40, 1)
        

      # ================== WIDGETS QPUSHBUTTON ===================

        OkButton = QPushButton("Accept", self)
        OkButton.setFixedWidth(135)
        OkButton.setFixedHeight(28)
        OkButton.move(52, 130)
        OkButton.clicked.connect(self.velocity)

      # ==================== SEÑALES BOTONES =====================
    def velocity(self):
        self.linearVelocity=str(self.lineEditVL.text())
        self.angularVelocity=str(self.lineEditVA.text())
        self.window.label3.setText("Linear speed: "+ str(self.linearVelocity))
        self.window.label4.setText("Angular speed: "+str(self.angularVelocity))
        self.close()
