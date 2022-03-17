from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . import models
from . forms import *

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
        "lead": lead }
    # print(lead)
    return render(request, 'details.html', context)

def lead_create(request):
    forms = LeadModelForm()
    if request.method == "POST":
        # print('Successfully')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            # print("Information")
            # print(form.cleaned_data)
            # ismi = form.cleaned_data['ismi']
            # familiyasi = form.cleaned_data['familiyasi']
            # yoshi = form.cleaned_data['yoshi']
            # agent = models.Agent.objects.first()
            # models.Lead.objects.create(
            #     ismi=ismi,
            #     familiyasi=familiyasi,
            #     yoshi=yoshi,
            #     agent=agent
            # )
            # print("Success")
            return redirect('/leads')
    context = {
        'forms': forms
    }
    return render(request, "create.html", context)


def lead_update(request, pk):
    lead = models.Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        # print('Successfully')
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {
        'lead': lead,
        'form': form
        
    }
    return render(request, "update.html", context)


def lead_delete(request, pk):
    lead = models.Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
    