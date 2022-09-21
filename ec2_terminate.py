#AWS Lambda to terminate instances:(http://rahuldhumal.com/techblog/index.php/2018/10/01/aws-lambda-to-terminate-instances/)

import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)
region = ‘eu-west-2’

s3 = boto3.client(‘s3’)
ec2 = boto3.client(‘ec2’, region_name=region)

def lambda_handler(event, context):
    logger.info(‘Event Details-{}’.format(event))
    bucket_name = event[‘Records’][0][‘s3’][‘bucket’][‘name’]
    file_key = event[‘Records’][0][‘s3’][‘object’][‘key’]
    logger.info(‘Reading {} from {}’.format(file_key, bucket_name))
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    lines_from_success_file = obj[‘Body’].read().split(b’\n’)
    instance_ids=[]
    for instance_id in lines_from_success_file:
        if instance_id:
            instance_ids.append(instance_id)
    logger.info(‘Instance to terminate -{}’.format(instance_ids))
    ec2.terminate_instances(InstanceIds=instance_ids)
