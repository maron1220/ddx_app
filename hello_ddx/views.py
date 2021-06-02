from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import DdxForm

class BtDdxView(TemplateView):

  def __init__(self):
    self.params = {
      'title':'Lets Ddx!',
      'message':'ddx list',
      'form':DdxForm(),
    }
  
  def get(self,request):
    return render(request,'hello_ddx/index.html',self.params)

  def post(self,request):
    msg = request.POST['name']+'('+request.POST['age']+')'
    self.params['message'] = msg
    self.params['form'] = DdxForm(request.POST)
    return render(request,'hello_ddx/index.html',self.params)



# Create your views here.
