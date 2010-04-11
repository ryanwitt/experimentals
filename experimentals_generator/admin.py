from django.contrib.admin import *
from models import *

class OpticalRotationInline(TabularInline):
	model = OpticalRotation
	extra = 1
class GCRetentionTimeInline(TabularInline):
	model = GCRetentionTime
	extra = 1
class ProtonNMRShiftInline(TabularInline):
	model = ProtonNMRShift
	extra = 2
class ProtonNMRInline(TabularInline):
	model = ProtonNMR
	extra = 1
class CarbonNMRShiftInline(TabularInline):
	model = CarbonNMRShift
	extra = 2
class CarbonNMRInline(TabularInline):
	model = CarbonNMR
	extra = 1
class IRTypeInline(TabularInline):
	model = IRType
	extra = 1
class IRPeakInline(TabularInline):
	model = IRPeak
	extra = 3
class HRMS(TabularInline):
	model = HRMS
	extra = 1

class MoleculeAdmin(ModelAdmin):
	inlines = (
		OpticalRotationInline,
		GCRetentionTimeInline,
		ProtonNMRInline,
		ProtonNMRShiftInline,
		CarbonNMRInline,
		CarbonNMRShiftInline,
		IRTypeInline,
		IRPeakInline,
        HRMS,
	)

site.register(Molecule, MoleculeAdmin)

