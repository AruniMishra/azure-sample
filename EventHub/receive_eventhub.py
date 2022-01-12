import asyncio
from azure.eventhub.aio import EventHubConsumerClient


async def on_event(partition_context, event):
    # Print the event data.
    print("Received the event: \"{}\" from the partition with ID: \"{}\" and sequence number: \"{}\"".format(event.body_as_str(encoding='UTF-8'), partition_context.partition_id, event.sequence_number))

    # Update the checkpoint so that the program doesn't read the events
    # that it has already read when you run it next time.
    await partition_context.update_checkpoint(event)

async def main():
    # Create an Azure blob checkpoint store to store the checkpoints.
    # checkpoint_store = BlobCheckpointStore.from_connection_string("AZURE STORAGE CONNECTION STRING", "BLOB CONTAINER NAME")

    # Create a consumer client for the event hub.
    client = EventHubConsumerClient.from_connection_string("Endpoint=sb://myeventhubnsaruni.servicebus.windows.net/;SharedAccessKeyName=root;SharedAccessKey=Uph1lDhCrjE5Hm6YMy7P6cZ7MOL1K/gVSFiiJjNiVY0=;EntityPath=appeventhub", consumer_group="$Default", eventhub_name="appeventhub")
    async with client:
        # Call the receive method. Read from the beginning of the partition (starting_position: "-1")
        await client.receive(on_event=on_event,  starting_position="-1")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Run the main method.
    loop.run_until_complete(main())