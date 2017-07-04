from django.contrib import admin

from .models import Listing, DocFile, Investment, Valuation, Financial, ListingImage

class DocFileInline(admin.StackedInline):
	model = DocFile

class ListingImageInline(admin.StackedInline):
	model = ListingImage

class ListingAdmin(admin.ModelAdmin):
	inlines = [DocFileInline,]


admin.site.register(Listing, ListingAdmin)
admin.site.register(DocFile)
admin.site.register(Investment)
admin.site.register(Valuation)
admin.site.register(Financial)
admin.site.register(ListingImage)