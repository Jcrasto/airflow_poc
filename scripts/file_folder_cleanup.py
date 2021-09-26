import boto3
import os
import logging

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

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
        if file in object_list and ".csv" in file:
            logging.info("Removing file : ../files/" + file + " from files/ directory")
            os.remove("../files/" + file)