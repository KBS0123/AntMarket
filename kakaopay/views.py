# kakaopay/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from django.conf import settings
from .models import KakaoPayment
from django.http import HttpResponse

# Create your views here.
def index(request):  # 'kakaopay' -> 'index'
    if request.method == "POST":
        approval_url = request.build_absolute_uri(reverse('kakaopay:approval'))
        cancel_url = request.build_absolute_uri(reverse('kakaopay:cancel'))
        fail_url = request.build_absolute_uri(reverse('kakaopay:fail'))


        headers = {
            "Authorization": f"KakaoAK  {settings.KAKAOPAY_REST_API_KEY}",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }



        params = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": "1001",     # 주문번호
            "partner_user_id": str(request.user.id),    # 유저 아이디
            "item_name": "연어초밥",        # 구매 물품 이름
            "quantity": "1",                # 구매 물품 수량
            "total_amount": "12000",        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": approval_url,
            "cancel_url": cancel_url,
            "fail_url": fail_url,
        }

        res = requests.post('https://kapi.kakao.com/v1/payment/ready', headers=headers, data=params)
        res_json = res.json()

        # 결제 정보 저장
        KakaoPayment.objects.create(
            user=request.user,
            tid=res_json['tid'],
            amount=params['total_amount'],
            status='ready',
            item_name=params['item_name']
        )

        request.session['tid'] = res.json()['tid']
        return  redirect(res_json['next_redirect_pc_url'])

    return render(request, 'kakaopay/index.html')

def approval(request):
    tid = request.session.get('tid')
    payment = KakaoPayment.objects.get(tid=tid)
    payment.status = 'approved'
    payment.save()
    return render(request, 'kakaopay/approval.html', {'payment': payment})

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