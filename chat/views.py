from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

@login_required
def market_chat_room(request, market_id):
    try:
        #현재 사용자가 가입한 ID가 지정된 코스를 검색
        market = request.user.market_joined.get(id=market_id)
    except:
        #사용자가 코스의 학생이 아니거나 코스가 존재하지 않는 경우
        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {'market': market})