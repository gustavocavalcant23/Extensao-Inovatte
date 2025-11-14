import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import UserContact
from core.utils import send_email_brevo  


@receiver(post_save, sender=UserContact)
def contact_post_save(sender, instance, created, **kwargs):
    if not created:
        return

    # E-mail para o cliente
    welcome_subject = 'Email Subject'
    welcome_html = f"""
    <h3>Email Content</h3>
    """

    send_email_brevo(
        to_email=instance.email,
        subject=welcome_subject,
        html_content=welcome_html,
        sender_email=os.getenv('EMAIL_HOST_USER'),  
        sender_name="Your Name"
    )

    # E-mail para os admins
    admins = User.objects.filter(is_superuser=True, email__isnull=False).exclude(email='')
    admin_subject = 'Email Subject'
    admin_html = f"""
    <h3>Email Content</h3>
    """

    for admin in admins:
        send_email_brevo(
            to_email=admin.email,
            subject=admin_subject,
            html_content=admin_html,
            sender_email=os.getenv('EMAIL_HOST_USER'),
            sender_name="Your Name"
        )