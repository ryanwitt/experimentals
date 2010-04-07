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

class ProtonJValues(Model):
	molecule = ForeignKey('Molecule')
	shift = CharField(blank=True, max_length=32)
	peak_type = CharField(blank=True, max_length=32)
	integration = CharField(blank=True, max_length=32)
	j_value_1 = CharField(blank=True, max_length=8)
	j_value_2 = CharField(blank=True, max_length=8)
	j_value_3 = CharField(blank=True, max_length=8)
	j_value_4 = CharField(blank=True, max_length=8)
	class Meta:
		verbose_name = 'Proton J-Value'

