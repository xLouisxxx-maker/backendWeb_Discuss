from django.db import models

# Article erbt von models.Model
class Article(models.Model):  # Model erstellen, um auf SQLite-datenbank zuzugreifen
    title = models.CharField(max_length=200)
    issue = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} Issue: {self.issue}'
