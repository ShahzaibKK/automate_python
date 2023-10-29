import json, pprint

str_json_data = '{"name": "gulabu","age": 26,"tel": null,"hobbies": ["fucking", "and more fucking"],"sex": "love pussies"}'
json_data_as_python_value = json.loads(str_json_data)
pprint.pprint(json_data_as_python_value)

loaded_json = json.dumps(json_data_as_python_value)
print(loaded_json)
