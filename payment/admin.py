from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'date')
    list_filter = ('status', 'date')
    search_fields = ('user__username', 'status')



