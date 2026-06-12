from abc import ABC, abstractmethod


# 1. Abstract Base Class (The Contract)
class CloudStorage(ABC):

    @abstractmethod
    def upload_file(self, file_name):
        pass

    @abstractmethod
    def delete_file(self, file_name):
        pass


# 2. Concrete Implementation 1
class AWSStorage(CloudStorage):

    def upload_file(self, file_name):
        return "Uploading " + file_name + " to AWS S3 bucket structural block"

    def delete_file(self, file_name):
        return "Deleting " + file_name + " from AWS S3"


# 3. Concrete Implementation 2
class GoogleDriveStorage(CloudStorage):

    def upload_file(self, file_name):
        return "Uploading " + file_name + " to Google Drive API cluster"

    def delete_file(self, file_name):
        return "Deleting " + file_name + " from Google Drive"


# 4. Live Execution Driver Block
if __name__ == "__main__":
    aws_client = AWSStorage()
    print(aws_client.upload_file("semester_notes.pdf"))
    print(aws_client.delete_file("old_pic.jpg"))

    gdrive_client = GoogleDriveStorage()
    print(gdrive_client.upload_file("project_source_code.zip"))
    print(gdrive_client.delete_file("temp_file.txt"))