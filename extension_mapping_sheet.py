import glob
import sys
import pprint

file_list = glob.glob("extension_schemas/*.csv")

core_schema_path = sys.argv[1]

core_schema = open(core_schema_path, "r")

core = core_schema.readlines()

for file in file_list:
	extension_schema = open(file, "r")
	extension = extension_schema.readlines()
	with open("extension-mapping-sheet.csv", "a") as fp:
		for line in extension:
			if line not in core:
				fp.write(file.split("/")[1].split(".")[0]+","+line)
