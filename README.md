# vending_machin_swarm

## Create virtual env

https://docs.python.org/3/library/venv.html

```cmd
python -m venv .\tu_carpeta
```

## Activate env

```cmd
env\Scripts\Activate.ps1
```

## Dowload required libraries for the project

```cmd
pip install -r requirements.txt
```

## Update required libraries for the project

```cmd
pip freeze > requirements.txt
```

# Project Structure

`__pycache__/`: Compiled code for python. Do not change anything here.

`env/`: Virtual environment. Do not change anything here.

`Models/`: Only define entyties. No logic here.

`Repository/`: Database access logic. No bussiness logic here.

`Controllers/`: Bussiness logic here. What to we do before saving data to db?

# Running the project

## Server

```bash
uvicorn main:app --host 0.0.0.0 --port 7777 --reload
```
## Vending Machine

```bash
python VendingMachine.py
```
