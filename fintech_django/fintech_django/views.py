import subprocess

from django.http import HttpResponse, HttpResponseForbidden


def git_update(request):
    if request.user.is_staff:
        output = subprocess.getoutput("git pull")
        return HttpResponse(output)
    else:
        return HttpResponseForbidden("Only admins can access this command.")

