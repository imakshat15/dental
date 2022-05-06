from django.urls import path
from website.views import home,contact,blog,blogdetails,pricing,service,about

urlpatterns =[
   path('',home,name='home'),
   path('contact.html/',contact,name='contact'),
   path('blog.html/',blog,name='blog'),
   path('blog-details.html/',blogdetails,name='blogdetails'),
   path('pricing.html/',pricing,name='pricing'),
   path('service.html/',service,name='service'),
   path('about.html/',about,name='about'),
   
]