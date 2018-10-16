from django.shortcuts import render

from .models import Djeet

def feed(request):
  userids = []
  for id in request.user.djeeterprofile.follows.all():
    userids.append(id)

  userids.append(request.user.id)
  djeets = Djeet.objects.filter(user_id__in=userids)[0:25]

  return render(request, 'feed.html', {'djeets': djeets})
