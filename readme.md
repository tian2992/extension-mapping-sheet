## Install

install curl:

> apt-get install curl

set up virtual environment:

> python3 -m venv .ve

activate virtual environment:

> source .ve/bin/activate

install ocdskit from source (in order to get [this commit](https://github.com/open-contracting/ocdskit/commit/c1cd50ab16593f10afe1149bedd86e896643d537)):

> pip install https://github.com/open-contracting/ocdskit/archive/master.zip

install requirements:

> pip install -r requirements.txt

## Run

> bash extension-mapping-sheet.bash

results in:

> extension-mapping-sheet.csv