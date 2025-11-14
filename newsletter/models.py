from django.db import models

# Create your models here.

class NewsLetterMessage(models.Model):
    title = models.CharField(verbose_name='Título', max_length=255)
    content = models.TextField(verbose_name='Conteúdo', max_length=10000)
    sent = models.BooleanField(verbose_name='Enviado', default=False)
    scheduled_date = models.DateField(verbose_name='Data agendada')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta: 
        ordering = ['-scheduled_date']
        verbose_name = 'Conteúdo da NewsLetter'
        verbose_name_plural = 'Conteúdos da NewsLetter'
