import boto3
from botocore.exceptions import ClientError

class awsS3Operations():
    def __init__(self, parent=None):
        print("inside awsOperations class inti()")
        self.S3_client = boto3.client("s3")     #'s' should be small
    
    def dummy(self):
        print("Dummy print.")

    def CreateBucket(self, bucketName):
        try:
            location = {'LocationConstraint': "ap-south-1"}
            result = self.S3_client.create_bucket(Bucket=bucketName,
                                    CreateBucketConfiguration=location)
            print("createBucket: ", result)

        except ClientError as e:
            print(e)
            return False
        
        return True

    def GetBucketList(self):
        print("Fetch Bucket list")
        bucketDict = self.S3_client.list_buckets()
        bucketList = bucketDict["Buckets"]
        print(bucketList)
        return bucketList


    
