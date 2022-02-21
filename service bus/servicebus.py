from azure.servicebus import ServiceBusClient, ServiceBusMessage

CONNECTION_STR = "Endpoint=sb://my-servicebus-namespace-aruni.servicebus.windows.net/;SharedAccessKeyName=mypolicy;SharedAccessKey=MHo2rDAEoZVoZJBSzP2BCWKxv5mS6X44YW+pt0scnl4=;EntityPath=my-queue"
QUEUE_NAME = "my-queue"

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

        # Sending a list of messages
        messages = [ServiceBusMessage("First message-list1"), ServiceBusMessage("Second message-list2")]
        sender.send_messages(messages)

print("Done sending messages")
print("-----------------------")

with servicebus_client:
    receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME, max_wait_time=1, receive_mode="peeklock")
    with receiver:
        for msg in receiver:
            print("Received: " + str(msg))

            """complete_message will delete the message
            applicable for receive_mode="peeklock", since "receiveanddelete" will delete the message immediately.
            """
            #receiver.complete_message(msg)