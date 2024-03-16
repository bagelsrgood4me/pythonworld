#!/usr/bin/env python
import pika
import time

connection_params = pika.ConnectionParameters(host='rabbitmq_container')
queue_name = "task_queue"

while True:
    try:
        # Establish connection
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)

        # Start consuming messages
        for method_frame, properties, body in channel.consume(queue_name, auto_ack=True):
            if body:
                print(f"Received message: {body.decode('utf-8')}")
                # Acknowledge the message
                # channel.basic_ack(method_frame.delivery_tag)
            else:
                print("No more messages in the queue.")
                break

        # Close the channel and connection
        channel.close()
        connection.close()

    except pika.exceptions.AMQPConnectionError as e:
        print(f"AMQPConnectionError: {e}")
        print("Attempting to reconnect in 5 seconds...")
        time.sleep(5)