# DDB insert MAP (dict or Json) and deserialize post get_item

import boto3
from boto3.dynamodb.types import TypeDeserializer

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = 'YourTableName'
table = dynamodb.Table(table_name)

# Define a map-type item without type annotations
item = {
    'PK': 'example_key',
    'SK': 'example_subkey',
    'info': {
        'name': 'John Doe',
        'age': 30,
        'address': {
            'city': 'Example City',
            'state': 'Example State'
        }
    }
}

# # Convert the item to DynamoDB format
# deserializer = TypeDeserializer()
# dynamodb_item = {key: deserializer.deserialize(value) for key, value in item.items()}
dynamodb_item = item

# Put the item into DynamoDB
response = table.put_item(Item=dynamodb_item)
print("PutItem succeeded:", response)


# ########## get item
# Get the item from DynamoDB
response = table.get_item(
    Key={
        'PK': 'example_key',
        'SK': 'example_subkey'
    }
)

# thies where we deserioalize (To go from low-level format to python)
# Convert DynamoDB item to a format without type annotations
item_from_dynamodb = response.get('Item', {})
serializer = TypeDeserializer()
converted_item = {key: serializer.serialize(value) for key, value in item_from_dynamodb.items()}

# Access the converted attributes
info_map = converted_item.get('info')
if info_map:
    print("Name:", info_map.get('name'))
    print("Age:", info_map.get('age'))
    address_map = info_map.get('address')
    if address_map:
        print("City:", address_map.get('city'))
        print("State:", address_map.get('state'))



#######################################################################################
# Example from stackoverflow
# https://stackoverflow.com/questions/43755888/how-to-convert-a-boto3-dynamo-db-item-to-a-regular-dictionary-in-python

import boto3

low_level_data = {
  "ACTIVE": {
    "BOOL": True
  },
  "CRC": {
    "N": "-1600155180"
  },
  "ID": {
    "S": "bewfv43843b"
  },
  "params": {
    "M": {
      "customer": {
        "S": "TEST"
      },
      "index": {
        "N": "1"
      }
    }
  },
  "THIS_STATUS": {
    "N": "10"
  },
  "TYPE": {
    "N": "22"
  }
}

# Lazy-eval the dynamodb attribute (boto3 is dynamic!)
boto3.resource('dynamodb')

# To go from low-level format to python
deserializer = boto3.dynamodb.types.TypeDeserializer()
python_data = {k: deserializer.deserialize(v) for k,v in low_level_data.items()}

# To go from python to low-level format
serializer = boto3.dynamodb.types.TypeSerializer()
low_level_copy = {k: serializer.serialize(v) for k,v in python_data.items()}

assert low_level_data == low_level_copy
