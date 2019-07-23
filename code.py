import os 
import sys
import request
import yaml

mac_info = sys.argv[1]


def main()
    validate_input(mac_info)
    get_Host_data(mac_info)

def fetch_api_key():
    # Read YAML file
    with open("settings.yaml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded['apikey']['maddr']

def validate_input(mac_info):
    input_length=len(sys.argv)
    if(input_length == 2):
       print "\nCurrent MAC address is ", (sys.argv[1])
    else:
        print (" Enter correct MAC address (Example:  44:38:39:ff:ef:57")
        sys.exit()

def get_Host_data(mac_info)
    key=get_api_key()
    url = f"https://api.macaddress.io/v1?apiKey={key}&output=json&search={mac_info}"
    response = requests.get(url)
    #Writing output to file 
    outfile=open(Productdetails.json,"w")
    outfile.write(response)
    outfile.close

    output=response.json()
    
    company=output["vendorDetails"]["companyName"]
    print( "Here is the company name")
    print(company)


main()