import json

fileopen = open('./sample.json5', 'r')
dict_json = json.load(fileopen)
dumped_dict = json.dumps(dict_json)

print(type(dict_json))
print(dict_json)
print(type(dumped_dict))
print(dumped_dict)

fileopen.close()
