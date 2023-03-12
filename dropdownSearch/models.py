from django.db import models

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('receiving', 'Receiving'),
        ('reading', 'Reading'),
        ('writing', 'Writing'),
        ('published', 'Published'),
        ('playing', 'Playing'),
        ('teaching', 'Teaching'),
        ('thinking', 'Thinking'),
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title
    
