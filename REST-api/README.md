# RESTFul
Using: `Flask (python framework)` + `MSSQL (SQL server)`.

### detailed look :

- `python 3.7.4`
    - `flask`
    - `flask-restful`
    - `flask-alchemy`
    - `pyodbc`
    - `flask-jwt-extended`
- `MSSQL`

# Project setup and execution (windows)

## 1. Installing SQL Server

Install SQL Server Developer edition ([Link](https://www.microsoft.com/en-in/sql-server/sql-server-downloads))
change the name of the server in run.py (now: YAMI)

## 2. Create the virtual environment 
```bash
virtualenv venv
venv\Scripts\activate.bat
```
## 3. Installing Packages

```bash
pip install -r requirements.txt
```

## 4. Run the application locally

```bash
set FLASK_APP=run.py 

python -m flask run # at: http://127.0.0.1:5000/

# to change port add: "--port=1337"
```