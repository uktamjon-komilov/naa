from django import template

register = template.Library()


@register.simple_tag
def get_paged_link(request, page, obj, flag=False):
    page_num = page
    items = obj
    if items.has_previous and flag:
        if bool(request.GET):
            return f"{request.get_full_path}&{page_num}"
        else:
            return f"?{page_num}"
            
    elif items.has_next:
        if bool(request.GET):
            return f"{request.get_full_path}&{page_num}"
        else:
            return f"?{page_num}"

    else:
        return "#"