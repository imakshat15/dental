from email import message
from wsgiref.util import request_uri
from django.shortcuts import render
from django.core.mail import send_mail
def  home(request):
    return render(request,'website/home.html')

def contact(request):
    if request.method=='POST':
        # form ki info extract krrna 
        message_name=request.POST['message-name']
        message_email=request.POST['message-email']
        message=request.POST['message']
  
  # send mail
        send_mail=(
            message_name,#who sent
            message,#message
            message_email,#from email
            ['akshatshrivastava71@gmail.com'],#to email
        )
        return render(request,"website/contact.html",{'message_name':message_name})
    else:

       return render(request,'website/contact.html')
    
def blog(request):
        return render(request,'website/blog.html')

def blogdetails(request):
        return render(request,'website/blog-details.html')

def pricing(request):
        return render(request,'website/pricing.html')
def service(request):
        return render(request,'website/service.html')
def about(request):
       return render(request,'website/about.html')