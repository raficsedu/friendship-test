# Friendship Test Calculator

Any user can create a friendship-test by answering 10 random questions. The questions and their corresponding answers are predefined and provided by the application. The user gets the link to the created test and can share it with friends. A friend is asked exactly the same questions and gets the percentage of matching answers after submitting the form.


## Install
First clone this project into your machine/pc. This project can be run into both **Docker** and **Virtual Environment**

### Docker
1. Clone the project with ..
    ```
    git clone https://github.com/raficsedu/friendship-test.git
    ```
2. Install ***Docker*** and ***Dcoker Composer*** from their official web site based on your machine OS.
3. Create a .env file in the directory where the settings.py file resides and chage the database name, user and pass according to your choice.

    ```
    SECRET_KEY=django-insecure-th+0qr)afx__0_&&)477mpoo6wmy87-!7i!ba@s&5!x#&86yw&
    DEBUG=True
    DATABASE_NAME=friendship_test_db
    DATABASE_USERNAME=postgres
    DATABASE_PASSWORD=@CYLINRAf45
    DATABASE_HOST=db
    DATABASE_PORT=5432
    ```
    Use the same DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD value in docker-compose.yml file in db service under environment section.
    ```
    environment:  
      - POSTGRES_USER=postgres  
      - POSTGRES_PASSWORD=@CYLINRAf45  
      - POSTGRES_DB=friendship_test_db
    ```
4. Go to the project directory and run ...
    ```
    1. sudo docker-compose up --build -d
    ```
5. Migrate all the migration files and seed ...
    ```
    sudo docker-compose run web python setup_and_seed.py
    ```

Now open up your browser and navigate to http://127.0.0.1:8000.


### Virtual Environment
1. Clone the project with ..
    ```
    git clone https://github.com/raficsedu/friendship-test.git
    ```
2. Install ***Virtual Environment*** using pip.
3. Create a .env file in the directory where the settings.py file resides and chage the database name, user and pass according to your choice. Create the database in your machine Postgresql.

    ```
    SECRET_KEY=django-insecure-th+0qr)afx__0_&&)477mpoo6wmy87-!7i!ba@s&5!x#&86yw&
    DEBUG=True
    DATABASE_NAME=friendship_test_db
    DATABASE_USERNAME=postgres
    DATABASE_PASSWORD=@CYLINRAf45
    DATABASE_HOST=127.0.0.1
    DATABASE_PORT=5432
    ```
4. Go to the project directory and run ..
    ```
    1. source env/bin/activate
    2. pip install -r requirements.txt
    3. python setup_and_seed.py
    4. python manage.py runserver
    ```

Now open up your browser and navigate to http://127.0.0.1:8000.

## Automatic Test

For running all the automatic test cases, run the following commands. You must need to be inside virtual environment or into docker container.
```
1. python manage.py test
```
