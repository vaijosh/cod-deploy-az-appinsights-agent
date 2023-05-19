## Deploying Recipe
1. Modify ```config_appinsightsagent_master``` and ```config_appinsightsagent_regionserver``` change the CONNECTION_STRING
2. Recipe downloads applicationinsights agent and config files using curl command. 
3. Depending on the DMZ policies, upload these artifacts at appropriate place and change the curl command accordingly 
4. Add recipe to the cluster using steps in <https://cloudera.atlassian.net/wiki/spaces/ENG/pages/1456309002/RUNBOOK+Add+or+modify+a+recipe+for+existing+cluster`>
5. Create any HBase node and verify that applicationinsights artifacts are present in 
directory /var/lib/hbase/appinsights
6. Verify that metrics are pushed into application insights workspace from the newly deployed node.
