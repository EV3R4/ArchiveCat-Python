# ArchiveCat-Python
![GitHub](https://img.shields.io/github/license/EV3R4/ArchiveCat-Python)
![GitHub repo size](https://img.shields.io/github/repo-size/EV3R4/ArchiveCat-Python)
![Zero dependencies](https://img.shields.io/badge/dependencies-0-success)
## Official Python translation of ArchiveCat

ArchiveCat will clone and pull starred git repositories.

## Installation
* Install [Python](https://www.python.org/)
* Clone the repository with `git clone https://github.com/EV3R4/ArchiveCat-Python.git`

## Setup
### Config
You can copy this template into "config.json" and replace the values.
```json
{
    "github": {
        "username": "<insert your username here>"
    }
}
```
Additionally you can add the following lines after "github" if you want to ignore projects
```json
"ignore": [
    "<insert projects to ignore here>"
]
```

## Executing ArchiveCat-Python
Run `python main.py` in a cmd of your choice
