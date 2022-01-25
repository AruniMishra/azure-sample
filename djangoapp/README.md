---
services: app-service\web,app-service
platforms: python
author: cephalin
---

# Django and PostgreSQL sample for Azure App Service

This samples is a simple Django app that connects to a PostgreSQL database. The sample is used with the following tutorials:

- [Deploy a Django web app with PostgreSQL in Azure App Service (Azure CLI)](https://docs.microsoft.com/azure/app-service/containers/tutorial-python-postgresql-app).
- [Deploy a Django web app with PostgreSQL using the Azure portal](https://docs.microsoft.com/en-us/azure/developer/python/tutorial-python-postgresql-app-portal).

When deployed to Azure App Service, the database connection information is specified via environment variables `DBHOST`, `DBPASS`, `DBUSER`, and `DBNAME`. This app always uses the default PostgreSQL port. See the tutorials for more information.

## Change log

- 27 Oct 2020: Possible breaking change: removed use of the `DJANGO_ENV` environment variable to switch between local and production settings. The code instead triggers the selection using the `WEBSITE_HOSTNAME` environment variable, which is defined when the code is running inside the the Azure App Service container. See manage.py and azuresite/wsgi.py.

- 12 Oct 2020: **BREAKING CHANGE**: The `DBHOST` environment variable is expected to contain *only* the server name, not the full URL, which is constructed at run time (see azuresite/production.py). Similarly, `DBUSER` is expected to contain only the user name, not username@servername as before, because using the simpler `DBHOST` the code can also construct the correct login form at run time (again in azuresite/production.py), avoiding failures that arise when `DBUSER` lacks the @servername portion.  

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

-----

## misc

az postgres up --resource-group DjangoPostgres-tutorial-rg --location centralus --sku-name B_Gen5_1 --server-name postgres-server-name --database-name pollsdb --admin-user mishra --admin-password passAwsd123!! --ssl-enforcement Enabled
or via Portal

run below cmd from django code folder
>az webapp up --resource-group my-rg --location westeurope --plan DjangoPostgres-tutorial-plan --sku B1 --name djangoapparuni

if we create Postgres server via the Posrtal the default Databse is postgres, so first login and create a new DB pollsdb
>az postgres server firewall-rule create --resource-group my-rg --server postgres-server-name --name AllowMyIP --start-ip-address 20.50.183.104 --end-ip-address 20.50.183.104
>psql --host=postgres-server-name.postgres.database.azure.com --port=5432 --username=mishra@postgres-server-name --dbname=postgres

az webapp config appsettings set --settings DBHOST="postgres-server-name" DBUSER="mishra" DBPASS="passAwsd123!!" DBNAME="pollsdb"
