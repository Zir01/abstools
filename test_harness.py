"""
Simple test script
"""
from absstat import parser

# Get this url from the ABS.Stat website: http://stat.data.abs.gov.au/
# Export -> Developer API -> Generate API queries -> Copy/Paste into url below
abs_api_url = f'http://stat.data.abs.gov.au/sdmx-json/data/ABS_BA_SA2_ASGS2016/1.9.9.100+110.SA2.101021007.M/all?startTime=2019&endTime=2019&dimensionAtObservation=allDimensions'

# Make the call to the API
data_as_a_list_tuples = parser.parse(abs_api_url)
print(data_as_a_list_tuples)