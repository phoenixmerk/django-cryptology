from django.shortcuts import render
from django.http import HttpResponse
import base64


# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse(render(request, 'polls/index.html', locals()))


def clipher(request):
    if request.method == 'GET':
        return render(request, 'polls/index.html')
    elif request.method == 'POST':
        if 'encode' in request.POST:
            p_text = request.POST.get('p_text').encode('utf-8')
            p_text = base64.b64encode(p_text).decode('utf-8')
            return render(request, 'polls/index.html', locals())
        elif 'decode' in request.POST:
            p_text = request.POST.get('p_text')
            p_text = base64.b64decode(p_text).decode('utf-8')
            return render(request, 'polls/index.html', locals())  # locals()表示将原本请求的数据重新返回