# 뷰 : 기능을 담당(페이지 단위)
# 화면이 나타나는 뷰, 화면이 없는 뷰
# 화면이 있건 없건 주소 URL은 있어야 한다.

# 뷰 내용(함수, 클래스), URL이 있으면 동작한다.

# 뷰의 코드 형식 : 함수형, 클래스형
# 함수형 : request를 매개변수로 받고(추가 매개변수 가능), 모양은 함수,
#           내가 원하는대로 동작들을 설계하고 만들고 싶을 때

# 클래스형 : CRUD 기존에 많이 사용하는 기능을 미리 클래스로 만들어두고
#           상속받아서 사용한다.
# 장고의 제네릭 뷰를 많이 사용
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # 어떤 계산이나, 데이터베이스 조회, 수정, 등록
    # 응답 메시지를 만들어서 반환.
    # html 변수를 대신해서 템플릿
    html = "<html><body>Hi Django.</body></html>"
    return HttpResponse(html)

# 뷰의 이름은 : welcome
# 뷰의 접속 주소 : welcome/
# 내용은 : Welcome to Django.

def welcome(request):
    html = "<html><body>Welcome to Django.</body></html>"
    return HttpResponse(html)

def template_test(request):
    # 기본 템플릿 폴더
    # 1. admin 앱
    # 2. 각 앱의 폴더에 있는 templates 폴더
    # 3. 여러분이 설정한 폴더
    return render(request, 'test.html')

# 함수형 뷰 만들기, 템플릿 만들기, URL연결하기, 브라우저로 접속해보기
