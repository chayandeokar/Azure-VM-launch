# login into azure account
from azure.identity import DefaultAzureCredential
credentail = DefaultAzureCredential()

# provide your subsciption id
subscription_id = 
from azure.mgmt.resource import ResourceManagementClient
resource_client = ResourceManagementCLient(credentail , subscription_id)

RGname = "chayandeokar"

# create Resource Group with name and location 
rg_result = resource_client.resource_group.create_or_update(
    RGname , { "location" : "westus2" }
)
