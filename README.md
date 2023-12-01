# About This Project
This project is a collection of applications written in Python using the Flask framework. 

# Quick Start
* Python 3.8 is required.
* Run the following commands:
```
pip install -r requirements.txt
python WebApp.py
```
* Open http://127.0.0.1:8080 in a web browser.

# Project Structure
Some notes about the files and directories found in the repository

## Azure DevOps and Ansible
```
.
├── ansible/
│   ├── playbooks/
│   ├── roles/
│   ├── vars/
│   └── inv
├── ansible.cfg
└── pipeline.yml
```
* Azure DevOps is used for the project's CI/CD. The pipeline tasks are found in the `pipeline.yml` file.
* It uses Ansible to deploy to a target server. All of the relevant playbooks, roles, variables, and inventory are found in the `ansible/` directory
* The configuration file for Ansible is found in `ansible.cfg`

## Applications
```
.
├── commonlib/
│   ├── functions.py
│   └── initproperties.py
├── foobar/
│   └── hello.py
├── nsinfo/
│   └── trips.py
├── tests/
│   └── test_commonlib.py
├── WebApp.ini
├── WebApp.py
└── requirements.txt
```
* `commonlib`: contains files that can be used across different applications
* `foobar`: a placeholder application
* `nsinfo`: uses the NS API to retrieve train schedules and more
* `tests`: for unit testing
* `WebApp.ini`: configuration file for the main Flask application
* `WebApp.py`: main Flask application
* `requirements.txt`: all the required Python modules 

## Running Tests
Run `pytest` on project directory path

# Footnotes
* [tree.nathanfriend.io](https://tree.nathanfriend.io/)