from azure.mgmt.compute import ComputeManagementClient
compute_client = ComputerManagementClient(credentail , subscription_id)


from azure.mgmt.network import NetworkManagementClient
Network_client = NetworkManagementClient(credentail , subscription_id)

VNET_NAME = "python-example-vnet"
SUBNET_NAME = "python-example-subnet"
IP_NAME = "python-example-ip"
IP_CONFIG_NAME = "python-example-ip-config"
NIC_NAME = "python-example-nic"

poller = network_client.virtual_networks.begin_create_or_update(
    RGname,
    VNET_NAME,
    {
        "location": "westus2",
        "address_space": {"address_prefixes": ["10.0.0.0/16"]},
    },
)


network_client.public_ip_addresses.begin_create_or_update(
    RESOURCE_GROUP_NAME,
    IP_NAME,
    {
        "location": "westus2",
        "sku": {"name": "Standard"},
        "public_ip_allocation_method": "Static",
        "public_ip_address_version": "IPV4",
    },
)

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
