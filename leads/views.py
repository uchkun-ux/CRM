from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models
from .forms import *

# Create your views here.
def leads_lists(request):
    leads = models.Lead.objects.all()
    context = {
        "leads": leads
        

    }
    return render(request, "leads_lists.html", context)

def lead_detail(request, pk):
    # print(pk)
    lead = get_object_or_404(models.Lead, id=pk)
    context = {
        "lead": lead}
    # print(lead)
    return render(request, 'details.html', context)

def lead_create(request):
    print(request.POST)
    context = {
        'forms': Leadform()
    }
    return render(request, "create.html", context)