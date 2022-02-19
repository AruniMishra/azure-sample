azureaduser=$(az ad user list --filter "userPrincipalName eq 'sqluser'" --query [].objectId --output tsv)


az sql server ad-admin create --resource-group my-rg --server-name 'my-sql-server-aruni' --display-name ADMIN --object-id 0582230b-5696-45ae-8d86-d0242bfd60a5



sqlcmd -S 'my-sql-server-aruni.database.windows.net' -d 'my-sql-db' -U 'sqluser@arunimishramsitgmail.onmicrosoft.com' -P "Hofstad!" -G -l 30

Hofstad!


sqluser is only used to login and to run below cmd


CREATE USER [my-sql-uai] FROM EXTERNAL PROVIDER;
ALTER ROLE db_datareader ADD MEMBER [my-sql-uai];
ALTER ROLE db_datawriter ADD MEMBER [my-sql-uai];
ALTER ROLE db_ddladmin ADD MEMBER [my-sql-uai];
GO