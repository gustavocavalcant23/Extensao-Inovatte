import os
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException



def send_email_brevo(to_email, subject, html_content, sender_email=None, sender_name=None):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = os.getenv("API_KEY_BREVO")

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    default_sender = os.getenv('EMAIL_HOST_USER')

    if not sender_email:
        sender_email = default_sender
    if not sender_name:
        sender_name = "Your Name"

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": to_email}],
        sender={"email": sender_email, "name": sender_name},
        subject=subject,
        html_content=html_content
    )

    try:
        response = api_instance.send_transac_email(send_smtp_email)
        return response
    except ApiException as e:
        print(f"Erro ao enviar e-mail: {e}")
        return None
