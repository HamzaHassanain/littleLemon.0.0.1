# Little Lemon Project First Edition

### Little Lemon is a fictional company for the Meta Backend- Developer Track

## Installation

### 0- Prerequisites

- Python 3.x.x installed on your machine
- MySQL installed on your machine

### 1- Clone the repository

```bash

git clone https://github.com/HamzaHassanain/LittleLemon.0.0.1.git

cd LittleLemon.0.0.1

```

### 2- Install dependencies

if you do not have virtualenv installed, you can follow this [link](https://virtualenv.pypa.io/en/latest/installation.html) to install it.

- Create a virtual environment

  ```bash
  python3 -m venv venv
  ```

- Activate the virtual environment

  ```bash
    source venv/bin/activate
  ```

  Note: if you are using windows, you can activate the virtual environment by running the following command:

  ```bash
    venv\Scripts\activate
  ```

- Install the dependencies

  ```bash
    pip install -r requirements.txt
  ```

3- Create a database

- Create a database in MySQL

```bash
mysql -u root -p
```

- Then enter your password

```bash
CREATE DATABASE littlelemon;

exit
```

3- Go to the LittleLemon.0.0.1/littlelemon/settings.py file and change the database settings

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # change from sqlite3 to mysql
        'NAME' : 'littleLemon', # The name of the database you created
        'USER' : 'root', # The name of user
        "PASSWORD":"root", # the users password
        "HOST":"localhost",
        "PORT":"3306"
    }
}
```

4- Run the migrations

- Make Sure you are in the root directory of the project

```bash
python manage.py makemigrations

python manage.py migrate

```

5- Create a superuser

```bash
python manage.py createsuperuser
```

- Enter your username, email and password

6- Run the server

```bash
python manage.py runserver
```
