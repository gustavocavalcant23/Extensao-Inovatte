from django.db import models

# Create your models here.


class UserContact(models.Model):

    SUBJECT_CHOICES = [
        ('AGN', 'Agronegócio'),
        ('GTE', 'Gestão Empresarial'),
        ('SST', 'Saúde e Segurança do Trabalho'),
        ('TRN', 'Treinamentos'),
        ('OTR', 'Outro'),
    ]

    name = models.CharField(verbose_name='Nome', max_length=50)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Telefone', max_length=20)
    subject = models.CharField(verbose_name='Assunto', choices=SUBJECT_CHOICES, default='OTR')
    text = models.TextField(verbose_name='Mensagem', max_length=1000)
    replied = models.BooleanField(verbose_name='Respondida', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject} - {self.name}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'