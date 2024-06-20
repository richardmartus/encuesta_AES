from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    context = {
        'archivos': "archivos",

    }
    print(context)
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(context)
    else:
        return render(request, 'board/index.html', context)

    def index(request):
        context = {
            'archivos': "archivos",

        }
        print(context)
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return JsonResponse(context)
        else:
            return render(request, 'board/index.html', context)


def resultados(request):
    context = {
        'archivos': "archivos",

    }
    print(context)
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(context)
    else:
        return render(request, 'board/resultados.html', context)
