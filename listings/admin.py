from django.contrib import admin

from .models import Listing, Report, Investment, Valuation, Financial

class ReportInline(admin.StackedInline):
	model = Report

class ListingAdmin(admin.ModelAdmin):
	inlines = [ReportInline,]


admin.site.register(Listing, ListingAdmin)
admin.site.register(Report)
admin.site.register(Investment)
admin.site.register(Valuation)
admin.site.register(Financial)