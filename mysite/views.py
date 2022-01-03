# from django.core.checks import messages
from django.shortcuts import render
from django.http import HttpResponse
from mysite import models

def index(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all() 
    return render(request,'index.html',locals())


# def index(request, pid=None, del_pass=None):
#     posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
#     moods = models.Mood.objects.all()
#     try:
#         urid = request.GET['user_id']
#         urpass = request.GET['user_pass']
#         se_byear = request.GET['user_post']
#         urfcolor = request.GET('mood')
#     except:
#         urid = None
#         messages = '如果要張貼訊息,則每一個欄位都要填寫'

#     if del_pass and pid:
#         try:
#             post = models.Post.objects.get(id=pid)
#         except:
#             post = None
#         if post:
#             if post.del_pass == del_pass:
#                 post.delete()
#                 message = '資料刪除成功'
#             else:
#                 message = '密碼錯誤'
#     else user_id != None:
#     # if urid != is not None:
#         moods = models.Mood.objects.get(status=user_mood)
#         post = models.Post.objects.create(mood=mood,nickname=user_id, del_pass=user_pass,message=user_post)
#         post.save()
#         message='成功儲存!請記得編輯密碼[{}]!'.format(user_pass)
        
#     return render(request, 'index.html',locals())



# def listing(request):
#     posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
#     moods = models.Mood.objects.all()
#     return render(request, 'index.html',locals())
#     try:
#         user_id = request.POST['user_id']
#         user_pass = request.POST['user_pass']
#         user_post = request.POST['user_post']
#         user_mood = request.POST('mood')
#     except:
#         urid_id = None
#         messages = '如果要張貼訊息,則每一個欄位都要填寫'

#     if user_id is not None:
#         moods = models.Mood.objects.get(status=user_mood)
#         post = models.Post.objects.create(mood=mood,nickname=user_id, del_pass=user_pass,message=user_post)
#         post.save()
#         message='成功儲存!請記得編輯密碼[{}]!'.format(user_pass)
        
#     return render(request, 'index.html',locals())
