from django.shortcuts import render, reverse
from random import choice
from urllib.parse import urlparse
from django.http import JsonResponse, HttpResponseRedirect
from .models import ShortedUrls
from django.views.decorators.csrf import csrf_exempt

# def url_checker(request):
#     """Function that checks URL length more then 16 symbols"""
# result = False
# length = len(url_splitter())
# if length >= 16:
#    result = True
#    print('OK')
# else:
#     print('Sorry, URL is to short already')
#
# return result


def url_splitter(full_url):
    """Function that splits URL by / and returns main part without /"""
    parsed = urlparse(full_url)
    components = parsed.path[1:].split('/')
    result = ''.join(components).replace('-', '').replace('.', '')

    return result

@csrf_exempt
def short_url(request):
    """Function that generates string for URL"""
    if request.is_ajax():
        url = request.POST.get('url')
        if url:
            url_parts = url_splitter(url)
            slug = slug_generator(url_parts)
            ShortedUrls.objects.create(
                main_url=url,
                slug=slug,
                visits=0
            )

            return JsonResponse(
                {'status': True, 'msg': request.scheme + '://' + request.get_host() + '/' + slug.lower()},
                status=200)
        else:
            return JsonResponse({'status': False, 'msg': 'Field cannot be empty'}, status=200)
    else:
        return JsonResponse({'status': False, 'msg': 'Request is not allowed'}, status=200)


def slug_generator(parts, symbols=8):
    slug = str()
    for _ in range(symbols):
        symbol = choice(parts)
        slug += symbol

    return slug


def slug_exists(slug):
    """Function that checks is generated slug exists in db"""
    if ShortedUrls.objects.filter(slug=slug).exists():
        return True
    else:
        return False


def url_redirect(request, slug):
    """Function that redirects to URL by slug from db"""
    if slug_exists(slug):
        obj = ShortedUrls.objects.get(slug=slug)
        obj.visits += 1
        obj.save()
        return HttpResponseRedirect(obj.main_url)
    else:
        return HttpResponseRedirect(reverse('main:home'))


def view_main(request):
    """Function that renders main page for application"""
    return render(request, 'views/index.html')

@csrf_exempt
def get_count_url_visits(request):
    """Function that renders page with number of visits for shorted URL"""
    if request.is_ajax():
        slug = request.POST.get('slug')
        if slug:
            visits = ShortedUrls.objects.get(slug=slug).visits

            return JsonResponse({'status': True, 'msg': str(visits) + ' visits on link with slug: ' + slug}, status=200)
        else:
            return JsonResponse({'status': False, 'msg': 'Field cannot be empty'}, status=200)
    else:
        return JsonResponse({'status': False, 'msg': 'Request is not allowed'}, status=200)
