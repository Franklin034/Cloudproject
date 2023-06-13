from django.contrib import admin
from .models import Post, Video, SurveyQuestion, SurveyAnswer, Cloud_Choice, Migraton_Phase
from django import forms

admin.site.register(Post)

admin.site.register(Video)


class AnswerAdminForm(forms.ModelForm):
    class Meta:
        model = SurveyAnswer
        fields = '__all__'
        widgets = {
            'recommendation': forms.Textarea(attrs={'rows': 3}),
        }

class AnswerAdmin(admin.ModelAdmin):
    form = AnswerAdminForm

admin.site.register(SurveyQuestion)
admin.site.register(SurveyAnswer,AnswerAdmin)
admin.site.register(Cloud_Choice)
admin.site.register(Migraton_Phase)