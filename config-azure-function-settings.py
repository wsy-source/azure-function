from azure.mgmt.web.v2022_03_01 import WebSiteManagementClient
from azure.mgmt.web.v2022_03_01.models import StringDictionary
from azure.identity import ClientSecretCredential, AzureAuthorityHosts

credential = ClientSecretCredential(
    tenant_id='1a6857ff-9169-4a8a-83bf-5de6129d38f6',
    client_id='01bf713f-2d84-4471-b729-66b1361c0ff5',
    client_secret='O7SotHf-Vk28R2-ohPLV4BSm~Gu-_i~48O',
    authority=AzureAuthorityHosts.AZURE_CHINA
)

site_management_client = WebSiteManagementClient(credential=credential, subscription_id='1204c64b-8557-4ee6-975f-c531df82f703',
                                 base_url='https://management.chinacloudapi.cn',
                                 credential_scopes=['https://management.core.chinacloudapi.cn/.default'])

job = site_management_client.web_apps.list_application_settings(resource_group_name='rg-viper-portal-dms-test', name='func-scale-node-test')
# job.properties's type is dict
job.properties['name']='wangwu'
config = StringDictionary(properties=job.properties)
site_management_client.web_apps.update_application_settings(resource_group_name='rg-viper-portal-dms-test', name='func-scale-node-test',app_settings=config)

