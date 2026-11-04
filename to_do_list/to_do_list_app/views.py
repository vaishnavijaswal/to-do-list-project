from django.shortcuts import render ,redirect
from to_do_list_app.models import task
from django.http import HttpResponse




# Create your views here.
def home(request):
  task_data = task.objects.all()
  return render(request, 'home.html', {"tasks":task_data})


def add_task(request):
  return render(request, 'add_task.html')


def add_task_from(request):
  if request.method == "POST":
    title = request.POST.get('title')
    description = request.POST.get('description')
    if title and description:
      task.objects.create(title=title,description=description)
      return redirect('home')
    else :
      redirect('add_task')
      return HttpResponse(f"Fill all the feilds.")


def delete_task(request, id):
    delete_task = task.objects.get(id=id)
    delete_task.delete()


    return redirect('home')


def edit_task(request, id):
  task_data = task.objects.get(id=id)
  return render(request, 'edit_task.html' ,{'task_data':task_data}) 


def edit_task_form(request ,id):
  
  if request.method == "POST":


    title = request.POST.get('title')
    description = request.POST.get('description')
    if title and description:
      task.objects.filter(id=id).update(title = title , description= description)


      return redirect('home')


    else:
      return HttpResponse(f"Fill all the feilds")


  return redirect('home')


def toggle_task(request, id):


    if request.method == "POST":
        task_data = task.objects.get(id=id)
        task_data.completed = not task_data.completed
        task_data.save()


    return redirect('home')