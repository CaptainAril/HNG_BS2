# HNG-backend: Stage two

This repo is my submission for the HNG Internship (backend track) stage two task.

The project is a simple REST API capable of CRUD operations on a `Person` resource. The project interfaces with MySQL database.


# Installation and run commands

## Python version
- 3.10.7

Ensure you have this version of python, or something close (3.8.x +) on your system
***
## Clone this repository into your local machine to be able to test this Project.

## Set up and run Virtual Environment
In the root directory, run the following commands:
- `python3 -m venv venv`
- `source venv/bin/activate` (for Linux or mac)
- `./venv/Scripts/activate`  (for windows)

## Install Dependencies in virtual env
- `pip3 install -r requirements.txt`

## Setup MySQL Database
Create a MySQL database on your local machine. Tables are automatically created.
In the root directory, create a `.env` file containing MySQL database credential as environment variables

> MYSQL_USER=`user`

> MYSQL_PWD=`user password`

> MYSQL_DB=`database name`

> MYSQL_HOST=`localhost`
* The project will interface with the database on the default port - 3306

## Run the server
`python3 -m api.v1.app`
This starts a flask app at `http://127.0.0.1:8000/`.

Refer to [`DOCUMENTATION.md`](https://github.com/CaptainAril/HNG_BS2/blob/main/DOCUMENTATION.md) for API endpoints and usage.
