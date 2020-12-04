from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, "test.html")


def test(request):
    hi = '你好，世界是美丽的'
    test = 'this is a test page,test successful！'

    return render(request, "test.html", {'hi': hi, 'test': test})


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username == 'test' and password == '123'):
            return redirect('/test/')
        else:
            return render(request, "login.html", {'error': '用户名或密码错误！'})
