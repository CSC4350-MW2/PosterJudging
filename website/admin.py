from django.contrib import admin
from .models import session, judge, administrator, submission

admin.site.register(session)
admin.site.register(judge)
admin.site.register(administrator)
admin.site.register(submission)