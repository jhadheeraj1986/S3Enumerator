from PySide2 import QtWidgets 
from ui import MainUI
from utility import utility
from utility import awsS3Handler
import os

class awsUIHandler(MainUI.Ui_awsDialog, QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(awsUIHandler, self).__init__(parent)
        utility.logObj.log("Inside awsHandler")
        self.setupUi(self)
        self.setWindowTitle("S3Enumerator")
        self.awsConnection = awsS3Handler.awsS3Operations()
        
        self.awsConfig_PB.clicked.connect(self.awsConfig)
        self.CreateBucket_PB.clicked.connect(self.CreateBucket)
        self.ShowBucket_PB.clicked.connect(self.ListBuckets)
        self.DownloadObject_PB.clicked.connect(self.DownloadS3Obj)
        self.S3Widget.itemDoubleClicked.connect(self.getData)

        self.UplpadObject_PB.clicked.connect(self.UploadObjToS3)


    def awsConfig(self):
        QtWidgets.QMessageBox.about(self, "test", "test")
        
        #TODO: Start working form here.

    def SetUserAwsCred(self, strAccesKey, strSecretKey):
        print("SetUserAwsCred")
        print(strAccesKey + "\t" + strSecretKey)
        QtWidgets.QMessageBox.information(self, "SetUserAwsCred",
                    strAccesKey + " - " + strSecretKey)

    def CreateBucket(self):
        bucketName = self.BucketName_LE.text()
        print("Create a bucket" + bucketName) 
        self.awsConnection.dummy()
        self.awsConnection.CreateBucket(bucketName)

    def ListBuckets(self):
        print("List buckets")
        bucketList = self.awsConnection.GetBucketList()
        self.treeWidgetItem = []
        self.S3Widget.setColumnCount(3)
        for i in range(len(bucketList)):
            bucketName = str(bucketList[i]["Name"])
            # Convert datetime.datetime() obj to string format
            bucketCreationDate = bucketList[i]["CreationDate"].strftime('%m/%d/%Y') 

            listItem = QtWidgets.QTreeWidgetItem(self.S3Widget, [str(i+1),bucketName,bucketCreationDate])
            self.treeWidgetItem.append(listItem)

        for i in range(len(self.treeWidgetItem)):
           QtWidgets.QTreeWidgetItem(self.treeWidgetItem[i],[str(i+1),bucketName,bucketCreationDate] )   #self.treeWidgetItem[i],[str(i+1),bucketName,bucketCreationDate]
           #self.treeWidgetItem[i].addChildren([str(i+1),bucketName,bucketCreationDate])


    def DownloadS3Obj(self):
        print("Download selected S3 obj")
        # index = self.S3Widget.currentIndex()
        # data = self.S3Widget.model().data(index)
        # print("Index: ", data)

        # item = self.S3Widget.selectedItems()
        # item[0].data()
        # print("index: " ,item[0].data())

        # self.S3Widget.currentColumn()
        # print("index1: " ,self.S3Widget.currentColumn())    #Will give the coloumn selected not Row
        # self.treeWidgetItem[0].indexOfChild()

        item = self.S3Widget.selectedItems()
        #item.getData()
        print(item[0])

    def getData(self, val):
        print("getData()")
        print(val.data(0,1))
        # print(val.row())
        # print(val.column())



    def UploadObjToS3(self):
        print("Upload Oj to s3")
        #text, ok = QInputDialog.getText(self, "", "")
