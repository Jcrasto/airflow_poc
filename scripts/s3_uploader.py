import boto3
import os
import logging

if __name__ == "__main__":
    session = boto3.session.Session()
    s3_client = session.client('s3')

    response = s3_client.list_objects(
        Bucket='crasto-distribution-random-sampling',
    )

    object_list = []
    for object in response['Contents']:
        object_list.append(object['Key'])

    file_folder_list = os.listdir("../files/")

    for file in file_folder_list:
        if file not in object_list and ".csv" in file:
            logging.info("Uploading file : ../files/" + file + " to crasto-distribution-random-sampling")
            s3_client.upload_file("../files/" + file ,'crasto-distribution-random-sampling',file)