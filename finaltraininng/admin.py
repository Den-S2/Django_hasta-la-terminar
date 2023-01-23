from django.contrib import admin
from finaltraininng.models import User, Training, Trainer, Abon, Prize, Order, Wallet
# Register your models here.

admin.site.register(Training)
admin.site.register(Trainer)
admin.site.register(Abon)
admin.site.register(Prize)
admin.site.register(Order)
admin.site.register(Wallet)
admin.site.register(User)