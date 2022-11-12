# Run

run:

```bash
func host start
```

- update local.settings.json: update connection string for myservicebusnamespacearuni_SERVICEBUS

## to run from portal

- deploy first to portal, and create myservicebusnamespacearuni_SERVICEBUS in configuration.
- create "myqueue" and set it to "myqueue" (queue) name

Publishing to Azure:
func azure functionapp publish <APP_NAME>
<https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Cazurecli-linux%2Capplication-level#folder-structure>

Or,
az functionapp deployment source config-zip -g <resource_group> -n \
<app_name> --src <zip_file_path>
<https://docs.microsoft.com/en-us/azure/azure-functions/deployment-zip-push#cli>

OR,
Ymal deployment:
<https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops?tabs=nodejs%2Cyaml%2Cpython>
