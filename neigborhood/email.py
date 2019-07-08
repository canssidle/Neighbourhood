from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import notifications,Profile


def send_priority_email(name,receiver,title,message,author,neighbourhood):
 
    subject = title
    sender = 'canssidlewairimu@gmail.com'

  
    text_content = render_to_string('email/email.txt',{"name":name,"title":title,"message":message,"author":author,"neighbourhood":neighbourhood})
    html_content = render_to_string('email/email.html',{"name":name,"title":title,"message":message,"author":author,"neighbourhood":neighbourhood})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
