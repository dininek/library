from django.db import models
from components.models import Component, Editable

class Project(Editable):
	name				= models.CharField(max_length=64)
	acronym				= models.CharField(max_length=16)
	customer			= models.CharField(max_length=64)
	end_user			= models.CharField(max_length=64)
	start_date			= models.DateField()
	end_date			= models.DateField()

class Board(Editable):
	name				= models.CharField(max_length=32)
	model				= models.ForeignKey(Model)
	width				= models.FloatField(null=True,blank=True)
	length				= models.FloatField(null=True,blank=True)
	thickness			= models.FloatField(null=True,blank=True)
	material			= models.CharField(null=True,blank=True,max_length=8)
	layers				= models.IntegerField(null=True,blank=True)
	components			= models.ManyToManyField(Component, through='DeclaredComponent')
	minimum_temperature	= models.FloatField(null=True,blank=True)
	maximum_temperature = models.FloatField(null=True,blank=True)
	shock_environment	= models.FloatField(null=True,blank=True)
	natural_frequency	= models.FloatField(null=True,blank=True)


class Model(Editable):
	ENV_CHOICE			= (
					('GB','Ground, Benign'),
					('GF','Ground, Fixed'),
					('GM','Ground, Mobile'),
					('NS','Naval, Sheltered'),
					('NU','Naval, Unsheltered'),
					('AIC','Airborne, Inhabited, Cargo'),
					('AIF','Airborne, Inhabited, Fighter'),
					('AUC','Airborne, Uninhabited, Cargo'),
					('AUF','Airborne, Uninhabited, Fighter'),
					('ARW','Airborne, Rotary Winged'),
					('SF','Space Flight'),
					('MF','Missle, Flight'),
					('ML','Missle, Launch'),
					('CL','Cannon, Launch'),
				)
	phase				= models.CharField(max_length=8,null=True,blank=True)
	project				= models.ForeignKey(Project)
	number				= models.IntegerField()
	name				= models.CharField(max_length=32)
	environment			= models.CharField(max_length=3,choice=ENV_CHOICE)
	
class DeclaredComponent(Editable):
	board				= models.ForeignKey(Board)
	component			= models.ForeignKey(Component)
	designator			= models.CharField(max_length = 8)



