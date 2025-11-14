from django.db import models
from datetime import date

class Subscriber(models.Model):

    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Prefiro não especificar'),
    ]

    PROFESSIONAL_AREA_CHOICES = [
        ('AG', 'Agrônomo'),
        ('PR', 'Produtor Rural'),
        ('GE', 'Gestor(a) Empresarial'),
        ('SS', 'Profissional de SST'),
        ('ES', 'Estudante'),
        ('CO', 'Consultor(a)'),
        ('PE', 'Pesquisador(a)'),
        ('OU', 'Outro'),
    ]

    first_name = models.CharField(verbose_name='Nome', max_length=50)
    last_name = models.CharField(verbose_name='Sobrenome', max_length=50)
    email = models.EmailField(verbose_name='E-mail', unique=True)

    gender = models.CharField(
        verbose_name='Gênero',
        max_length=1,
        choices=GENDER_CHOICES,
        default='N'
    )

    birth_date = models.DateField(verbose_name='Data de nascimento')

    professional_area = models.CharField(
        verbose_name='Área profissional',
        max_length=2,
        choices=PROFESSIONAL_AREA_CHOICES,
        default='OU'
    )

    created_at = models.DateTimeField(verbose_name='Data de inscrição', auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
        return age
    
    class Meta:
        ordering = ['first_name']
        verbose_name = 'Assinante'
        verbose_name_plural = 'Assinantes'
