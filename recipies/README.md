## Deploying Recipe
1. Modify file ```config_appinsightsagent_regionserver``` change the CONNECTION_STRING according 
to the actual connection string in the customer environment.
2. Recipe downloads applicationinsights agent and config files using curl command. 
So depending on the DMZ policies, put these artifacts at appropriate place and change the curl command in 
the script accordingly. 
3. Go to```Cloudera Management console/Shared Resources/Recipes``` click on ```Register Recipe``` and 
register recipe with propert name and script we modifed in step #2. Node down the mae you enter on the UI for 
the recipe.
4. Go to the Datahub UI and associate recipe we registered above to the worker group.

## Testing the changes 
1. Simulate autoscaling scenario using ```update-database``` command e.g. 
```cdp.sh opdb update-database --environment-name vj-cod-7216-az --database-name vj-cod-7216 --auto-scaling-parameters '{"maxWorkersForDatabase":10,"minWorkersForDatabase":3}'```
2. Login to newly created node and verify that application insights agent and config files are placed in directory /var/lib/hbase/appinsights/regionserver
3. Verify that agent is able to push metrics to application insights workspace.