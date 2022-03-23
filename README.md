# About the application

This is a Django based app wherein the admin can log-in and perform CRUD (create, read, update, and delete) operations on articles, whereas the visitors can only read articles. Internationalization is implemented to translate in English and German language.


## Requirements

Python 3.8  
Django 4.0.3

## Setting up the Project

  * Download and install Python 3.8
  * Download and install Git.
  * Fork the Repository.
  * Clone the repository to your local machine `$ git clone https://github.com/mbilal117/articles.git`
  * Change directory to articles `$ cd articles`
  * Create a virtual environment and install all requirements from Pipfile `$ virtualenv -p python3 venv`  
  * Activate the venv: `$ source venv/bin/activate`
  * Install required packages `$ pip install -r requirements.txt `
  * Make migrations `$ python manage.py makemigrations`
  * rename .env_local file under articles folder to .env and replace database credentials
  * Migrate the changes to the database `$ python manage.py migrate`
  * Create superuser `$ python manage.py createsuperuser`
  * Run the server `$ python manage.py runserver`