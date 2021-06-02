from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import DdxForm,UpdownForm
from .models import Ddxlist,Firstddxlist,Secondddxlist,Thirdddxlist


class BtDdxView(TemplateView):

  def __init__(self):
    ddxdata = Ddxlist.objects.all()
    self.params = {
      'title':'Lets Ddx!',
      'message':'ddx list',
      'form':DdxForm(),
      'ddxdata':ddxdata,
      'secondform':UpdownForm(),
     
    }
  
  def get(self,request):
    return render(request,'hello_ddx/index.html',self.params)

  def post(self,request):
    bt_ch = request.POST['bt_choice']
    status_ch = request.POST['status_choice']
    status_message = ''
    if status_ch == "up":
      selected_bt = Ddxlist.objects.filter(bt_category = bt_ch).filter(true_up = True)
      status_message = '上昇'
    elif status_ch == "down":
      selected_bt = Ddxlist.objects.filter(bt_category = bt_ch).filter(true_up = False)
      status_message = '低下'
    self.params['ddxdata'] = selected_bt
    self.params['result'] = '結果:('+bt_ch+status_message+')'
    self.params['form'] = DdxForm(request.POST)
    self.params['secondform'] = UpdownForm(request.POST)
  
    
    return render(request,'hello_ddx/index.html',self.params)



# Create your views here.
