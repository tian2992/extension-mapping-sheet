import json
import json_merge_patch
from collections import OrderedDict
import sys
import urllib
import requests
import copy

core_schema_path = sys.argv[1]

extension_registry_path = sys.argv[2]

with open(core_schema_path) as core_schema_file:
	core_schema = json.load(core_schema_file, object_pairs_hook=OrderedDict)

with open(extension_registry_path) as extension_registry_file:
	extension_registry = json.load(extension_registry_file)

for extension in extension_registry["extensions"]:
	core_schema_copy = copy.deepcopy(core_schema)
	if extension["core"] == True:
		with urllib.request.urlopen(extension["url"]+"release-schema.json") as url:
			extension_schema = json.loads(url.read().decode(), object_pairs_hook=OrderedDict)
			extended_schema = json_merge_patch.merge(core_schema_copy, extension_schema)
			with open("extension_schemas/"+extension["slug"]+".json", "w") as fp:
				json.dump(extended_schema, fp, indent=4)
