from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection, transaction
from django.http import HttpResponse
from django.utils import timezone
from django.views import generic
from .models import SysLog, Customer
#from .forms import ShipClassForm
import inspect
from inspect import currentframe, getframeinfo

# Create your views here.
class SysLogView(generic.ListView):
    model = SysLog

def log_detail(request, logid):
    log = get_object_or_404(SysLog, logid=logid)
    return render(request, 'ClockApp/log_detail.html', {'log': log})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'ClockApp/customer_list.html', {'customers': customers})
