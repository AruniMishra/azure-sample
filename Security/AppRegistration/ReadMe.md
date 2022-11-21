

az webapp auth microsoft update  -g my-rg --name myapparuni --allowed-audiences api://8700c85c-1e3f-446e-b873-ca6674d7fd77 --client-id 8700c85c-1e3f-446e-b873-ca6674d7fd77 --client-secret uvY8Q~N34vEZBZ8kqMLLQ2qbursq00OQDfh1Capi --issuer https://sts.windows.net/21cf2068-16a1-412e-8383-0ec993073e05/v2.0


az webapp auth  update --name myapparuni --resource-group my-rg  --set globalValidation.unauthenticatedClientAction=Return403 --enabled true