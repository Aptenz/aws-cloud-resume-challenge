import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("cloudresume-test")

    # get the item at key value 0
    response = table.get_item(Key={"id": "0"})

    # get the views from the table and add one
    views = response["Item"]["views"]
    views += 1
    print(views)
    response = table.put_item(Item={"id": "0", "views": views})

    return views
