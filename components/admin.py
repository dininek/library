# -*- coding: utf-8 -*-
import datetime
from django.contrib import admin
import models 
import reversion

class CrossreferenceInline(admin.TabularInline):
	extra = 0
	fk_name = 'component_2' 
	model = models.Crossreference

class ComponentAdmin(reversion.VersionAdmin):
	fieldsets 		= (
					('Identyfikacja części',{'fields': (
							'local_ref',
							'manufacturer_pn',
							'standard_pn', 
							'symbol_ref',
							)}),
					('Podstawowe informacje',{'fields': (
							'manufacturer',
							('family',
							'group'),
							'package',
							)}),
					('Specyfikacja',{'fields': (
							'datasheet',
							'spec_type',
							'general_spec',
							'detailed_spec',
							'spec_level',
							)}),
					('Dane radiacyjne',{'fields': (
							'radiation_tid',
							'radiation_see',
							'rha',
							)}),
					)
	list_display	= (
							'manufacturer_pn', 
							'standard_pn',
							'local_ref',
							'manufacturer', 
							'family', 
							'group', 
							'package', 
							'spec_type', 
							'spec_level',
						)
	list_display_links = (
							'manufacturer_pn',
							'standard_pn',
							'local_ref',
						)
	list_filter		= (
							'manufacturer',
							'family',
							'group',
							'package',
						)
	inlines			= (CrossreferenceInline,)

class PackageAdmin(reversion.VersionAdmin):
	fieldsets = (
					('Identyfikacja',{'fields': (
							'name',
							'description',
							)}),
					('Footprint',{'fields': (
							('footprint',
							'alt_footprint'),
							)}),
					('Parametry komponentu',{'fields': (
							'body_width',
							'body_length',
							'body_height',
							'mass',
							'package_style',
							'package_material',
							)}),
					('Parametry wyprowadzeń',{'fields': (
							'lead_count',
							'lead_finish',
							'lead_style',
							'lead_pattern',
							'pitch',
							)}),
					)
	list_display = (		
							'name',
							'lead_count',
							'package_style',
							'lead_pattern',
							'lead_style',
							'body_width',
							'body_length',
							'body_height',
					)
	list_filter = (
							'lead_count',
							'package_style',
							'lead_pattern',
							'lead_style',
					)
class GroupInline(admin.TabularInline):
	extra = 0
	model = models.Group

class FamilyAdmin(reversion.VersionAdmin):
	inlines = (GroupInline,)

class ManufacturerAdmin(reversion.VersionAdmin):
	pass

					
admin.site.register(models.Component, ComponentAdmin)
admin.site.register(models.Package, PackageAdmin)
admin.site.register(models.Manufacturer, ManufacturerAdmin)
admin.site.register(models.Family, FamilyAdmin)
