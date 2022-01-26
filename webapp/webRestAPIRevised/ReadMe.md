# command

```bash
python -m pip install Django djangorestframework

django-admin startproject countryapi .

python manage.py startapp countries

python manage.py makemigrations

```

add the requirement.txt

run below from root folder:  
> az webapp up

## misc

az postgres up --resource-group DjangoPostgres-tutorial-rg --location centralus --sku-name B_Gen5_1 --server-name postgres-server-name --database-name pollsdb --admin-user mishra --admin-password passAwsd123!! --ssl-enforcement Enabled
or via Portal

run below cmd from django code folder
>az webapp up --resource-group my-rg --location westeurope --plan DjangoPostgres-tutorial-plan --sku B1 --name djangoapparuni

if we create Postgres server via the Posrtal the default Databse is postgres, so first login and create a new DB pollsdb

>az postgres server firewall-rule create --resource-group my-rg --server postgres-server-name --name AllowMyIP --start-ip-address 20.86.238.157 --end-ip-address 20.86.238.157

```bash
psql --host=postgres-server-name.postgres.database.azure.com --port=5432 --username=mishra@postgres-server-name --dbname=postgres
```

az webapp config appsettings set --settings DBHOST="postgres-server-name" DBUSER="mishra" DBPASS="Consopage13!" DBNAME="country"

<https://docs.microsoft.com/en-us/azure/postgresql/quickstart-create-server-database-portal>
