from django.shortcuts import render, redirect, reverse
# from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from .forms import *
import leads

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = NewUserForm
    
    def get_success_url(self):
        return reverse('leads:listlar')

class HomeView(TemplateView):
    template_name = "home.html"

class ListsView(LoginRequiredMixin, ListView):
    template_name = "leads_lists.html"
    queryset = models.Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "details.html"
    queryset = models.Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/create.html"
    form_class = LeadModelForm

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/update.html"
    form_class = LeadModelForm
    queryset = models.Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:listlar')


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/delete.html"
    form_class = LeadModelForm
    queryset = models.Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:listlar')


# def home(request):
#     return render(request, "home.html")
# class HomeView(TemplateView):
#     template_name = "home.html"

# def leads_lists(request):
#     leads = models.Lead.objects.all()
#     context = {
#         "leads": leads
#     }
#     return render(request, "leads_lists.html", context)

# def lead_detail(request, pk):
#     lead = get_object_or_404(models.Lead, id=pk)
#     context = {
#         "lead": lead
#     }
#     return render(request, 'details.html', context)

# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/leads')
#     context = {
#         'forms': form
#     }
#     return render(request, "create.html", context)

def lead_update(request, pk):
    lead = models.Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {
        'lead': lead, 
        'form': form
    }
    return render(request, "update.html", context)
    
# def lead_delete(request, pk):
#     lead = models.Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")