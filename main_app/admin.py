from django.contrib import admin
from main_app.models import Cities, ProgramLanguage, Vacancy, Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "owner"]
    search_fields = ["name", "owner"]


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
    list_display = ['name', 'author', 'city', 'language']
    search_fields = ['name', 'author', 'city', 'language']
    list_filter = ['city', 'language', 'phone_contact']


admin.site.site_title = 'Управление сайтом'
admin.site.site_header = 'Управление сайтом'
