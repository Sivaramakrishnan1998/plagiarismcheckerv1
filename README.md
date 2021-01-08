# Plagiarism Checker

Plagiarism Checking  is the process of locating instances of plagiarism within a work or document. The widespread use of computers and the advent of the Internet has made it easier to plagiarize the work of others. Most cases of plagiarism are found in academia, where documents are typically essays or reports. However, plagiarism can be found in virtually any field, including novels, scientific papers, art designs, and source code.



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
python 3
virtualenv
easy_install or pip

install requirements.txt file
```

### Installing

A step by step procedure to get a development env running

Installing the virtualenv

```
sudo apt-get update
sudo apt-get install virtualenv
```
Creating the virtualenv in linux

```
python3 -m virtualenv venv
cd venv
source bin/activate
```

Creating the virtualenv in Windows

```
python3 -m virtualenv venv
cd venv/Scripts
activate
```

Installing the requirements.txt file
```
pip install -r requirements.txt
pip freeze
```

To run the server type the command

 ```
python manage.py makamigrations
python manage.py migrate
python manage.py runserver
 ```
## Built With

* [Django](https://docs.djangoproject.com/en/2.0/) - The web development framework used
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Scraping data from web
* [Nltk](http://www.nltk.org/) - Natural Language Processing



