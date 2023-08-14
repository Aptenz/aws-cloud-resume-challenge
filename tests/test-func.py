import unittest
from infra.lambda_module.func import lambda_handler
import boto3
from moto import mock_dynamodb


class TestLambdaHandler(unittest.TestCase):
    @mock_dynamodb
    def test_lambda_handler(self):
        # Setting up our mock DynamoDB
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.create_table(
            TableName="cloudresume-test",
            KeySchema=[
                {"AttributeName": "id", "KeyType": "HASH"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "id", "AttributeType": "S"},
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
        )

        # Initially setting views to 5
        table.put_item(Item={"id": "0", "views": 5})

        # Calling our lambda function
        views = lambda_handler(None, None)

        # Asserting that the returned views are the incremented value of the initial views
        self.assertEqual(views, 6)

        # Fetching the views directly from the table to double check
        response = table.get_item(Key={"id": "0"})
        self.assertEqual(response["Item"]["views"], 6)


if __name__ == "__main__":
    unittest.main()
