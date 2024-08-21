from .models import Article
from django.contrib import admin


admin.site.register(Article) # um neuen tabel auf admin seite zu laden
# wird erst bei server steart ausgeführt