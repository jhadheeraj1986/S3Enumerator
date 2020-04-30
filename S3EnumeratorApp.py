from PySide2 import QtWidgets       #for QT widgets and function. pip install PySide2
from pymongo import MongoClient, errors
from pprint import pprint
from ui import login
from utility import utility
from ui import MainUI
from SignUp import CSignupDialog
from utility import awsDetailsPageHandler



class S3Enum(login.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(S3Enum, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("S3Enumerator")

        self.dbObj = utility.dbObj
        self.dbObj.connect_to_db()

        self.login_Btn.clicked.connect(self.login)
        self.Signup_Btn.clicked.connect(self.signUP)

    def login(self):
        user_name = self.user_name_LE.text()
        if not user_name:
            utility.logObj.log("User name error.")
            QtWidgets.QMessageBox.about(self,"User name error", "Please add valid user name")
            return

        password = self.password_LE.text()
        if not password:
            utility.logObj.log("Password Error.")
            QtWidgets.QMessageBox.about(self, "Password Error", "Please provide valid password")
            return
        
        print(user_name + "\t" + password)
        IsValid, err = self.dbObj.IsValidUser(user_name, password)
        if IsValid:
            strAccesKey, strSecretKey = self.dbObj.getUserAWSCred(user_name)

            self.hide()
            awshandlerDialog = awsDetailsPageHandler.awsUIHandler()
            awshandlerDialog.SetUserAwsCred(strAccesKey, strSecretKey)
            awshandlerDialog.show()
            awshandlerDialog.exec_() 
            self.user_name_LE.clear()
            self.password_LE.clear() 
            self.show()
        else:
            QtWidgets.QMessageBox.about(self, "Password Error", err)

    def signUP(self):
        utility.logObj.log(" Signup.")
        self.signupDialog = CSignupDialog()
        self.signupDialog.show()


               
        




if __name__ == "__main__":
    utility.logObj.log(__name__)

    app = QtWidgets.QApplication()
    S3EnumApp = S3Enum()
    S3EnumApp.show()
    app.exec_()

    utility.logObj.close()