from django.contrib.admin import *
from models import *

class OpticalRotationInline(TabularInline):
	model = OpticalRotation
	extra = 1
class GCRetentionTimeInline(TabularInline):
	model = GCRetentionTime
	extra = 1
class ProtonJValuesInline(TabularInline):
	model = ProtonJValues
	extra = 2
class ProtonNMRInline(TabularInline):
	model = ProtonNMR
	extra = 1

class MoleculeAdmin(ModelAdmin):
	inlines = (
		OpticalRotationInline,
		GCRetentionTimeInline,
		ProtonNMRInline,
		ProtonJValuesInline,
	)

site.register(Molecule, MoleculeAdmin)
