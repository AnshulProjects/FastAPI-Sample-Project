# FastAPI Sample Project

This is a sample project using [FastAPI](https://fastapi.tiangolo.com/), a modern web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Features
- FastAPI for API development
- Pydantic for data validation
- Asynchronous request handling


## Installation

#### Prerequisites
- Python 3.7+
- pip package manager


##### Project Structure
```bash
FastAPI-Sample-Project/
│── main.py #execution file is here          
│── Models/
│   ├── models.py # All pydantic models are located here       
│── api/
│   ├── endpoints/
│   │   ├── main_router.py # All API routes are located here
│── requirements.txt  # Dependencies list
│── README.md         # Documentation

```

###### How to get started

## 1. Create and activate a Python virtual environment
```sh
python3 -m venv env
source env/bin/activate
```
## 2 . Download all dependencies
```sh
pip install -r requirements.txt
```

## 3 . Run FastAPI server
```sh
cd src
fastapi run main.py
```





