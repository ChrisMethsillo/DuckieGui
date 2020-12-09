from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame, QLabel, QComboBox, QLineEdit,
                             QPushButton, QWidget)


# ===================== CLASE ventanaLogin =========================

class SpeedWindow(QWidget):
    def __init__(self, parent=None):
        super(SpeedWindow, self).__init__(parent)
        self.x, self.y=380, 180
        
        self.setWindowTitle("Velocidad del DuckieBot")
        self.setWindowIcon(QIcon("img/icon.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(self.x,self.y)

        self.initUI()

    def initUI(self):
        labelVL = QLabel("Velocidad Lineal", self)
        labelVL.move(50, 10)

        frameVL = QFrame(self)
        frameVL.setFrameShape(QFrame.StyledPanel)
        frameVL.setFixedWidth(280)
        frameVL.setFixedHeight(28)
        frameVL.move(50, 30)

        self.lineEditVL = QLineEdit(frameVL)
        self.lineEditVL.setFrame(False)
        self.lineEditVL.setTextMargins(8, 0, 4, 1)
        self.lineEditVL.setFixedWidth(238)
        self.lineEditVL.setFixedHeight(26)
        self.lineEditVL.move(40, 1)

        # ========================================================

        labelVA = QLabel("Velocidad Angular", self)
        labelVA.move(50, 70)

        frameVA = QFrame(self)
        frameVA.setFrameShape(QFrame.StyledPanel)
        frameVA.setFixedWidth(280)
        frameVA.setFixedHeight(28)
        frameVA.move(50, 90)


        self.lineEditVA = QLineEdit(frameVA)
        self.lineEditVA.setFrame(False)
        self.lineEditVA.setTextMargins(8, 0, 4, 1)
        self.lineEditVA.setFixedWidth(238)
        self.lineEditVA.setFixedHeight(26)
        self.lineEditVA.move(40, 1)

      # ================== WIDGETS QPUSHBUTTON ===================

        buttonLogin = QPushButton("Aceptar", self)
        buttonLogin.setFixedWidth(135)
        buttonLogin.setFixedHeight(28)
        buttonLogin.move(120, 130)

      # ==================== SEÑALES BOTONES =====================
    def velocity(self):
        self.linearVelocity=self.lineEditVL.text()
        self.AngularVelocity=self.lineEditVA.text()


# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")

    aplicacion.setFont(fuente)
    
    ventana = SpeedWindow()
    ventana.show()
    
    sys.exit(aplicacion.exec_())