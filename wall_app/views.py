from django.shortcuts import render,redirect,HttpResponse
from app_folder.models import *
from .models import *
from datetime import datetime,timedelta

def wall(request):
    user_id = request.session.get('user_id')
    now = datetime.now().replace(tzinfo=None)
    if user_id:
        for message in Message.objects.all():
            date = message.date.replace(tzinfo=None)
            time_limit = timedelta(minutes=30)
            if message.user.id == user_id and now - date < time_limit:
                message.deletable = True
                message.save()
            else:
                message.deletable = False
                message.save()
        for comment in Comment.objects.all():
            date = comment.date.replace(tzinfo=None)
            time_limit = timedelta(minutes=30)
            if comment.user.id == user_id and now - date < time_limit:
                comment.deletable = True
                comment.save()
            else:
                comment.deletable = False
                comment.save()
        context = {
            'user' : User.objects.get(id=user_id),
            'messages' : Message.objects.all().order_by("-id"),
            'comments' : Comment.objects.all(),
        }
        return render(request,"wall.html",context)
    else:
        return redirect('/')

def post_message(request):
    user_id = request.session['user_id']
    if user_id:
        user = User.objects.get(id=user_id)
        body = request.POST['message']
        Message.objects.create(body=body,user=user)
        return redirect('/wall')
    else:
        return redirect('/')

def post_comment(request,message_id):
    user_id = request.session['user_id']
    if user_id:
        user = User.objects.get(id=user_id)
        body = request.POST['comment']
        message = Message.objects.get(id=message_id)
        Comment.objects.create(body=body,user=user,message=message)
        return redirect('/wall')
    else:
        return redirect('/')

def delete_message(request,message_id):
    user_id = request.session['user_id']
    if user_id:
        message = Message.objects.get(id=message_id)
        if message.user.id == user_id:
            message.delete()
        return redirect('/wall')
    else:
        return redirect('/')

def delete_comment(request,comment_id):
    user_id = request.session['user_id']
    if user_id:
        comment = Comment.objects.get(id=comment_id)
        if comment.user.id == user_id:
            comment.delete()
        return redirect('/wall')
    else:
        return redirect('/')
