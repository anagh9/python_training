from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from .models import Questions, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        """Return the last five published questions."""
        return Questions.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Questions
    template_name = 'polls/detail.html'
    context_object_name = 'question'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Questions.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'polls/result.html'
    context_object_name = 'question'


def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls_app:results', args=(question.id,)))

