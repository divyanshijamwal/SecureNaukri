from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   
    return render(request, "home.html")
def job_detail(request):
    return render(request, "job_detail.html")
def explore(request):
    return render(request, "explore.html")
def companies(request):
    return render(request, "companies.html")
def about(request):
    return render(request, "about_us.html")
def contact(request):
    return render(request, "contact.html")
def employer(request):
    return render(request, "employer_form.html")
def login(request):
    return render(request, "login.html")
def signup(request):
    return render(request, "signup_form.html")
def privacy(request):
    return render(request, "privacy_policy.html")
def jobpostingrules (request):
    return render(request, "job_posting_rules.html")
def reset(request):
    return render(request, "password_reset.html")
def manage(request):
    return render(request, "manage_account.html")
def jobpost(request, post):
    return HttpResponse(post)
    