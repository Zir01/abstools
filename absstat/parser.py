import requests

def parse(url):
    """
    Calls ABS API to return an array of tuples
    
    Example:
    > parse(url to abs api)
    outputs resulting array of tuples containing the data
    """    
    r = requests.get(url)
    json_data = r.json()
    
    dataSets = json_data["dataSets"]
    dimensions = json_data["structure"]["dimensions"]["observation"]

    params = []
    for ds in dataSets:
        observations = ds["observations"]
        for key in observations:
            dim_ids_str = key.split(':')
            dim_ids = [int(numeric_string) for numeric_string in dim_ids_str]
            row_data = []
            for index, item in enumerate(dim_ids):
                dim_value = dimensions[index]["values"][item]["id"]
                if dim_value.isdigit():
                    dim_value = int(dim_value)
                row_data.append(dim_value)
            
            row_data.append(observations[key][0])
            tup = tuple(row_data)
            params.append(tup)
    
    return params
