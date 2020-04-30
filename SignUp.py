from PySide2 import QtWidgets
from utility import utility
from PySide2.QtCore import ( QRect)
from utility import encryptionHandler

class CSignupDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CSignupDialog, self).__init__(parent)
        self.db = utility.dbObj

        utility.logObj.log("Start SignUp process. Creating sign up widget")
        
        self.nameLable = QtWidgets.QLabel("Name:")
        
        self.name_LE = QtWidgets.QLineEdit()
        self.findText = ''

        self.UserNameLable = QtWidgets.QLabel("User Name:")
        self.UserName_LE = QtWidgets.QLineEdit()

        self.PasswordLable = QtWidgets.QLabel("Password:")
        self.Password_LE = QtWidgets.QLineEdit()

        self.AccessKeyLable = QtWidgets.QLabel("AWS access key id:")
        self.AccessKey_LE = QtWidgets.QLineEdit()

        self.SecretKeyLable = QtWidgets.QLabel("AWS secret access key:")
        self.SecretKey_LE = QtWidgets.QLineEdit()

        self.EmailLable = QtWidgets.QLabel("Email:")
        self.Email_LE = QtWidgets.QLineEdit()

        layout = QtWidgets.QFormLayout()

        layout.addWidget(self.nameLable)
        layout.addWidget(self.name_LE)

        layout.addWidget(self.UserNameLable)
        layout.addWidget(self.UserName_LE)

        layout.addWidget(self.PasswordLable)
        layout.addWidget(self.Password_LE)

        layout.addWidget(self.AccessKeyLable)
        layout.addWidget(self.AccessKey_LE)

        layout.addWidget(self.SecretKeyLable)
        layout.addWidget(self.SecretKey_LE)

        layout.addWidget(self.EmailLable)
        layout.addWidget(self.Email_LE)

        self.SignUpButton = QtWidgets.QPushButton("&SignUp")
        layout.addWidget(self.SignUpButton)

        self.setLayout(layout)
        self.setWindowTitle("Please SignUp")
        self.setFixedWidth(300)

        self.SignUpButton.clicked.connect(self.SignUpButtonClicked)
        self.SignUpButton.clicked.connect(self.accept)

    def SignUpButtonClicked(self):
        '''
        This function gets user information and save it to mongoDB.
        '''
        Name = self.name_LE.text()
        if not Name:
            QtWidgets.QMessageBox.information(self, "Empty Field",
                    "Please enter a name.")
            return

        UserName = self.UserName_LE.text()
        if not UserName:
            QtWidgets.QMessageBox.information(self, "Empty Field",
                    "Please enter a UserName.")
            return

        Password = self.Password_LE.text()
        if not Password:
            QtWidgets.QMessageBox.information(self, "Empty Field",
                    "Please enter a Password.")
            return

        encrypertedPassword, Passwordkey = encryptionHandler.encryption.encryptString(Password)
        #utility.logObj.log("Password: ")
        #utility.logObj.log(encrypertedPassword)

        AccessKey = self.AccessKey_LE.text()
        if not AccessKey:
            QtWidgets.QMessageBox.information(self, "Empty Field",
                    "Please enter a AccessKey.")
            return

        encrypertedAccessKey, AccessKeykey = encryptionHandler.encryption.encryptString(AccessKey)
        #utility.logObj.log("AccessKey: ")
        #utility.logObj.log(encrypertedAccessKey)

        SecretKey = self.SecretKey_LE.text()
        if not SecretKey:
            QtWidgets.QMessageBox.information(self, "Empty Field",
                    "Please enter a SecretKey.")
            return

        encrypertedSecretKey, SecretKeykey = encryptionHandler.encryption.encryptString(SecretKey)
        #utility.logObj.log("SecretKey: ")
        #utility.logObj.log(encrypertedSecretKey)

        Email = self.Email_LE.text()
        if not Email:
            QtWidgets.QMessageBox.information(self, "Empty Field",
                    "Please enter a Email.")
            return

        user = {
            "name" : Name,
            "user_name" : UserName,
            "password" : encrypertedPassword + ":-:" + Passwordkey, 
            "email" : Email
        }

        returId = self.db.addNewUser(user)
        utility.logObj.log(str(returId.inserted_id))

        awsCredential = {
            "user_id" : returId.inserted_id,
            "Access_key": encrypertedAccessKey + ":-:" + AccessKeykey,
            "Secret_Key": encrypertedSecretKey + ":-:" +SecretKeykey,
        }

        retawsCred = self.db.addNewUserAwsCred(awsCredential)
        utility.logObj.log(str(retawsCred.inserted_id))



