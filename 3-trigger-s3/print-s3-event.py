import boto3


s3 = boto3.client('s3')


def lambda_handler(event, context):

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(f"Event: {event}")
    # print(f"Bucket: {bucket_name}")
    # print(f"Key: {key}")
