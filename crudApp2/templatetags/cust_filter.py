
from django import template

register=template.Library()

def proper_case(value):
    str1=str(value).capitalize()
    return str1

register.filter('sentence',proper_case)