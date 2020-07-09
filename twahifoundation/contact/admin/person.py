from django.contrib import admin

from contact.models.person import Person, Company


class PersonAdmin(admin.ModelAdmin):
    pass


class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)

admin.site.register(Company, CompanyAdmin)
