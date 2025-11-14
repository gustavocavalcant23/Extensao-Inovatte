import os

from django.contrib import admin, messages

from core.utils import send_email_brevo
from .models import NewsLetterMessage
from subscribers.models import Subscriber

# Register your models here.

@admin.register(NewsLetterMessage)
class NewsLetterAdmin(admin.ModelAdmin):
    search_fields = ('schedule_date', 'title')
    list_display = ('title', 'scheduled_date', 'status')
    list_filter = ('sent', )
    actions = ['send_message']


    @admin.display(description='Status')
    def status(self, obj):
        return "✅ Enviada" if obj.sent else "❌ Pendente"


    @admin.action(description='Enviar agora')
    def send_message(self, request, queryset):
        subscribers = Subscriber.objects.all()
        recipient_list = [subs.email for subs in subscribers]

        if not recipient_list:
            self.message_user(request=request, message='Nenhum inscrito encontrado...', level=messages.WARNING)
            return
        
        for newsletter in queryset:
            if newsletter.sent:
                self.message_user(request=request, message='A NewsLetter selecionada já foi enviada e será ignorada.', level=messages.WARNING)
                continue

            try:
                for email in recipient_list:
                    send_email_brevo(
                        to_email=email,
                        subject=newsletter.title,
                        html_content=newsletter.content,
                        sender_email=os.getenv('EMAIL_HOST_USER'),
                        sender_name='Your Name'
                    )

                newsletter.sent = True
                newsletter.save()

                self.message_user(request=request, message=f'NewsLetter enviada com sucesso para {len(recipient_list)} inscritos', level=messages.SUCCESS)

            except Exception as e:
                self.message_user(request=request, message=f'Erro ao enviar a NewsLetter. Erro: {e}', level=messages.ERROR)
            
            
        


