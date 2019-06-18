from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value,arg):
    '''
    this cuts all the value of the "arg" from the strings!
    '''
    return value.replace(arg,"")

#register.filter( filter name, filter_fuunction)
# register.filter("cut",cut)
