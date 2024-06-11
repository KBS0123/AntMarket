# kakaopay/admin.py
from django.contrib import admin
from .models import KakaoPayment

@admin.register(KakaoPayment)
class KakaoPaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'date', 'tid', 'item_name')
    list_filter = ('status', 'date')
    search_fields = ('user__username', 'status', 'tid')