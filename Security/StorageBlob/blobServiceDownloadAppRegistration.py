import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, __version__
from azure.identity import ClientSecretCredential

tenant_id = '21cf2068-16a1-412e-8383-0ec993073e05'
client_id = '408e2a9f-6e32-4b26-a6b0-0e58cca8513c'
client_secret = 'P_R7Q~.OwroKJvmxtGEPyFql-W~PNor1ZYm95'

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    token_credential  = ClientSecretCredential(tenant_id, client_id, client_secret)
    blob_service_client = BlobServiceClient(account_url='https://mystorageaccountaaruni.blob.core.windows.net', credential=token_credential)
   

    # name for the container
    container_name = 'mycontainer'

    # Create a file in the local data directory to upload and download
    local_file_name = 'sample.txt'

    # Create a blob client using the local file name as the name for the blob
    #blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    # OR blob_client can be create directly without the blob_service_client
    blob_client = BlobClient(account_url='https://mystorageaccountaaruni.blob.core.windows.net', container_name=container_name, blob_name=local_file_name, credential=token_credential)
    

    download_file_path = str(uuid.uuid4()) + "_downloaded.txt"
    print("\nDownloading blob to \n\t" + download_file_path)

    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

except Exception as ex:
    print('Exception:')
    print(ex)