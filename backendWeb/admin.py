from .models import Question
from django.contrib import admin


admin.site.register(Question) # um neuen tabel auf admin seite zu laden
# wird erst bei server steart ausgeführt