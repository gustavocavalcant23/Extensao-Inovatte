import os

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Subscriber
from core.utils import send_email_brevo  


@receiver(post_save, sender=Subscriber)
def welcome_regards(sender, instance, created, **kwargs):
    if not created:
        return  

    subject = "Email Subject"
    html_content = f"""
        <h2>Email Content</h2>
    """

    send_email_brevo(
        to_email=instance.email,
        subject=subject,
        html_content=html_content,
        sender_email=os.getenv('EMAIL_HOST_USER'),  
        sender_name="Your Name"
    )
