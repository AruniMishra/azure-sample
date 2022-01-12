import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://myeventhubnsaruni.servicebus.windows.net/;SharedAccessKeyName=root;SharedAccessKey=Uph1lDhCrjE5Hm6YMy7P6cZ7MOL1K/gVSFiiJjNiVY0=;EntityPath=appeventhub", eventhub_name="appeventhub")
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData('First event '))
        event_data_batch.add(EventData('Second event'))
        event_data_batch.add(EventData('Third event'))

        event_data = EventData('Message with properties')
        event_data.properties = {'prop_key': 'prop_value'}
        event_data_batch.add(event_data)

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)
        print("done")

loop = asyncio.get_event_loop()
loop.run_until_complete(run())