from django.contrib import admin

from .models import Option, Poll, Vote, Voter

# Register your models here.
class OptionAdmin(admin.ModelAdmin):
    list_display =  ("poll", "answer")

admin.site.register(Option, OptionAdmin)
admin.site.register(Poll)
admin.site.register(Vote)
admin.site.register(Voter)
