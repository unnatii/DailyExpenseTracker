# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
#from django.template import loader
from .models import Expenses
from .forms import ExpensesForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import ListView,CreateView,UpdateView
#from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Sum

@login_required
def index(request):
    current_user = auth.get_user(request)
    if request.method == 'POST':
        expenses_list=Expenses.objects.filter(usr=current_user)
        return render(request,'tracker/index.html',{ 'expenses_list':expenses_list})
    else:
        expenses_list=Expenses.objects.filter(usr=current_user)
        context={ 'expenses_list':expenses_list,}
        return render(request,'tracker/index.html',context)
        
        
class PostListView(LoginRequiredMixin,ListView):
    model=Expenses 
    template_name='tracker/list.html'
    context_object_name='expenses_list'   
    ordering=['-date'] 
    #@method_decorator(login_required)  
    def get_queryset(self):
           return Expenses.objects.filter(usr=self.request.user) 
        
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Expenses 
    template_name='tracker/Home.html'

    fields=["name","amount","exp_type"]
   # @method_decorator(login_required)  
    def form_valid(self,form):
        form.instance.usr=self.request.user
        form.save()
        return super(PostCreateView, self).form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model=Expenses 
    template_name='tracker/Home.html'

    fields=["name","amount","exp_type"]
   # @method_decorator(login_required)  
    def form_valid(self,form):
        form.instance.usr=self.request.user
        form.save()
        return super(PostUpdateView, self).form_valid(form)    
        
        
@login_required    
def Home(request):
    current_user = auth.get_user(request)
    if request.method == 'POST' :
        name=request.POST.get('name')
        amount=request.POST.get('amount')
        etype=request.POST.get('etype')
        s=Expenses(name=name,amount=amount,exp_type=etype)
        s.save()
        return redirect('index')
    else:
   
        return render(request,'tracker/Home.html')
   # sum = Expenses.objects.filter(usr=current_user).aggregate(Sum('amount'))
        
    
@login_required       
def delete(request,expense_id):
    exp=Expenses.objects.get(pk=expense_id)
    exp.delete()
    return redirect('index')

@login_required       
def total(request):
    current_user = auth.get_user(request)
    sum = Expenses.objects.filter(usr=current_user).aggregate(Sum('amount'))
    return render(request,'tracker/total.html',{'sum':sum})  
                

          
    
    
