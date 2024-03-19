import xml.etree.ElementTree as ET

# Assume you have an XML file named 'sites.xml'
tree = ET.parse('sites.xml')
root = tree.getroot()

# Now you can iterate over the elements as shown previously
for site in root.findall('site'):
    url = site.find('url').text
    # continue with your logic
import requests
from bs4 import BeautifulSoup  # or from lxml import html

for site in root.findall('site'):
    url = site.find('url').text
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')  # or html.fromstring(response.content)
        for dp in [dp.text for dp in site if dp.tag.startswith('dataPoint')]:
            data = soup.select_one(dp)  # For CSS selectors
            # Or use soup.xpath(dp) if you're using lxml with XPaths
            print(data.text if data else "Data point not found")
