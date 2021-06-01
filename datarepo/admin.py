from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Operators, Plans, Recharge


# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'otp', 'phone', 'created']
    search_fields = ['phone']
    list_filter = ['phone']

    UserAdmin.fieldsets += (
        (
            'Custom fields', {
                'fields': ('phone', 'otp', 'created')
            }
        ),
    )


class OperatorsAdmin(admin.ModelAdmin):
    list_display = ['operator_name']
    list_filter = ['operator_name']
    search_fields = ['operator_name']


class PlansAdmin(admin.ModelAdmin):
    list_display = ['plans']
    list_filter = ['plans']
    search_fields = ['plans']


class RechargeAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'operator_name', 'view_plan', 'amount', 'validity']
    list_filter = ['operator_name', 'amount']
    search_fields = ['phone_number', 'operator_name']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Operators, OperatorsAdmin)
admin.site.register(Plans, PlansAdmin)
admin.site.register(Recharge, RechargeAdmin)