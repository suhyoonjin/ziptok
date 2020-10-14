from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import User

# Create your views here.
def register(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get("username")   #딕셔너리형태
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")
        name = request.POST.get("name")
        birth = request.POST.get("birth")
        email = request.POST.get("email")
        phone_num = request.POST.get("phone_num")
        addr = request.POST.get("addr")
        rcmd_id = request.POST.get("rcmd_id")
        is_expert = request.POST.get("is_expert")

        res_data = {}
        if not (username and password and re_password):
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password:
            return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User(username=username, password=make_password(password), name=name, birth=birth, email=email,
                        phone_num=phone_num, addr=addr, rcmd_id=rcmd_id, is_expert=is_expert)
            user.save()
        return render(request, 'register.html', res_data) #register를 요청받으면 register.html 로 응답.