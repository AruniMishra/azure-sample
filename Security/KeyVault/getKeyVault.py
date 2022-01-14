from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

tenant_id = '21cf2068-16a1-412e-8383-0ec993073e05'
client_id = '408e2a9f-6e32-4b26-a6b0-0e58cca8513c'
client_secret = 'P_R7Q~.OwroKJvmxtGEPyFql-W~PNor1ZYm95'

keyvault_url = 'https://mykeyvaultaruni.vault.azure.net/'
secret_name = 'mysecret'

token_credential  = ClientSecretCredential(tenant_id, client_id, client_secret)

client = SecretClient(vault_url=keyvault_url, credential=token_credential)


# keyVaultName = input("Input a name for your KeyVault > ")
# secretName = input("Input a name for your secret > ")

keyVaultName = 'myKeyVaultaruni'
secretName = 'mysecret'

print(f"Retrieving your secret from {keyVaultName}.")

retrieved_secret = client.get_secret(secretName)

print(f"Your secret is '{retrieved_secret.value}'.")