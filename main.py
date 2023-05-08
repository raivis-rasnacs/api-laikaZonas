from requests import get, post
from pprint import pprint

url = "https://www.timeapi.io/api/TimeZone/AvailableTimeZones"
visasLaikaZonas = get(url)

#pprint(visasLaikaZonas.json())
#print(len(visasLaikaZonas.json()))
for i, zona in enumerate(visasLaikaZonas.json()):
    print(i, zona)

url_conversion = "https://www.timeapi.io/api/Conversion/ConvertTimeZone"
#req = post(url, json={"fromTimeZone":visasLaikaZonas.json()[0], "dateTime":"2023-05-08 13:45:22", "toTimeZone":})