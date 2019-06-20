from django.shortcuts import render, HttpResponse, redirect
from .models import user
from django.contrib import messages
def index(request):
    context = {
        'users' : user.objects.all()
    }
    return render(request, "tv_show_app/page1.html", context)

def display_page2(request):
    return render(request,"tv_show_app/page2.html")

def create(request):
    errors = user.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect ('/shows/new')
    else:
        user.objects.create( title = request.POST['title'], network = request.POST['network'], release_date = request.POST['release_date'], desc = request.POST['desc'])
        user_id = user.objects.last().id
        return redirect ('shows/'+ str(user_id))

def display_page3(request, user_id):
    context = {
        'user' : user.objects.get(id=user_id)
    }
    return render(request,"tv_show_app/page3.html", context)

def display_page4(request, user_id):
    context = {
        'user' : user.objects.get(id=user_id)
    }
    return render(request, "tv_show_app/page4.html",context)

def edit_info(request, user_id):
    errors = user.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect ('/edit/' + str(user_id))
    else:
        update = user.objects.get(id=1)
        print(update.title)
        update.title = request.POST['title']
        update.network = request.POST['network']
        update.release_date = request.POST['release_date']
        update.desc = request.POST['desc']
        update.save()

    return redirect ('/shows/' + str(user_id))


def delete(request, user_id):
    destroy = user.objects.get(id=user_id)
    destroy.delete()
    return redirect('/shows')

# Complete each of the following routes:
#  /shows/new- GET - method should return a template containing the form for adding a new TV show
#  /shows/create - POST - method should add the show to the database, then redirect to /shows/<id>
#  /shows/<id> - GET - method should return a template that displays the specific show's information
#  /shows - GET - method should return a template that displays all the shows in a table
#  /shows/<id>/edit - GET - method should return a template that displays a form for editing the TV show with the id specified in the url
#  /shows/<id>/update - POST - method should update the specific show in the database, then redirect to /shows/<id>
#  /shows/<id>/destroy - POST - method should delete the show with the specified id from the database, then redirect to /shows
#  Have your root route redirect to /shows
