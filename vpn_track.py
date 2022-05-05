import requests
import json
from pyfiglet import Figlet
from clint.textui import colored



banner = Figlet(font='slant')
print(colored.red(banner.renderText("VPN Info")))

ip = "12.12.12.0"

api = "https://vpnapi.io/api/"

data = requests.get(api+ip+"?key={api_key}")

try:
    if data.status_code == 200:
             
            json_data = json.loads(data.text)
            
            ip_addr = json_data['ip']
            print("target ip is " , ip_addr ,"\n")

            details = json_data['security']
            print('vpn     : %s' % details['vpn'])
            print('proxy   : %s' % details['proxy'])
            print('tor     : %s' % details['tor'])
            print('relay   : %s' % details['relay'],"\n")

            network = json_data['network']
            print('network : %s' % network['network'])
            print('autonomous_system_number : %s' % network['autonomous_system_number'])
            print('autonomous_system_organization : %s' % network['autonomous_system_organization'],"\n")


            location = json_data['location']
            print('country    : %s' % location['country'])
            print('country_code   : %s' % location['country_code'])
            print('continent     : %s' % location['continent'])
            print('time_zone   : %s' % location['time_zone'])
            print('latitude   : %s' % location['latitude'])
            print('longitude   : %s' % location['longitude'])
            print('region_code   : %s' % location['region_code'])
            print('is_in_european_union : %s ' %location['is_in_european_union'])
        

    else:
        print("network issuse or not a vaild ip")

except:

    error = json.loads(data.text)

    print("error : %s" % error['message'])