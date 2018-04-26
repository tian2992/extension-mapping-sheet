#temporary directory
mkdir extension_schemas

#get latest release schema
curl "http://standard.open-contracting.org/latest/en/release-schema.json" > release-schema.json

#activate virtualenv
source .ve/bin/activate

#flatten core schema
cat release-schema.json | ocdskit mapping-sheet > release-schema-flat.csv

#fetch extension schemas and create patched versions of core schema
python3 fetch_extension_schemas.py release-schema.json ../extension_registry/extensions.json

#flatten patched schemas
for file in extension_schemas/*
do
	cat "$file" | ocdskit mapping-sheet > "$file.csv"
done

#diff patched and core flattened schemas
python3 extension_mapping_sheet.py release-schema-flat.csv

rm -r extension_schemas