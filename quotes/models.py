from django.db import models
from django_countries import CountryField
from components.models import Component, Editable
from lists.models import Project

class Quote(Editable):
	required_quantity	= models.IntegerField()
	quoted_quantity		= models.IntegerField()
	unit_price			= models.DecimalField()
	nre_price			= models.DecimelField()
	lead_time			= models.IntegerField()
	distributor			= models.ForeignKey(Distributor)
	required_component	= models.ForeignKey(Component)
	quoted_component	= models.ForeignKey(Component)
	project				= models.ForeignKey(Project)
	date				= models.DateField()
	comment				= models.CharGield(max_length=255)

class Distributor(Editable):
	name				= models.CharField(max_length=64)
	country				= CountryField()

