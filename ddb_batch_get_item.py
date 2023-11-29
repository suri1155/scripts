import boto3

# Scenario 1:
# get multiple items from DDB table, when we have unique PK's

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Specify the table name
table_name = 'YourTableName'

# List of primary keys (PKs) you want to retrieve
primary_keys = [{'YourPKAttributeName': 'Value1'}, {'YourPKAttributeName': 'Value2'}, {'YourPKAttributeName': 'Value3'}]


# Use batch_get_item to retrieve items based on the list of primary keys
# here table_name is DDB table name
response = dynamodb.batch_get_item(
    RequestItems={
        table_name: {
            'Keys': primary_keys
        }
    }
)

print("response == ", response)

#############################################################################################################################
# Scenario 2:
# get multiple items from DDB table, when we have unique PK's and multiple SK's (you have both PK's and Sk's in hand)

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Specify the table name
table_name = 'YourTableName'

# List of composite primary keys (PKs) you want to retrieve
composite_keys = [
    {'YourPartitionKeyAttributeName': 'PartitionValue1', 'YourSortKeyAttributeName': 'SortValue1'},
    {'YourPartitionKeyAttributeName': 'PartitionValue1', 'YourSortKeyAttributeName': 'SortValue2'},
    # Add more keys as needed
]

# Create a DynamoDB table resource
table = dynamodb.Table(table_name)

# Use batch_get_item to retrieve items based on the list of composite primary keys
response = table.batch_get_item(
    RequestItems={
        table_name: {
            'Keys': composite_keys
        }
    }
)

# Retrieve the items from the response
items = response['Responses'][table_name] 

print("items = ", items)


#############################################################################################################################
# Scenario 3:
# get multiple items from DDB table, when we have unique PK's and multiple SK's (but you have only PK's and not Sk's in hand)

# Specify the table name
table_name = 'YourTableName'

# Partition key value for which you want to retrieve all items
partition_key_value = 'YourPartitionValue'

# Create a DynamoDB table resource
table = dynamodb.Table(table_name)

# NOTE:Loop through each partition key value and retrieve all items, in case we have list of partition keys
# for partition_key_value in partition_key_values:

# Use query to retrieve all items with the specified partition key
response = table.query(
    KeyConditionExpression='YourPartitionKeyAttributeName = :partition_key',
    ExpressionAttributeValues={
        ':partition_key': partition_key_value
    }
)

# Retrieve the items from the response
items = response['Items']

# Print the retrieved items
for item in items:
    print(item)

#########################################################################################################################

# Example for Scenario 1
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
