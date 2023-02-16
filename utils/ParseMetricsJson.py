import json

f = open("utils/HbaseMetrics.json")

inputJson = json.load(f)

keysToSkip = {'description', 'modelerType', 'tag.Context', 'tag.Hostname', 'name'}

outputJson = []
for i in inputJson:
  objectName = i['name']
  for key in i:
    if key not in keysToSkip:
      attribute = key
      data = {}
      data['objectName'] = objectName
      data['attribute'] = attribute
      if isinstance(i[key], dict):
        data['name'] = i[key]['description']
        outputJson.append(data)
print(outputJson)
