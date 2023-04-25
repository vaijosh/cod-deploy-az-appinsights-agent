## Deploying Recipe
1. Modify ```configure_appinsightsagent_recipie.sh``` and change the CONNECTION_STRING
2. Recipe downloads applicationinsights agent and config files using curl command. 
3. Depending on the DMZ policies, upload these artifacts at appropriate place and change the curl command accordingly 
4. Upload the recipe in to COD shared resources.
5. Create any HBase node and verify that applicationinsights artifacts are present in 
directory /var/lib/hbase/appinsights
6. Verify that metrics are pushed into application insights workspace from the newly deployed node.