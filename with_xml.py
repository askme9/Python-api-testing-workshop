import requests
import xml.etree.ElementTree as et

def test_xml():
    response = requests.get("https://parabank.parasoft.com/parabank/services/bank/customers/12212")
# parse the response content using fromstring and convert the result to xml
    xml = et.ElementTree(et.fromstring(response.content))
    assert xml.getroot().tag == 'customer'
    assert xml.find('id').text=='12212'
    address = xml.findall('.//address/*')
    for i in range(0,len(address)):
        print(address[i].text)
    assert xml.find('phoneNumber').text=='310-447-4121'
    assert xml.find('ssn').text=='622-11-9999'
