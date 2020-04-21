# ArchiveCat-Python
## ArchiveCat will clone and pull starred git repositories.
### Official Python translation of ArchiveCat
![GitHub](https://img.shields.io/github/license/EV3R4/ArchiveCat-Python)
![GitHub repo size](https://img.shields.io/github/repo-size/EV3R4/ArchiveCat-Python)
![Zero dependencies](https://img.shields.io/badge/dependencies-0-success)

## Installation
* Install [Python](https://www.python.org/)
* Install [Git](https://git-scm.com/)
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

## Notes
If you are using Windows, you might need to use Git Bash
