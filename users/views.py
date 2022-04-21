from django.shortcuts import render

# Create your views here.

import json, re, bcrypt, jwt

from django.http      import JsonResponse, HttpResponse
from django.views     import View
from my_settings      import SECRET_KEY
from users.models     import User
from users.validation import Validation
from django.core.exceptions import ValidationError
from django.conf            import settings

class SignUpView(View):
      def post(self, request):
          try:
              data         = json.loads(request.body)
              email        = data['email']
              password     = data['password']
              name         = data['name']
              phone_number = data['phone_number']

              Validation.email_validate(email)
              Validation.password_validate(password)

              if User.objects.filter(email=email).exists():
                  return JsonResponse({'message': 'ALREADY_EXISTS'}, status = 400)

              hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

              User.objects.create(
                  name         = name,
                  email        = email,
                  password     = hashed_password,
                  phone_number = phone_number
                  )
              return JsonResponse({'message': 'SUCCESS'}, status = 201)

          except KeyError:
              return JsonResponse({'message': 'KEY_ERROR'}, status = 400)
          except ValidationError as error:
              return JsonResponse({"message": error.message}, status=400)

class LoginView(View):
      def post(self, request):
          try:
              data     = json.loads(request.body)

              user = User.objects.get(email=data['email'])

              if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                 return JsonResponse({"message" : "INVALID_PASSWORD"}, status=401)

              access_token = jwt.encode({"id" : user.id}, settings.SECRET_KEY, algorithm = settings.ALGORITHM)

              return JsonResponse({
                  "message"      : "SUCCESS",
                  "access_token" : access_token
              }, status=200)

          except KeyError:
              return JsonResponse({'message': 'KEY_ERROR'}, status = 400)

          except ValueError:
              return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)

          except User.DoesNotExist:
              return JsonResponse({"message" : "INVALID_EMAIL"}, status=401)