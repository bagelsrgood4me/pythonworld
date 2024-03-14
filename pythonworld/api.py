from ninja import NinjaAPI
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)
# import pika
# import sys
# import time


api = NinjaAPI()
# connection_params = pika.ConnectionParameters(host='rabbitmq_container')


# def send_message(queue_name: str, message: str):
#     while True:
#         try:
#             # Establish connection
#             connection = pika.BlockingConnection(connection_params)
#             channel = connection.channel()
#             channel.queue_declare(queue=queue_name)

#             # Publish message
#             channel.basic_publish(exchange='', routing_key=queue_name, body=message)
#             print(f"Message '{message}' sent to queue '{queue_name}'")

#             # Close the channel and connection
#             channel.close()
#             connection.close()
#             break

#         except pika.exceptions.AMQPConnectionError as e:
#             print(f"AMQPConnectionError: {e}")
#             print("Attempting to reconnect in 5 seconds...")
#             time.sleep(5)



# def setup_consumer(queue_name):
#     while True:
#         try:
#             # Establish connection
#             connection = pika.BlockingConnection(connection_params)
#             channel = connection.channel()
#             channel.queue_declare(queue=queue_name)

#             # Start consuming messages
#             for method_frame, properties, body in channel.consume(queue_name):
#                 if body:
#                     print(f"Received message: {body.decode('utf-8')}")
#                     # Acknowledge the message
#                     channel.basic_ack(method_frame.delivery_tag)
#                 else:
#                     print("No more messages in the queue.")
#                     break

#             # Close the channel and connection
#             channel.close()
#             connection.close()

#         except pika.exceptions.AMQPConnectionError as e:
#             print(f"AMQPConnectionError: {e}")
#             print("Attempting to reconnect in 5 seconds...")
#             time.sleep(5)


@api.get("/hello")
def hello(request):
    # send_message('task_queue', "Hello World")
    
    # test = None
    # if cache.get("test"):
    #     test = cache.get("test")
    # else:
    #     cache.set("test", 1)
    logger.info("Hello Joe INFO")
    logger.error("Hello Joe ERROR")
    return "Hello world test"


# setup_consumer('task_queue')
