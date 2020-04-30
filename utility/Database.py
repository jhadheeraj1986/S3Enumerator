
from utility import utility
from pymongo import MongoClient, errors
from utility import encryptionHandler

# Database name is AppDB
class database():
    '''
    Handles all database related operations.
    '''
    def __init__(self, parent=None):
        self.connectionURl = utility.mongoDB_connectionURl

    def connect_to_db(self):
        '''
        Connect to MongoDB database
        '''
        utility.logObj.log("Connect to " + self.connectionURl)
        serverSelectionTimeoutMS=30     #default value is 30s
        try:
            self.client = MongoClient(self.connectionURl, serverSelectionTimeoutMS)
        except errors.ConnectionFailure:
            utility.logObj.log("Failed to connect to server.")
            return False

        return True

    def findUser(self, user_name):
        '''
        Find user details in DB
        '''
        print(self.client.AppDB)
        print("Database::findUser() - " + user_name + "\t", type(user_name))
        return self.client.AppDB.login.find_one({"user_name": user_name})

    def addNewUser(self, user):
        '''
        Add new user AWS details to DB
        '''
        return self.client.AppDB.login.insert_one(user)

    def IsValidUser(self, userName, password):
        '''
        Check whether user name and password are valid or not.
        '''
        search_result = self.findUser(userName)
        if search_result:
            utility.logObj.log("User found.")

            passDB = search_result.get("password")

            passKey = passDB.split(":-:")

            #Decrypt received password using key here
            decrypetedUserPassword = encryptionHandler.encryption.decryptString(passKey[0], passKey[1])
            strtoken = decrypetedUserPassword.decode("ascii")

            if password == strtoken:
                print("valid User")
                return True, "Valid User"
            else:
                return False, "wrong password."

        else:
            return False, "User not found"

    def addNewUserAwsCred(self, userCred):
        '''
        Add new user AWS credientials to DB
        '''
        return self.client.AppDB.credential.insert_one(userCred)

    def fetchUserCredfromDB(self, user_name):
        '''
        This function is to fetch AWS credentials for User_id passed. 
        This is for internal DB use. Don't use outside of this class.
        TODO: How to make a function private in a class.
        '''
        user_detail = self.findUser(user_name)
        user_id = user_detail.get("_id")

        print(self.client.AppDB)
        print("Database::findUserCred() - " + "\t", type(user_id))
        return self.client.AppDB.credential.find_one({"user_id": user_id})

    def getUserAWSCred(self, user_name):
        '''
        Get uses's aws cred from DB and decrypt it and return to main app for aws handler.
        Use this as an Interface.
        '''
        search_result = self.fetchUserCredfromDB(user_name)
        if search_result:
            EncryptedAccesKey = search_result.get("Access_key")
            AccesKeyKey = EncryptedAccesKey.split(":-:")
            #Decrypt received AccesKey using key here
            decrypetedAccesKey = encryptionHandler.encryption.decryptString(AccesKeyKey[0], AccesKeyKey[1])
            strAccesKey = decrypetedAccesKey.decode("ascii")

            EncryptedSecretKey = search_result.get("Secret_Key")
            SecretKeyKey = EncryptedSecretKey.split(":-:")
            #Decrypt received Secret using key here
            decrypetedSecretKey = encryptionHandler.encryption.decryptString(SecretKeyKey[0], SecretKeyKey[1])
            strSecretKey = decrypetedSecretKey.decode("ascii")

        return strAccesKey, strSecretKey
