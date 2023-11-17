# !/usr/bin/python
import boto3
import re

client = boto3.client('s3')

def all_buckets_in_server():  # TO DISPLAY THE BUCKETS PRESENT IN THE SERVER AND SAVE THAT BUCKET NAMES IN AN FILE WHICH USER WANT TO SAVE AS FILE
    global bucket_name
    bucket_name = []
    clint = client.list_buckets()
    bucket_details = clint['Buckets']
    usr_inp = input("If you want to save the list of bucket name present in the server to an file in local press 1 Else press 'ENTER'\n")
    if (usr_inp == "1"):
        inp_fil_path = input("Please enter the path to save the file")
        inp_new_file_name = input("Please enter the file name for new file\n")
        fil = open("{0}/{1}".format(inp_fil_path,inp_new_file_name), 'a')
        for buck in bucket_details:
            bucket_name.append(buck['Name'])
            fil.write(buck['Name'])
            fil.write('\n')
        fil.write("===============\n")
        fil.close()
    else:
        for buck in bucket_details:
            bucket_name.append(buck['Name'])


def new_bucket():  # THIS BLOCK WILL CREATE NEW BUCKET
    inp_name = input("Please enter the bucket name:")
    inp_rgn = input("Please enter the region name:")
    try:
        response = client.create_bucket(
            Bucket=inp_name,
            CreateBucketConfiguration={
                'LocationConstraint': inp_rgn,
            }, )
        print("The bucket is created:{0}".format(response['Location']))
    except Exception as e:
        print("There was an error occurred during creation of bucket.Error states that\n{0}".format(e))


def upload_content():  # THIS BLOCK WILL UPLOAD CONTENT TO THE BUCKET
    inp_file_path = input("Please enter the file name with file path to upload \n")
    inp_buck_name = input("Please enter the bucket name\n")
    inp_file_txt = input("Please enter the file should named in server\n")
    try:
        response = client.upload_file('{0}'.format(inp_file_path), '{0}'.format(inp_buck_name),'{0}'.format(inp_file_txt))
    except Exception as e:
        print("There is an error occurred during uploading file\n{0}".format(e))


def download_contents():  # THIS BLOCK WILL DOWNLOAD CONTENT FROM BUCKET
    inp_buck_name = input("Please enter the bucket name\n")
    inp_file_name = input("Please enter the file named present in server\n")
    inp_file_path = input("Please enter the directory path where file should download \n")
    try:
        responce = client.download_file('{0}'.format(inp_buck_name), '{0}'.format(inp_file_name),'{0}'.format(inp_file_path))
    except Exception as e:
        print("There is an error occurred during downloading content it says\'n{0}'".format(e))


def delete_bucket_content():  # THIS BLOCK WILL DELETE THE CONTENT FROM THE BUCKET
    inp_buck_name = input("Please enter the bucket name\n")
    inp_file_name = input("Please enter the file name\n")
    try:
        response = client.delete_objects(
            Bucket='{0}'.format(inp_buck_name),
            Delete={
                'Objects': [
                    {
                        'Key': '{0}'.format(inp_file_name)
                    },
                ],
            }
        )
        print("The content {0} is deleted from bucket:{1}".format(inp_file_name, inp_buck_name))
    except Exception as e:
        print("There is an error occurred during deleting the content inside the file error states that \n{0}".format(e))


def delete_bucket():  # THIS BLOCK WILL DELETE THE BUCKET
    inp_buck_name = input("Please enter the bucket name\n")
    try:
        response = client.delete_bucket(
            Bucket='{0}'.format(inp_buck_name)
        )
        print("The bucket {0} is deleted successfully".format(inp_buck_name))
    except Exception as e:
        print("There is an error occurred while deleting buckets it states that\n{0}".format(e))




while True:

    all_buckets_in_server()  # TO DISPLAY BUCKET NAMES
    print("Below are the buckets present in the server\n{0}".format(bucket_name))

    #ASKING USER INPUT FOR WHAT OPERATION THEY WANT TO PERFORM
    inp = input("If you want to create an  bucket press 1\nIf you want to upload the object to the bucket press 2\nIf you want to download the file from bucket press 3\nTo delete the content from the bucket press 4\nTo delete bucket press 5\n")

    if (inp == "1"):  # TO CREATE NEW BUCKET
        new_bucket()


    elif (inp == "2"):  # TO UPLOAD CONTENT TO THE BUCKET
        upload_content()


    elif (inp == "3"):  # TO DOWNLOAD THE CONTENTS FROM THE S3 BUCKET
        download_contents()


    elif (inp == "4"):  # TO DELETE THE CONTENT FROM THE BUCKET
        delete_bucket_content()


    elif (inp == "5"):  # TO DELETE THE BUCKET
        delete_bucket()

    else:
        print("Please enter the valid user input")

 # Ask if the user wants to perform operations again
    repeat = input("Do you want to perform another operation? (yes/no): ").lower()
    if (repeat != "yes"):
        print("Exiting the program.")
        break
