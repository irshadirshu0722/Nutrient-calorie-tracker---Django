from django.shortcuts import render,redirect

from .models import Consume, Food

# Create your views here.

def index(request):

  
  if request.method == 'POST':
    food_consumed = request.POST.get('food_consumed')
    consume_ob = Food.objects.filter(name=food_consumed).first()
    Consume.objects.create(user=request.user,food_consumed=consume_ob)
  
  foods = Food.objects.all()
  user_food_consumed = Consume.objects.filter(user=request.user).all()
  return render(request,'myapp/index.html',{'foods':foods,"consumed_foods":user_food_consumed})

def delete_consume(request,id):
  
  consume = Consume.objects.filter(user = request.user,pk=id)
  if request.method == "POST":
    consume.delete()
    return redirect('/')
  return render(request,'myapp/delete.html')

