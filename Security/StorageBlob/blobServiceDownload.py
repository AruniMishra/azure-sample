import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

CONNECTION_STR = "DefaultEndpointsProtocol=https;AccountName=mystorageaccountaaruni;AccountKey=bTbSffdRyNPSaSXKSs2GPpGX8lQw5HnQIP8/RPw6Acp3T2eNCkCnQrtGNaQO35wMdvJrYf7KzmsPZdsaVSmhWw==;EndpointSuffix=core.windows.net"

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STR)

    # name for the container
    container_name = 'mycontainer'

    # Create a file in the local data directory to upload and download
    local_file_name = "sample.txt"

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    download_file_path = str(uuid.uuid4()) + "_downloaded.txt"
    print("\nDownloading blob to \n\t" + download_file_path)

    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

except Exception as ex:
    print('Exception:')
    print(ex)