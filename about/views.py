from django.shortcuts import render, get_list_or_404

from about.models import About


class MultipleObjectsReturnedError(Exception):
    pass

def about(request):
    about_pages = About.objects.filter(status=1)
    if about_pages.count() > 1:
        raise MultipleObjectsReturnedError("More than one object found in the database.")
    about_page = about_pages.first()  # Retrieve the first object if it exists
    return render(request, 'about/about.html', {'about_page': about_page})


