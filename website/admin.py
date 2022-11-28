from django.contrib import admin
from .models import session, judge, submission

admin.site.register(session)
admin.site.register(judge)
admin.site.register(submission)