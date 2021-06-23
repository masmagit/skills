from django.contrib import admin
from .models import Company, Country, Industry, Skill, Category, JobPosting, City

# Register your models here.
admin.site.register(Company)
admin.site.register(Country)
admin.site.register(Industry)
admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(JobPosting)
admin.site.register(City)