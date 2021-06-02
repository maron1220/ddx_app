from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import DdxForm
from .models import Ddxlist,Firstddxlist,Secondddxlist,Thirdddxlist

class BtDdxView(TemplateView):

  def __init__(self):
    ddxdata = Ddxlist.objects.all()
    self.params = {
      'title':'Lets Ddx!',
      'message':'ddx list',
      'form':DdxForm(),
      'ddxdata':ddxdata,
    }
  
  def get(self,request):
    return render(request,'hello_ddx/index.html',self.params)

  def post(self,request):
    bt_ch = request.POST['bt_choice']
    selected_bt = Ddxlist.objects.filter(bt_category = bt_ch)
    self.params['ddxdata'] = selected_bt
    self.params['result'] = bt_ch
    self.params['form'] = DdxForm(request.POST)
    
    return render(request,'hello_ddx/index.html',self.params)



# Create your views here.
