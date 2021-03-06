from django.db import models
from django_countries.fields import CountryField
import fields
from filebrowser.fields import FileBrowseField
from smart_selects.db_fields import GroupedForeignKey, ChainedForeignKey

class Package(models.Model):
	LEAD_FINISH_CHOICE	= (
					('A', 'Tin/lead dipped'), 
					('B', 'Tin/lead plated'), 
					('C', 'Gold plated'),
					('P', 'Palladium'),
					('S', 'Pure tin plated'), 
					('D', 'Palladium/nickel/gold plated'),
					('X', 'Other'),
					)
	LEAD_STYLE_CHOICE = (
					('F', 'Flat'),
					('G', 'Gullwing'),
					('J', 'J-bend'),
					('N', 'No lead'),
					('P', 'Pin/Peg'),
					('T', 'Through hole'),
					('U', 'J-reversed'),
					('W', 'Wraparound'),
					('X', 'Other'),
					)
	LEAD_PATTERN_CHOICE = (
					('A', 'Axial'),
					('B', 'Bottom'),
					('D', 'Dual'),
					('M', 'Matrix/Array'),
					('Q', 'Quad'),
					('R', 'Radial'),
					('S', 'Single'),
					('Z', 'Zig-zag'),
					('X', 'Other'),
					)
	PACKAGE_STYLE_CHOICE = (
					('PC', 'Passive chip'),
					('PL', 'Passive leaded'),
					('CC', 'Chip-carrier'),
					('CY', 'Can/cylinder'),
					('FM', 'Flange mount'),
					('FP', 'Flat pack'),
					('GA', 'Grid-array'),
					('IP', 'In-line'),
					('SS', 'Other/special shape'),
					)
	PACKAGE_MATERIAL_CHOICE = (
					('C', 'Cofired ceramic, metal seal'),
					('E', 'Epoxy mold'),
					('T', 'Conformal coated'),
					('G', 'Ceramic, glass seal'),
					('L', 'Glass'),
					('M', 'Metal'),
					('P', 'Plastic'),
					('X', 'Other'),
					)
	lead_count 		= models.IntegerField()
	lead_finish		= models.CharField(max_length=1,choices=LEAD_FINISH_CHOICE)
	lead_style		= models.CharField(max_length=1,choices=LEAD_STYLE_CHOICE)
	lead_pattern	= models.CharField(max_length=1,choices=LEAD_PATTERN_CHOICE)
	package_style	= models.CharField(max_length=2,choices=PACKAGE_STYLE_CHOICE)
	package_material= models.CharField(max_length=1,choices=PACKAGE_MATERIAL_CHOICE)
	footprint		= models.CharField(max_length = 32, unique=True)
	alt_footprint	= models.CharField(max_length = 32, unique=True)
	surface_mount	= models.BooleanField()
	body_width 		= models.FloatField(blank = True, null = True)
	body_length 	= models.FloatField(blank = True, null = True)
	body_height 	= models.FloatField(blank = True, null = True)
	mass			= models.FloatField(blank = True, null = True)
	name 			= models.CharField(max_length = 32, unique=True)
	description		= models.CharField(max_length = 128, blank = True)
	pitch 			= models.FloatField()
	def __unicode__(self):
		return u'%s' % (self.name,)

class Family(models.Model):
	name			= models.CharField(max_length = 64, unique = True)
	def __unicode__(self):
		return unicode(self.name)
	
class Group(models.Model):
	name			= models.CharField(max_length = 64)
	number			= models.IntegerField()
	family			= models.ForeignKey(Family)
	def __unicode__(self):
		return unicode(self.name)

class Manufacturer(models.Model):
	name			= models.CharField(max_length = 64, unique = True)
	country			= CountryField()
	dscc_qml		= models.BooleanField()
	escc_qml		= models.BooleanField()
	def __unicode__(self):
		return u'%s, %s' % (self.name, self.country)


class Component(models.Model):
	standard_pn 	= models.CharField(max_length = 32)
	manufacturer_pn	= models.CharField(max_length = 32)
	local_ref 		= models.CharField(max_length = 32, unique=True)
	manufacturer 	= models.ForeignKey(Manufacturer)
	description 	= models.CharField(max_length = 128)
	package 		= models.ForeignKey(Package)
	symbol_ref		= models.CharField(max_length = 32)
	family			= models.ForeignKey(Family)
	group			= ChainedForeignKey(
						Group, 
						chained_field 		= "family",
						chained_model_field	= "family",
						show_all			= False,
						auto_choose			= True,
					)
	in_bom			= models.BooleanField()
	radiation_tid	= models.FloatField()
	radiation_see	= models.FloatField()
	rha				= models.BooleanField()
	spec_type		= models.CharField(max_length = 8)
	spec_level		= models.CharField(max_length = 8)
	general_spec	= models.CharField(max_length = 32)
	detailed_spec	= models.CharField(max_length = 32)
	datasheet		= FileBrowseField('PDF', max_length=200, directory='datasheets/', extensions=['.pdf'], blank=True)
	crossreference	= models.ManyToManyField('self',through='Crossreference',symmetrical=False,)
	def __unicode__(self):
		return u'%s' % (self.standard_pn,) 

class Project(models.Model):
	name			= models.CharField(max_length = 128)
	acronym			= models.CharField(max_length = 32)

class Board(models.Model):
	name			= models.CharField(max_length = 32)
	project			= models.ForeignKey(Project)

	
class Crossreference(models.Model):
	component_1		= models.ForeignKey(Component,related_name='xref1_%(app_label)s_%(class)s')
	component_2		= models.ForeignKey(Component,related_name='xref2_%(app_label)s_%(class)s')
	summary			= models.CharField(max_length=255)
	same_pinout		= models.BooleanField()
	same_package	= models.BooleanField()
	same_function	= models.BooleanField()

	
	

	
	
	
	
