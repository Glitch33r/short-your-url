from django.shortcuts import render
from random import choice
from urllib.parse import urlparse
from django.http import JsonResponse

def url_checker(request):
    """Function that checks URL length more then 16 symbols"""
    result = False
    # length = len(url_splitter())
    # if length >= 16:
    #    result = True
    #    print('OK')
    # else:
    #     print('Sorry, URL is to short already')
    #
    return result


def url_splitter(full_url):
    """Function that splits URL by / and returns main part without /"""
    parsed = urlparse(full_url)
    components = parsed.path[1:].split('/')
    result = ''.join(components).replace('-', '').replace('.', '')
    
    return result


def slug_generator(request):
    """Function that generates string for URL"""
    slug = str()
    if request.is_ajax():
        url = request.POST.get('url')
        if url:
            for _ in range(8):
                symbol = choice(url_splitter(url))
                slug += symbol

            return JsonResponse({'status': True, 'msg': request.scheme + '://' + request.get_host() + '/' + slug.lower()}, status=200)
        else:
            return JsonResponse({'status': False, 'msg': 'Field cannot be empty'}, status=200)
    else:
        return JsonResponse({'status': False, 'msg': 'Error'}, status=200)


def check_slug_existence(request):
    """Function that checks is generated slug exists in db"""
    pass


def url_redirect(request, slug):
    """Function that redirects to URL by slug from db"""
    pass


def view_main(request):
    """Function that renders main page for application"""
    return render(request, 'views/index.html')


def view_count_url_visits(request, slug):
    """Function that renders page with number of visits for shorted URL"""
    pass