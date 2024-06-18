# chat/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from market.models import Product

from .models import Message
from .forms import MessageForm

def room(request, room_name, id):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.room_name = room_name
            message.user = request.user  # 현재 사용자 설정
            message.save()
            return JsonResponse({'image_url': message.image.url}, status=201)
        else:
            return JsonResponse({'error': 'Invalid form'}, status=400)

    product = get_object_or_404(Product, id=id)
    messages = Message.objects.filter(product=product.id).order_by('timestamp')

    return render(request, 'chat/room.html', {
        'room_name': room_name,

        'messages': messages,
        'form': MessageForm(initial={'room_name': room_name}),
    })