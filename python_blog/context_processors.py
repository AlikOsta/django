from . import models

def menu_items(request):
    menu_items = models.Menu.objects.all()
    current_url_name = request.resolver_match.view_name if request.resolver_match else ''
    
    for item in menu_items:
        item.is_active = current_url_name == item.slug

    return {'menu_items': menu_items}