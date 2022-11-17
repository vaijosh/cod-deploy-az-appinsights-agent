# cod-deploy-az-appinsights-agent
This is a simple ansible script to deploy the Azure Application insights agent for different Cloudera Operational Database Roles.

## Prerequisites
Ansible : Download and Setup Ansible as per instructions from https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
ssh access to all Hbase hosts

## How to setup up application insights agent
1. Create an Application Insights Workspace and note down the conncetions
2. Modify applicationinsights.json and copy "Connection String" recorded in step 2. Also in jmxMetrics section include the JMX metrics you want to monitor.
3. Modify the hosts file and add the hosts grouped by role names e.g. [master], [regionserver].<br />( Note: The same group name will appear as role name in metric and hostname will be used role instance )
4. Run the ansible script using command

    ```export ANSIBLE_HOST_KEY_CHECKING=False```
    
    ```ansible -i hosts -u cloudbreak --private-key ~/.ssh/odx-developers playbook.yml```
5. The applicationinsights jar file and config file will be deployed in /var/lib/hbase/appinsights/<rolename> directory.
6. From Cloudera Manager, got to Configurations for Hbase and search "java_opts", and for each role you want to monitor add the following jvm argument

    ```-javaagent:/var/lib/hbase/appinsights/<rolename>/applicationinsights-agent-3.4.4.jar```

7. Restart the roles.

## Hos to check ingested metrics
1. Login to your Azure portal and select the application insights workspace you had created.
2. Go to Metric section and select scope as your application insights workspace and metric:Namespace as azure:applicationinsights
3. You should be able to see your metrics in "Metrics" dropdown.

## How to create Alerts
1. Login to Azure portal portal.azure.com and select the application insights workspace you created.
2. Click on Create an alert rule
3. Select Custom log search, which should open KQL query editor
4. add followng query to filter metrics
    ```
      customMetrics
        | where cloud_RoleInstance == "<role instance>" and name == '<metric name>'
    ```
5. In preview panel you can see the search results for the query. Once the results are validated, click "Continue Editing Alert"
6. Set appropraite configurations for "Measurement", "Alert logic"
7. In "Actions" Tab select and "existing action group" or "create new action group" to define configuratons for notifications.
8. Complete the remaining steps for Alert creation and alerts will start firing once the specified conditions are met.


  
