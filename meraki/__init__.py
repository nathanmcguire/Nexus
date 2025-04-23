API_KEY = "1df4924a544c228edfdf36135d5e3ea0b1ce54f7"  # demo read-only API key
import meraki
from pprint import pprint
dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.organizations.getOrganizations()
pprint(response)