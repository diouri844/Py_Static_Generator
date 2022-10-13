import sys
import os 
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QFileDialog,QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# create the main class : 

class Generator(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # setup the main window :
        self.setWindowTitle(" Static Web genrator ")
        self.setWindowIcon(QIcon("assets/icons8-generated-photos-48.png"))
        self.setFixedSize(600,700)
        self.move(300,20)
        # setup variables :
        self.path = ""
        # add components : 
        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap("assets/icons8-generated-photos-48.png"))
        self.title = QLabel(self)
        self.title.setText(" Build Your static App Now ! ")
        self.project_name = QLineEdit(self)
        self.project_name.setPlaceholderText("Project Name ")
        self.project_folder = QLineEdit(self)
        self.project_folder.setPlaceholderText(" select a folder ")
        self.project_folder.setReadOnly(True)
        self.btn_select_folder = QPushButton(self)
        self.btn_select_folder.setText(" Select folder ")
        self.btn_select_folder.setCursor(Qt.PointingHandCursor)
        self.btn_build_project = QPushButton(self)
        self.btn_build_project.setText(" Create ")
        self.btn_build_project.setCursor(Qt.PointingHandCursor)
        # add eventListner : 
        self.btn_select_folder.clicked.connect(self.setDirName)
        self.btn_build_project.clicked.connect(self.buildProject)
        # set the style : 
        self.setStyleSheet("""
            background-color:#000814;
            color:#FFD60A;
            font-family:Times;
        """)
        self.logo.setStyleSheet("""
            font-size:45px;
            """)
        self.title.setStyleSheet("""
            font-size:25px;
            color:#FFD60A
            """)
        self.project_name.setStyleSheet("""
            font-size : 12px;
            width:250px;
            height:15px;
            border:1px solid #FFD60A;
            border-radius: 5px;
            color:#fff;
            padding:10px;
            """)
        self.project_folder.setStyleSheet("""
            font-size : 12px;
            width:250px;
            height:15px;
            border:1px solid #FFD60A;
            border-radius: 5px;
            color:#fff;
            padding:10px;
            """)
        self.btn_select_folder.setStyleSheet("""
            font-size : 12px;
            color:"#fff";
            border:none;
            """)
        self.btn_build_project.setStyleSheet("""
            font-size : 12px;
            color:"#fff";
            border:none;
            """)
        # place component :
        self.logo.move(150,100)
        self.title.move(188,112)
        self.project_name.move(150,160)
        self.project_folder.move(150,210)
        self.btn_select_folder.move(150,260)
        self.btn_build_project.move(380,260)
    def setDirName(self):
        path = os.path.expanduser("~")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        if dlg.exec_():
            self.path = dlg.selectedFiles()[0]
            self.project_folder.setText(self.path)
        return
    def buildProject(self):
        self.full_folder = ""
        # check if the project name is valable and project dirname :
        if len(self.path) and len(self.project_name.text()):
            print("create : ",self.project_name.text()," Origin :   ",self.path)
            try :
                os.mkdir(path=self.path+"/"+str(self.project_name.text()), mode=777)
                self.full_folder = self.path+"/"+str(self.project_name.text())
            except Exception as e:
                print("[ Create Folder Error : ] : "+str(e))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Create Project Error   ! ") 
            msg.setInformativeText("You cann't Create this project ")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        return

if __name__ == "__main__":
    instance = QApplication.instance()
    if not instance:
        instance = QApplication(sys.argv)
    my_app = Generator()
    my_app.show()
    instance.exec_()





