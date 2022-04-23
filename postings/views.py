import json, re

from django.shortcuts import render
from django.views     import View
from django.http      import JsonResponse
from users.models     import User
from postings.models  import Posting, Image, Comment, Like
from json.decoder     import JSONDecodeError
from users.decorator  import log_in_decorator

class PostingView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user           = User.objects.get(email=data.get('user', None))
            content        = data.get('content', None)
            image_url_list = data.get('image_url', None)

            if not (user and image_url_list):
                return JsonResponse({'message':'KEY_ERROR'}, status=400)
              
            posting = Posting.objects.create(
                user    = user,
                content = content
                )

            for image_url in image_url_list:
                Image.objects.create(
                    image_url = image_url,
                    posting   = posting
                )
                
            return JsonResponse({'message':'SUCCESS'}, status=200)
        
        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)

    def get(self, request):
        posting_list = [{
            "username"  : User.objects.get(id=posting.user.id).username,
            "content"   : posting.content,
            "image_url" : [i.image_url for i in Image.objects.filter(posting_id=posting.id)],
            "create_at" : posting.created_at
            } for posting in Posting.objects.all()
        ]

        return JsonResponse({'data':posting_list}, status=200)

class PostingSearchView(View):
    def get(self, request, user_id):
        if not User.objects.filter(id=user_id).exists():
            return JsonResponse({'message':'USER_DOES_NOT_EXIST'}, status=404)

        posting_list = [{
            "username"  : User.objects.get(id=user_id).username,
            "content"   : posting.content,
            "image_url" : [i.image_url for i in Image.objects.filter(posting_id=posting.id)],
            "create_at" : posting.created_at
            } for posting in Posting.objects.filter(user_id=user_id)
            ]

        return JsonResponse({'data':posting_list}, status=200)

class CommentView(View):
    @log_in_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            content    = data.get('content', None)
            posting_id = data.get('posting_id', None)

            if not (content and posting_id):
                return JsonResponse({'message':'KEY_ERROR'}, status=400)

            if not Posting.objects.filter(id=posting_id).exists():
                return JsonResponse({'message':"POSTING_DOES_NOT_EXIST"}, status=404)

            posting = Posting.objects.get(id=posting_id)

            Comment.objects.create(
                content = content,
                user    = user,
                posting = posting
            )

            return JsonResponse({'message':'SUCCESS'}, status=200)
        
        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)

class CommentSearchView(View):
    def get(self, request, posting_id):
        if not Posting.objects.filter(id=posting_id).exists():
            return JsonResponse({'message':'POSTING_DOES_NOT_EXIST'}, status=404)

        comment_list = [{
            "username"  : User.objects.get(id=comment.user.id).username,
            "content"   : comment.content,
            "create_at" : comment.created_at
            } for comment in Comment.objects.filter(posting_id=posting_id)
        ]

        return JsonResponse({'data':comment_list}, status=200)

class LikeView(View):
    @log_in_decorator
    def post(self, request):
        try :
            data = json.loads(request.body)
            user = request.user

            posting_id = data.get('posting_id', None)

            if not posting_id:
                return JsonResponse({'message':'KEY_ERROR'}, status=400)

            if not Posting.objects.filter(id=posting_id).exists():
                return JsonResponse({'message':"POSTING_DOES_NOT_EXIST"}, status=404)
            
            posting = Posting.objects.get(id=posting_id)

            if Like.objects.filter(user=user, posting=posting).exists():
                Like.objects.filter(user=user, posting=posting).delete()
                like_count = Like.objects.filter(posting=posting).count()
                return JsonResponse({'message': 'SUCCESS', 'like_count':like_count}, status=200)

            Like.objects.create(
                user    = user,
                posting = posting
            )
            like_count = Like.objects.filter(posting=posting).count()
            return JsonResponse({'message': 'SUCCESS', 'like_count': like_count}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)
