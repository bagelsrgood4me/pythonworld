import pika
import sys
import time 
import uuid
from datetime import datetime
import json

connection_params = pika.ConnectionParameters(host='rabbitmq_container')
queue_name = "task_queue"


data = {
    "person": {
        "name": "John Doe",
        "age": 30,
        "addresses": [
            {
                "type": "home",
                "street": "123 Main St",
                "city": "Anytown",
                "state": "CA",
                "zip": "12345"
            },
            {
                "type": "work",
                "street": "456 Elm St",
                "city": "Another Town",
                "state": "NY",
                "zip": "54321"
            }
        ],
        "contacts": [
            {
                "type": "email",
                "value": "john.doe@example.com"
            },
            {
                "type": "phone",
                "value": "123-456-7890"
            }
        ]
    },
    "projects": [
        {
            "name": "Project A",
            "description": "Description of Project A",
            "tags": ["tag1", "tag2"],
            "contributors": ["Alice", "Bob"]
        },
        {
            "name": "Project B",
            "description": "Description of Project B",
            "tags": ["tag2", "tag3"],
            "contributors": ["Charlie", "David"]
        }
    ]
}

message = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:{uuid.uuid4()} Data: {json.dumps(data)}"

while True:
    try:
        # Establish connection
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)

        # Publish message
        channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        print(f"Message '{message}' sent to queue '{queue_name}'")

        # Close the channel and connection
        channel.close()
        connection.close()
        # time.sleep(0.01)

    except pika.exceptions.AMQPConnectionError as e:
        print(f"AMQPConnectionError: {e}")
        print("Attempting to reconnect in 5 seconds...")
        time.sleep(5)