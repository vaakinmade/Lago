from django.contrib import admin

from .models import Listing, Report

class ReportInline(admin.StackedInline):
	model = Report

class ListingAdmin(admin.ModelAdmin):
	inlines = [ReportInline,]


admin.site.register(Listing, ListingAdmin)
admin.site.register(Report)

# Register your models here.