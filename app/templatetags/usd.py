from django import template
register = template.Library()


def swapping(value):
    return value.swapcase()

@register.filter(name='count')
def counting(value,args):
    c=0
    for i in range(len(value)):
        if value[i:i+len(args)]== args:
            c+=1
    return c


def remove(value,args):
    return value.replace(args,'')

# registering filters
register.filter('swap',swapping)   # @register.filter(name='swap')
register.filter('remove',remove)
#register.filter('count',counting)
        