from django.contrib import admin

from .models import Option, Poll, Vote, Voter

# Register your models here.
admin.site.register(Option)
admin.site.register(Poll)
admin.site.register(Vote)
admin.site.register(Voter)

