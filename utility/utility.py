from utility import logger as log
from utility import Database as db

logObj = log.logging()

mongoDB_connectionURl = "" #mongoDB Connection URL

dbObj = db.database()       #Creating object here. Is there any other way to keep only one instance of DB conection
