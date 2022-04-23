<Instagram_Clone_Coding_Practice>

# requirements
- Homebrew
- MacOS M1

# 1. Django initial setting

## 1) Virtual Environments

    ```python
     #(python ver = 3.9)
     conda create -n instagram_clone python=3.9
     conda activate instagram_clone
    ```

## 2) Create Database

    ```python
     brew install MySQL (have to install Homebrew before)
     mysql> CREATE DATABASE instagram CHARACTER SET utf8mb4_general_ci;
     mysql> exit;
    ```

## 3) Project initial settings

- a) project repository clone (if have to be with others, but not at this project)
- b) project python package install (at Virtual Environment)
    ```python
    pip install django
    pip install mysqlclient
    ```
- c) Django project settings
    ```python
    git branch feature/-(branch name) (not at this project)
    git checkout feature/-
    django-admin startproject instagram_clone(project name)
    cd instagram_clone
    ```
- d) beginning development environment settings (settings.py)
  
  -> allow ip 
    ```python
    [ALLOWED_HOSTS = ['*'] 
    (if you want to allow specific person or group, U have to type that host name) (['*'] means allow local host only)]
    ```

  -> annotation process 
    ```python
    INSTALLED_APPS = [
    #    'django.contrib.admin',
    #    'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages'
        'django.contrib.staticfiles',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
    #    'django.middleware.csrf.CsrfViewMiddleware',
    #    'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ```

  -> urls.py
   ```python
   from django.urls import path

   urlpatterns = [
   ]
   ```
  
  -> my_settings.py (DATABASES, SECRET KEY)
   ```python
   # cd instagram_clone (project name)
   touch my_settings.py
   ```
   ```python
   # vi my_settings.py
   # based on your environments
   DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql' ,
        'NAME': 'DATABASE name',
        'USER': 'DB user name',
        'PASSWORD': 'DB password',
        'HOST': '127.0.0.1', #local host
        'PORT': '3306', #almost PORT '3306'
     	'OPTIONS': {'charset': 'utf8mb4'}
        }
    }
        
   SECRET_KEY = '' #settings.py_secret_key'
   ```

  -> linked settings.py & my_settings.py
   ```python
   #settings.py
   from pathlib     import Path
   from my_settings import DATABASES, SECRET_KEY
   ...
   ...

   DATABASES = DATABASES
   SECRET_KEY = SECRET_KEY
   ```
  -> M1 mysql setting
   ```python
   pip install pyMySQL
   ```
   ```python
   #settings.py
   from pathlib        import Path
   from my_settings    import DATABASES, SECRET_KEY

   import pymysql

   pymysql.install_as_MySQLdb()

   ...
   INSTALLED_APPS = [
    ...
   'corsheaders'
   ]
   
   MIDDLEWARE = [
    ...
   'corsheaders.middleware.CorsMiddleware',
    ...
   ]

   #REMOVE_APPEND_SLASH_WARNING
   APPEND_SLASH = False

    ##CORS
    CORS_ORIGIN_ALLOW_ALL  =True
    CORS_ALLOW_CREDENTIALS = True
        
    CORS_ALLOW_METHODS = (
        'DELETE',
        'GET',
        'OPTIONS',
        'PATCH',
        'POST',
        'PUT',
    )
        
    CORS_ALLOW_HEADERS = (
        'accept',
        'accept-encoding',
        'authorization',
        'content-type',
        'dnt',
        'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',    		
    )
   ```
  
  -> requirements.txt
   ```python
    touch requirements.txt
    vi requirements.txt
    
    # requirements.txt
    # pip freeze
    Django==3.2.4
    django-cors-headers==3.7.0
    mysqlclient==2.0.3
        
    PyMySQL==1.0.2 # for M1
    ```

  -> .gitignore
    ```python
    # https://www.toptal.com/developers/gitignore
    # python, pycharm, VisualStudioCode, vim, macOS, Linux, zsh
    #touch .gitignore
    #vi .gitignore
                
    ############################
    # gitignore.io copy and paste #
    ############################
    my_settings.py # Confidential
    ```
  -> execute project server
    ```python
    # pwd with manage.py
    python manage.py runserver
    ```

## 4) Create Github Pull Request
- add & commit & Pull 
    ```python
    git checkout feature/branch name

    git add .
    git commit -m "commit message"
    
    git push origin feature/branch name
    ```

# 2. Modeling

## 1) Create User Branch
    ```python
     git checkout main #MUST create branch at main
     git branch feature/branch name
    ```

## 2) Create User App
    ```python
     python manage.py startapp users
    ```

## 3) Create User table
    ```python
     # models.py
     from django.db import models

     class User(models.Model):
      email = models.CharField(max_length=100, unique=True)
      password = models.CharField(max_length=200)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      class Meta:
          db_table = 'users'
    ```
    
# 3. Signup

# 4. Login

# 5. Encryption

# 6. Access_token(JWT)

# 7. Postings

# 8. Comments

