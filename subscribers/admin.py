from django.contrib import admin
from datetime import date

from .models import Subscriber

# Register your models here.

class AgeRangeFilter(admin.SimpleListFilter):
    title = 'Faixa Etária'
    parameter_name = 'age_range'

    def lookups(self, request, model_admin):
        return [
            ('under_18', 'Menores de 18'),
            ('18_25', '18 a 25'),
            ('26_35', '26 a 35'),
            ('36_45', '36 a 45'),
            ('46_60', '46 a 60'),
            ('60_plus', '60+'),
        ]

    def queryset(self, request, queryset):
        today = date.today()
        value = self.value()

        if value == 'under_18':
            min_birth = date(today.year - 18, today.month, today.day)
            return queryset.filter(birth_date__gt=min_birth)

        elif value == '18_25':
            max_birth = date(today.year - 18, today.month, today.day)
            min_birth = date(today.year - 26, today.month, today.day)
            return queryset.filter(birth_date__range=(min_birth, max_birth))

        elif value == '26_35':
            max_birth = date(today.year - 26, today.month, today.day)
            min_birth = date(today.year - 36, today.month, today.day)
            return queryset.filter(birth_date__range=(min_birth, max_birth))

        elif value == '36_45':
            max_birth = date(today.year - 36, today.month, today.day)
            min_birth = date(today.year - 46, today.month, today.day)
            return queryset.filter(birth_date__range=(min_birth, max_birth))

        elif value == '46_60':
            max_birth = date(today.year - 46, today.month, today.day)
            min_birth = date(today.year - 60, today.month, today.day)
            return queryset.filter(birth_date__range=(min_birth, max_birth))

        elif value == '60_plus':
            max_birth = date(today.year - 60, today.month, today.day)
            return queryset.filter(birth_date__lt=max_birth)

        return queryset


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'email', )
    list_display = ('full_name', 'email', 'professional_area', 'age')
    list_filter = ('gender', 'professional_area', AgeRangeFilter)