
## PYTHONPATH

```bash
# check pythonpath
dir env:PYTHONPATH

```


## VENV

```bash
# env in src folder
python -m venv .env 

```

## Setup ENV

```bash
# command prompt
set ENV=dev
echo %ENV%
echo %PYTHONPATH%

# power shell 
$env:ENV='dev'
dir env:

# pip install "python-dotenv[cli]"
dotenv list
dotenv --help

# set value
dotenv set ENV dev

# get value
dotenv get ENV

# unset key
dotenv unset ENV

# another source 
dotenv -f .env.dev list
```


## pip package manager

```bash
# show update status
pip list --outdated

# update
pip install <package_name> -U
python.exe -m pip install --upgrade pip

# update all
# windows
pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}

```