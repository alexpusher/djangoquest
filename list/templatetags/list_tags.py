from django import template
from list.models import *
register = template.Library()


@register.inclusion_tag('base_list.html')
def base_list():
	top1 = top.objects.all()
	top2 = mosttop.objects.all()
	list = [a.name for a in top1]
	dict = {}
	for qwe in list:
		c = top.objects.get(name=qwe)
		d = c.category_set.all()
		list1 = {dn.name: dn.href for dn in d}
		dict.update({qwe: list1})
	
	return {'mtops' : top2}