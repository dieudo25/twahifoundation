from django.contrib import admin

from contact.models.person import Person, Company


class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


admin.site.register(Person, PersonAdmin)

admin.site.register(Company, CompanyAdmin)
