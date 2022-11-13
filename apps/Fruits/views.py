import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from .models import FruitsModel
from .forms import FruitsForm
# Create your views here.
 
class Inicio(TemplateView):
    template_name='presentacion.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)

class Fruits(View):  
    model=FruitsModel
    template_name= 'Fruits/listar_frutas.html'
    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        queryset= FruitsModel.objects.all 
        contexto = {
            'nombre':queryset
        }
         
        datos={'message':"Success"} 
        return render(request,self.template_name,contexto)

    def post(self,request): 
        jd= json.loads(request.body) 
        FruitsModel.objects.create(nombre=jd['nombre'])
    
        datos= {'message':"Successxx"}
        return JsonResponse(datos)  
    
def listar_frutas(request):
    return render(request,'Fruits/listar_frutas.html')

 