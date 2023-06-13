from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=timezone.now) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


ALLOWED_EXTENSIONS = ['MOV', 'avi', 'mp4', 'webm', 'mkv']

def validate_video_file(value):
    ext = value.name.split('.')[-1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        allowed_extensions = ', '.join(ALLOWED_EXTENSIONS)
        raise ValidationError(_('Invalid file format. Only {} files are allowed.').format(allowed_extensions))

    max_size = 204857600  # 200 MB
    if value.size > max_size:
        raise ValidationError(_('File size exceeds the maximum limit of 100 MB.'))

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/', validators=[validate_video_file])
    contents = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('video-detail', kwargs={'pk': self.pk})

class SurveyQuestion(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class SurveyAnswer(models.Model):
    ANSWER_CHOICES = [
        ('Agreed', 'Agreed'),
        ('Maybe', 'Maybe'),
        ('Disagreed', 'Disagreed'),
    ]

    GRADE_CHOICES = [
        (2, 'Agreed'),
        (1, 'Maybe'),
        (0, 'Disagreed'),
    ]

    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200, choices=ANSWER_CHOICES)
    recommendation = models.TextField(blank=True)
    grade = models.IntegerField(choices=GRADE_CHOICES)

    def __str__(self):
        return self.answer_text
    
class Cloud_Choice(models.Model):
    image = models.ImageField(upload_to='cloud_choice_images')
    content = models.TextField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Migraton_Phase(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    


