# AWS Automation with Python
# A. S3 Bucket Management Script
## Introduction
This Python script allows you to manage Amazon S3 buckets easily. It utilizes the Boto3 library to interact with the AWS S3 service. You can perform operations such as listing all buckets, creating a new bucket, uploading and downloading files, deleting content from a bucket, and deleting a bucket.

### Prerequisites
Before using the script, ensure you have the following:

* Python installed on your machine.

Boto3 library installed. You can install it using the following  command:

``` 
pip install boto3 
```
1. Usage: 
Clone the repository:

```
git clone https://github.com/180172/AWS-Automation_with_Python.git
```
2. Navigate to the project directory:

```
cd your-repository
```
3. Run the script:

``` 
python s3_bucket_management.py
```

* Follow the on-screen instructions to perform various operations on your S3 buckets.

-  Operations
### 1. List Buckets:
Displays a list of buckets present in the server.

### 2.  Create New Bucket:
Creates a new S3 bucket.

### 3. Upload Content:
Uploads a file to a specified bucket.

### 4. Download Contents:
Downloads a file from a specified bucket.

### 5. Delete Bucket Content:
Deletes a specific file from a bucket.

### 6. Delete Bucket:
Deletes an entire bucket.

### Additional Information: 
* If you choose to save the list of buckets to a file, you will be prompted to enter a file path and name.
* Ensure your AWS credentials are properly configured on your machine before running the script.
License

### Feel free to contribute or report issues!
