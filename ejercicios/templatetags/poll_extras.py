from django import template

register = template.Library()

# REF. https://stackoverflow.com/questions/13693888/accessing-dict-elements-with-leading-underscores-in-django-templates

@register.filter(name='get')
def get(d, k):
    return d.get(k, None)

# REF. https://stackoverflow.com/questions/34571880/how-to-check-in-template-if-user-belongs-to-a-group
@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() or user.username
