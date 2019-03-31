from django import template

register = template.Library()

# REF. https://stackoverflow.com/questions/13693888/accessing-dict-elements-with-leading-underscores-in-django-templates

@register.filter(name='get')
def get(d, k):
    return d.get(k, None)
