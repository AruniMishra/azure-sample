from azure.servicebus import ServiceBusClient, ServiceBusMessage

CONNECTION_STR = "Endpoint=sb://myservicebusnamespacearuni.servicebus.windows.net/;SharedAccessKeyName=mypolicy;SharedAccessKey=s/yRH6yOad2YliG9DHe3+MUJIRnz/67OY811EZRYe8A=;EntityPath=myqueue"
QUEUE_NAME = "myqueue"

def send_single_message(sender):
    # create a Service Bus message
    message = ServiceBusMessage("Single Message")
    # send the message to the queue
    sender.send_messages(message)
    print("Sent a single message")

# create a Service Bus client using the connection string
servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)
with servicebus_client:
    # get a Queue Sender object to send messages to the queue
    sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
    with sender:
        # send one message        
        send_single_message(sender)

print("Done sending messages")
print("-----------------------")

# with servicebus_client:
#     receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME, max_wait_time=5)
#     with receiver:
#         for msg in receiver:
#             print("Received: " + str(msg))
#             receiver.complete_message(msg)