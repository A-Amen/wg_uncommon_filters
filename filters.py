from django import template

register = template.Library()


@register.filter()
def next(lst, current_index):
    """
    A filter to fetch the next item in list, if the list has a next item.
    Returns an empty string if on the last element.
    Common use case: forward lookup, iterating through a list in template two items at a time.
    Use forloop.counter0 for index to get index for pythonic list.
    Usage in template: <list>|next:<index>
    """
    try:
        return lst[int(current_index) + 1]
    except:
        return ""


@register.filter()
def get_field_type(value):
    """
    Returns name of the field.
    Filter was made to be used in conjunction with wagtail's AbstractEmailForm to determine the type of field per form field.
    Usage in template: <field>|get_field_type
    """
    return type(value.field).__name__
