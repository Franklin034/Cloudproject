from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import SurveyQuestion, SurveyAnswer
from .models import Post, Video, Cloud_Choice, Migraton_Phase
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'edu/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'edu/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

class UserPostListView(ListView):
    model = Post
    template_name = 'edu/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def learn(request):
    context = {
        'videos': Video.objects.all()
    }
    return render(request, 'edu/learn.html', context)

class VideoListView(LoginRequiredMixin, ListView):
    model = Video
    template_name = 'edu/learn.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'videos'
    ordering = ['-date_posted']
    paginate_by = 1

class VideoDetailView(DetailView):
    model = Video
    

def assessment(request):
    questions = SurveyQuestion.objects.all()
    total_questions = len(questions)
    agreed_value = 2
    max_grade = agreed_value * total_questions
    

    if request.method == 'POST':
        answers = []

        for question in questions:
            answer_text = request.POST.get(str(question.id))
            grade = 2 if answer_text == 'Agreed' else 1 if answer_text == 'Maybe' else 0
            answer = SurveyAnswer(question=question, answer_text=answer_text, grade=grade)
            answers.append(answer)

        # Process the answers and retrieve the corresponding recommendation
        recommendation_data = []
        user_grade = 0
        for answer in answers:
            recommendation = SurveyAnswer.objects.filter(question=answer.question, answer_text=answer.answer_text).first()
            recommendation_data.append({'question': answer.question.question_text, 'answer': answer.answer_text, 'recommendation': recommendation.recommendation, 'grade': answer.grade})
            user_grade += answer.grade
            userPercentage = (user_grade / max_grade) * 100
            maxPercentage = (max_grade / max_grade) * 100
        passing_grade = 0.8 * max_grade

        # Render a response with the grades and recommendations
        context = {
            'recommendations': recommendation_data,
            'max_grade': maxPercentage, 
            'user_grade': userPercentage,
            'passing_grade': passing_grade,
        }
        html = render_to_string('edu/printable_form.html', context)
        return HttpResponse(html)

    return render(request, 'edu/assessment.html', {'questions': questions})


def choice(request):
    context = {
        'CloudChoices': Cloud_Choice.objects.all()
    }
    return render(request, 'edu/cloud-choice.html', context)

class ChoiceListView(ListView):
    model = Cloud_Choice
    template_name = 'edu/cloud-choice.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'CloudChoices'
    paginate_by = 2

def migration(request):
    context = {
        'migrations': Migraton_Phase.objects.all()
    }
    return render(request, 'edu/migration.html', context)

class MigrationListView(ListView):
    model = Migraton_Phase
    template_name = 'edu/migration.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'migrations'
    paginate_by = 2



def about(request):
    return render(request, 'edu/about.html', {'title': 'About'})






