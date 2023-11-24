import boto3

# Replace these with your AWS credentials
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'
aws_region = 'us-east-1'  # Replace with your desired AWS region

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Define the table name
table_name = 'Person'

# Get a reference to the table
table = dynamodb.Table(table_name)

# Specify the list of item IDs you want to retrieve
item_ids = [1, 2]

# Perform the batch_get_item operation
response = table.batch_get_item(
    Keys=[
        {'id': item_id} for item_id in item_ids
    ]
)

# Extract the relevant data from the response
items = response.get('Responses', {}).get(table_name, [])

for item in items:
    print("Item:", item)
