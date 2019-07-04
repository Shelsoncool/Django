from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItem
from django.shortcuts import redirect
# Create your views here.

def todoView(request):
    #return HttpResponse('Hello world')
    all_item=TodoItem.objects.all()
    return render(request,'todo/todo.html',{'all_item':all_item})

def addTodo(request):
    #c=request.POST['content']
    c = request.POST.get('content')
    newItem=TodoItem(content=c)
    newItem.save()
    return HttpResponseRedirect('todo/')
    #return redirect('todo/')

def deleteTodo(request, todo_id):
    delitem=TodoItem.objects.get(id=todo_id)
    delitem.delete()
    return HttpResponseRedirect('todo/')
    #return redirect('todo/')
