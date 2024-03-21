# 학생의 번호, 국어, 영어, 수학 점수를 전달받은 뒤
# 총점과 평균을 화면에 출력한다.
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView


# form태그는 get방식을 사용한다.
# 출력 화면에서 다시 입력화면으로 돌아갈 수 있게 한다.

# 입력: task/student/register.html
# 출력: task/student/result.html

class StudentRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/student/register.html')


class StudentRegisterView(View):
    def get(self, request):
        data = request.GET
        data = {
            'id': data['id'],
            'kor': int(data['kor']),
            'eng': int(data['eng']),
            'math': int(data['math'])
        }

        total = data['kor'] + data['eng'] + data['math']
        average = round(total / 3, 2)

        return redirect(f'/student/result?total={total}&average={average}')


class StudentResultView(View):
    def get(self, request):
        data = request.GET
        context = {
            'total': request.GET['total'],
            'average': request.GET['average']
        }
        return render(request, 'task/student/result.html', context)

# 회원의 이름과 나이를 전달받는다.
# 전달받은 이름과 나이를 아래와 같은 형식으로 변경시킨다.
# "홍길동님은 20살!"
# 결과 화면으로 이동한다.

# 이름과 나이 작성: task/member/register.html
# 결과 출력: task/member/result.html


class MemberRegisterFormView(View):
    def get(self, request):
        return render(request, 'task/member/register.html')


class MemberRegisterView(View):
    def get(self, request):
        data = request.GET
        data = {
            'name': data['name'],
            'age': data['age']
        }
        result = f'{data["name"]}님은 {data["age"]}살!'
        return redirect(f'/member/result?result={result}')

    def post(self, request):
        data = request.POST
        data = {
            'name': data['name'],
            'age': data['age']
        }
        result = f'{data["name"]}님은 {data["age"]}살!'
        return redirect(f'/member/result?result={result}')


class MemberResultView(View):
    def get(self, request):
        result = request.GET['result']

        return render(request, 'task/member/result.html', {'result': result})


# 상품 정보
# 번호, 상품명, 가격, 재고
# 상품 1개 정보를 REST 방식으로 설계한 뒤
# 화면에 출력하기
# 예시)
# products/1
# task/product/product.html
class ProductDetailView(View):
    def get(self, request):
        return render(request, 'task/product/product.html')


class ProductDetailAPI(APIView):
    def get(self, request, product_id):
        data = {
            'id': product_id,
            'product_name': '마우스',
            'product_price': 50000,
            'product_stock': 50
        }
        return Response(data)















