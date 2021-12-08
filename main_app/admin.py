from django.contrib import admin
from main_app.models import Cities, ProgramLanguage, Vacancy


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', ]


@admin.register(ProgramLanguage)
class ProgramLanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', ]


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'language', 'city']
    search_fields = ['name', 'company', 'city', 'language']
    list_filter = ['city', 'language']


admin.site.site_title = 'Управление сайтом'
admin.site.site_header = 'Управление сайтом'
