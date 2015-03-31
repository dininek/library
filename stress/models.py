from django.db import models
from components.models import Component, Editable, Family, Group
from lists.models import DeclaredComponent

class Stress(Editable):
	declared_component		= models.ForeignKey(DeclaredComponent)
	pin				= models.IntegerField()
	reference_pin	= models.IntegerField()
	value			= models.FloatField()
	limit			= models.ForeignKey(Limit)
	comment			= models.CharField(max_length=255)

class Derating(Editable):
	DERATING_STYLES  = (("m", "Margin"),
						("r", "Ratio"),)
	style			= models.CharField(max_length=1,choices=DERATING_STYLES)
	parameter		= models.ForeignKey(Parameter)
	family			= models.ForeignKey(Family)
	group			= models.ForeignKey(Group)

class Limit(Editable):
	LIMIT_STYLES	= (	("max","Maximum"),
						("min","Minimum"),)
	component		= models.ForeignKey(Component)
	parameter		= models.ForeignKey(Parameter)
	value			= models.FloatField()
	style			= models.CharField(max_length=3,choices=LIMIT_STYLES)
	name			= models.CharField(max_length=64)

	
# Create your models here.
