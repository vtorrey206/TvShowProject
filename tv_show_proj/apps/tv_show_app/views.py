from django.shortcuts import render, HttpResponse, redirect
from .models import Shows
from django.contrib import messages

#All shows page MAIN page this is rendering a html page!!!!!!!!

def shows(request):
    context = {
        "show" : Shows.objects.all()
    }
    return render (request, 'tv_show_app/shows.html', context)

#Create a new show This is rendering a html page!!!!!!!!!!!!!!!!!

def new(request):
     
    return render(request, 'tv_show_app/new.html')

#PROCESS route for creating a new book    

def create(request):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        add_title = Shows.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['release_date'], desc = request.POST['desc'])
        print(add_title)
        return redirect(f"/shows/{add_title.id}")

#Default information page This is rendering a html page!!!!!!!!!!!!!!!!!

def info(request, id):
    context = {
      "show" : Shows.objects.get(id=int(id)),
    }
    return render(request, 'tv_show_app/info.html', context)

#UPDATE method

def edit(request, id):
    context = {
    "show" : Shows.objects.get(id=int(id)),
    }
    return render(request, 'tv_show_app/edit.html', context)

#Process method for updateing information

def update(request, id):
    show = Shows.objects.get(id=int(id))
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show.id}/edit')
    else:
        show = Shows.objects.get(id=int(id))
        show.title = (request.POST['title']),
        show.network = (request.POST['network'])
        show.release_date = (request.POST['release_date'])
        show.desc = (request.POST['desc'])
        show.save()
        return redirect(f'/shows/{show.id}')

#Process route for deleteing shows
def delete (request, id):
      
      show = Shows.objects.get(id=int(id))
      show.delete()
      return redirect('/shows')

