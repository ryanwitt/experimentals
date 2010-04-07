from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
@stringfilter
def formulize(value):
	items = []
	number = []
	for c in value + ' ':
		if c.isdigit():
			number.append(c)
		else:
			if number:
				items += ['<sub>'] + number + ['</sub>']
				number = []
			items.append(c)

	return mark_safe(''.join(items).strip())

if __name__ == '__main__':
	print formulize('C143H56')