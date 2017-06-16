from django import template


register = template.Library() 

@register.filter('addfloat')
def addfloat(x, y):
	"""
	Adds the x and y and returns as floating points
	"""
	return float(x) + float(y)
	