import random
import string
from django.db import transaction
from django.shortcuts import render, redirect
from leaderboard.models import Entry

def leaderboard(request):
    entries = reversed(Entry.objects.order_by('-display_score'))

    return render(request, "chat/room.html", {
        'entries': entries,
    })