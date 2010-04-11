from django.db.models import *

class Molecule(Model):
	name = CharField(blank=True, max_length=255)

	def __unicode__(self):
		return u'%s' % self.name

	@permalink
	def get_absolute_url(self):
		return ('experimentals_generator.views.experimental', [str(self.id)])

class OpticalRotation(Model):
	molecule = ForeignKey('Molecule')
	temperature = CharField(blank=True, max_length=32)
	concentration = CharField(blank=True, max_length=32)
	solvent = CharField(blank=True, max_length=32)
	value = CharField(blank=True, max_length=32)
	class Meta:
		verbose_name = 'Optical Rotation'

class GCRetentionTime(Model):	
	molecule = ForeignKey('Molecule')
	major_retention_time = CharField(blank=True, max_length=32)
	minor_retention_time = CharField(blank=True, max_length=32)
	class Meta:
		verbose_name = 'GC Retention Time'

class ProtonNMR(Model):
	molecule = ForeignKey('Molecule')
	frequency = CharField(blank=True, max_length=32)
	solvent = CharField(blank=True, max_length=32)
	class Meta:
		verbose_name = 'Proton NMR'

class ProtonNMRShift(Model):
	molecule = ForeignKey('Molecule')
	shift = CharField(blank=True, max_length=32)
	peak_type = CharField(blank=True, max_length=32)
	integration = CharField(blank=True, max_length=32)
	j_value_1 = CharField(blank=True, max_length=8)
	j_value_2 = CharField(blank=True, max_length=8)
	j_value_3 = CharField(blank=True, max_length=8)
	j_value_4 = CharField(blank=True, max_length=8)
	class Meta:
		verbose_name = 'Proton NMR Shift'

class CarbonNMR(Model):
	molecule = ForeignKey('Molecule')
	frequency = CharField(blank=True, max_length=32)
	solvent = CharField(blank=True, max_length=32)
	class Meta:
		verbose_name = 'Carbon NMR'

class CarbonNMRShift(Model):
	molecule = ForeignKey('Molecule')
	shift = CharField(blank=True, max_length=8)
	class Meta:
		verbose_name = 'Carbon NMR Shift'

class IRType(Model):
	molecule = ForeignKey('Molecule')
	type = CharField(blank=True, max_length=32)
	class Meta:
		verbose_name = 'IR Type'

class IRPeak(Model):
	molecule = ForeignKey('Molecule')
	value = CharField(blank=True, max_length=8)
	class Meta:
		verbose_name = 'IR Peak'
    
class HRMS(Model):
	molecule = ForeignKey('Molecule')
	type = CharField(blank=True, max_length=32)
	formula = CharField(blank=True, max_length=32)
	fragment_type = CharField(blank=True, max_length=32)
	fragment_charge = BooleanField(blank=True, help_text = 'check for positive')
	found = CharField(blank=True, max_length=32)
	calculated = CharField(blank=True, max_length=32)
	class Meta:
		verbose_name = 'High Res Mass Spec'


