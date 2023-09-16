from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from notification.models import Notification


""" All notifications """


@login_required
def ShowNotifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')
    context = {
        'notifications': notifications,
    }
    return render(request, 'blog/notifications.html', context)
