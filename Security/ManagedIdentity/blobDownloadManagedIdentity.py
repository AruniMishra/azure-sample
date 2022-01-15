import os, uuid
from azure.storage.blob import BlobClient, __version__
from azure.identity import DefaultAzureCredential


try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    token_credential = DefaultAzureCredential()

    # name for the container
    container_name = 'mycontainer'

    # Create a file in the local data directory to upload and download
    local_file_name = 'sample.txt'

    # OR blob_client can be create directly without the blob_service_client
    blob_client = BlobClient(account_url='https://mystorageaccountaaruni.blob.core.windows.net', container_name=container_name, blob_name=local_file_name, credential=token_credential)
    

    download_file_path = str(uuid.uuid4()) + "_downloaded.txt"
    print("\nDownloading blob to \n\t" + download_file_path)

    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

except Exception as ex:
    print('Exception:')
    print(ex)