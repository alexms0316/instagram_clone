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

# 2. Modeling

# 3. Signup

# 4. Login

# 5. Encryption

# 6. Access_token(JWT)

# 7. Postings

# 8. Comments
