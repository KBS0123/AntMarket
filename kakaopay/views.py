# kakaopay/views.py
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from cart.cart import Cart

next_order_id = 1001
def index(request):
    global next_order_id

    if request.method == "POST":
        item_name = request.POST.get('item_name')
        quantity = request.POST.get('quantity')
        total_amount = request.POST.get('total_amount')

        url = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            'Authorization': 'KakaoAK 650da9554612f198b916502e78c1aad4',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        }
        data = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": str(next_order_id),     # 주문번호
            "partner_user_id": request.user.username,    # 유저 아이디
            "item_name": item_name,        # 구매 물품 이름
            "quantity": quantity,                # 구매 물품 수량
            "total_amount": total_amount,        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": "http://127.0.0.1:8000/kakaopay/success/",
            "cancel_url": "http://127.0.0.1:8000/kakaopay/cancel/",
            "fail_url": "http://127.0.0.1:8000/kakaopay/fail/",
        }

        res = requests.post(url, headers=headers, data=data)
        request.session['tid'] = res.json()['tid']      # 결제 승인시 사용할 tid를 세션에 저장
        next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장

        next_order_id += 1

        return redirect(next_url)

    return HttpResponse(status=405)

def success(request):
    global next_order_id

    url = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        'Authorization': 'KakaoAK 650da9554612f198b916502e78c1aad4',
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    params = {
        "cid": "TC0ONETIME",  # 테스트용 코드
        "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": str(next_order_id - 1),  # 주문번호
        "partner_user_id": request.user.username,  # 유저 아이디
        "pg_token": request.GET.get("pg_token"),  # 쿼리 스트링으로 받은 pg토큰
    }

    res = requests.post(url, headers=headers, params=params)
    amount = res.json()['amount']['total']

    res = res.json()
    context = {
        'res': res,
        'amount': amount,
    }

    cart = Cart(request)
    cart.clear()

    return render(request, 'kakaopay/success.html', context)

def cancel(request):
    return render(request, 'kakaopay/cancel.html')

def fail(request):
    return render(request, 'kakaopay/fail.html')

def kakao_callback(request):
    code = request.GET.get('code')
    # 인증 코드 처리 로직
    if code:
        return HttpResponse(f'인증 코드: {code}')
    return HttpResponse('인증 코드가 없습니다.')