<<Instagram_Clone_Coding_Practice>>

# requirements
- Homebrew
- MacOS M1

# 1. Django initial setting

## 1) Virtual Environments

   ### a) (python ver = 3.9)
   ### b) conda create -n instagram_clone python=3.9
   ### c) conda activate instagram_clone

## 2) Create Database

   ### a) brew install MySQL (have to install Homebrew before)
   ### b) mysql> CREATE DATABASE instagram CHARACTER SET utf8mb4_general_ci;
   ### c) mysql> exit;

## 3) Project initial settings

   ### a) project repository clone (if have to be with others, but not at this project)
   ### b) project python package install (at Virtual Environment)
- pip install django
- pip install mysqlclient
- pip install django-cors-headers
   ### c) Django project settings
- git branch feature/-(branch name) (not at this project)
- git checkout feature/-
- django-admin startproject instagram_clone(project name)
- cd instagram_clone
   ### d) beginning development environment settings (settings.py)
- allow ip
  -> ALLOWED_HOSTS = ['*'] (if you want to allow specific person or group, U have to type that host name) (['*'] means allow local host only)

# 2. Modeling

# 3. Signup

# 4. Login

# 5. Encryption

# 6. Access_token(JWT)

# 7. Postings

# 8. Comments
