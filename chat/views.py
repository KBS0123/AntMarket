# chat/views.py
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from market.models import Product
from .models import Message
from .forms import MessageForm

@login_required
def room(request, room_name, seller_id, user_id):
    user = request.user
    if user.id != user_id:
        return JsonResponse({'error': '잘못된 사용자 접근입니다.'}, status=403)

    seller = get_object_or_404(User, id=seller_id)

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.room_name = room_name
            message.user = user  # 현재 사용자 설정
            message.save()
            return JsonResponse({'image_url': message.image.url}, status=201)
        else:
            return JsonResponse({'error': form.errors}, status=400)

    messages = Message.objects.filter(room_name=room_name).order_by('timestamp')

    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages,
        'seller': seller,
        'form': MessageForm(initial={'room_name': room_name}),
    })
