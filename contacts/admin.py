from django.contrib import admin, messages

from .models import UserContact

# Register your models here.

@admin.register(UserContact)
class UserContactAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email', 'phone')
    list_display = ('subject', 'name', 'phone', 'replied')
    list_filter = ('replied', )
    actions = ['mark_contact_as_read']


    @admin.action(description='Marcar como lida')
    def mark_contact_as_read(self, request, queryset):
        contacts = queryset

        if not contacts:
            self.message_user(request=request, message='Nenhum contato encontrado...', level=messages.WARNING)
            return
        
        for contact in contacts:
            if contact.replied:
                self.message_user(request=request, message=f'O contato {contact}, já foi respondido e será ignorado.', level=messages.INFO)
                continue

            try:
                contact.replied = True
                contact.save()

                self.message_user(request=request, message=f'O contato {contact}, foi marcado como respondido.', level=messages.SUCCESS)
                continue
            
            except Exception as e:
                self.message_user(request=request, message=f'Erro no momento de marcar a mensagem {contact}, como respondida.Erro: {e}', level=messages.ERROR)
                return