from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import base64


# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse(render(request, 'polls/index.html', locals()))


def is_contains_chinese(strs):
    # find is there any chinese character
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


def clipher(request):
    if request.method == 'GET':
        return render(request, 'polls/index.html')
    elif request.method == 'POST':
        if 'encode' in request.POST:
            p_text = request.POST.get('p_text').encode('utf-8')
            p_text = base64.b64encode(p_text).decode('utf-8')
            return render(request, 'polls/index.html', locals())
        elif 'decode' in request.POST:
            if is_contains_chinese(request.POST.get('p_text')):
                messages.add_message(request, messages.INFO, 'Invalid Clipher Text')
                return render(request, 'polls/index.html')
            else:
                try:
                    p_text = request.POST.get('p_text').encode('utf-8')
                    p_text = base64.b64decode(p_text).decode('utf-8')
                    return render(request, 'polls/index.html', locals())  # locals()表示将原本请求的数据重新返回
                except(ValueError, ArithmeticError):
                    messages.add_message(request, messages.WARNING, 'Can Not Decode')
                    return render(request, 'polls/index.html')
