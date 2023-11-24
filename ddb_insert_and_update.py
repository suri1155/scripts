def ddb_read_and_update():
    """
    This fucntion inserts and updates item in DDB, when DDB attribute is reserved keyword "Data"
    """
    # Define the table name
    table_name = 'Person'


    try:
        # Create a DynamoDB table if it doesn't exist
        table = ddb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'N'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        # Wait until the table exists
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
    except:
        table = ddb.Table(table_name)

    # Insert data into the table
    table = ddb.Table(table_name)

    data = {
        "id": 2,
        "Data": {"name": "bean", "siblings": ["Alice", "Bob"]},
        "education": ["BTECH", "MBA"]
    }

    response = table.put_item(Item=data)

    print("Item inserted:", response)

    # Retrieve data from the table
    item_id = 2

    response = table.get_item(
        Key={
            'id': item_id
        },
        ProjectionExpression='#data',
        ExpressionAttributeNames={
            '#data': 'Data'
        }
    )
    print("response = ", response)
    item = response.get('Item')


    if item:
        siblings = item.get('Data', {}).get('siblings', [])
        print(f"Siblings for ID {item_id}: {siblings}")
    else:
        print(f"No item found with ID {item_id}")

    # Specify the item you want to update based on the ID
    item_id = 2

    # Update the "siblings" attribute with ExpressionAttributeNames
    update_expression = 'SET #data.siblings = :new_siblings'
    expression_attribute_values = {':new_siblings': ["Alice", "Bob", "Mary"]}
    expression_attribute_names = {'#data': 'Data'}

    response = table.update_item(
        Key={'id': item_id},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ExpressionAttributeNames=expression_attribute_names,
        ReturnValues='UPDATED_NEW'
    )

    # Print the updated item
    updated_item = response.get('Attributes', {})
    print("Updated item:", updated_item)