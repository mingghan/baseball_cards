from django.shortcuts import render
from django.http import HttpResponse

from .models import Profile


def index(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'card/index.html', context)


def detail(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    context = {'profile': profile}
    return render(request, 'card/card.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
