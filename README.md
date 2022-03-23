# About the application

This is a Django based app wherein the admin can log-in and perform CRUD (create, read, update, and delete) operations on articles, whereas the visitors can only
create and read articles. Internationalization is implemented to translate in English and German language.

## Installing and executing the app

```
> git clone https://github.com/mbilal117/articles.git
> cd articles
> pip install -r requirements.txt
> python manage.py migrate
> python manage.py runserver
```