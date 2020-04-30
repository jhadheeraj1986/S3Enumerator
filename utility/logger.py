

class logging():
    def __init__(self):
        self.log_file = open("S3Enumerator.log",'a')
        self.log("\n\n***********************************\n")

    def log(self, message):
        print(message)
        self.log_file.write(message)
        self.log_file.write("\n")
    
    def close(self):
        print("Closing log file.")
        self.log("***********************************\n\n")
        self.log_file.close()

    def __del__(self):
        self.close()