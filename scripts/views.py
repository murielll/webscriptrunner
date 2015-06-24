from subprocess import Popen, PIPE
from StringIO import StringIO
import getpass

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

from scripts.models import Script


class Home(View):
    def get(self, request):
        scripts = Script.objects.filter(visible=True)
        username = getpass.getuser()
        context = {'scripts': scripts,
                   'username': username}
        return render(request, "base.html", context)

    def post(self, request):
        script_id = request.POST.get('script_id', False)
        try:
            script_id = int(script_id)
        except ValueError, TypeError:
            return JsonResponse(
                {'status': 'Error',
                 'stdout': '',
                 'stderr': 'Script id is wrong!'}
                 )

        try:
            script = Script.objects.get(pk=script_id)
        except Script.DoesNotExist:
            return JsonResponse(
                {'status': 'Error',
                 'stdout': '',
                 'stderr': 'Script does not exist!'}
                )

        return JsonResponse(
                    runscript(script.filename.path,
                              script.args,
                              script.interpreter)
               )


def runscript(scriptname, args, interpreter='/bin/bash'):
    stdOut = StringIO()
    stdErr = StringIO()
    script = Popen([interpreter, scriptname, args],
                   stdout=PIPE,
                   stderr=PIPE)
    stdOut, stdErr = script.communicate()
    return {'status': 'OK',
            'stdout': stdOut,
            'stderr': stdErr}
