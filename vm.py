from azure.mgmt.compute import ComputeManagementClient
compute_client = ComputerManagementClient(credentail , subscription_id)

compute_client.virtual_machine.begin_create_or_update(
    RGname , 
    "myosname1",
    {
        "location" : "westus2",
        "storage_profile" : {
            "image_reference":{
                "publisher" : "canonical",
                "offer" : "UbuntuServer",
                "version" : "latest",
            }
        }

        "hardware_profile" : {
            "vm_size": "standarad_D2s_v3"
        },
        
        
    }
    
)
