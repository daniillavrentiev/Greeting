from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView
from django.http import Http404

from .models import Greeting

from .forms import GreetingForm

JSON_DUMPS_PARAMS = {
    'ensure_ascii': False
}


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(self, request, *args, **kwargs)
        except Exception as e:
            return self._response({'errorMessage': e.message}, status=400)
        if isinstance(response, (dict, list)):
            return self._response(response)
        else:
            return response


@staticmethod
def _response(data, *, status=200):
    return JsonResponse(
        data,
        status=status,
        safe=not isinstance(data, list),
        json_dumps_params=JSON_DUMPS_PARAMS
    )


class GreetingView(View):

    def get(self, request, *args, **kwargs):
        try:
            name = Greeting.objects.filter(id=kwargs['id'])
        except:
            raise Http404('fwaaw')
        context = {'name': name}
        return render(request, 'greeting.html', context=context)


class MeetingView(View):

    def get(self, request, *args, **kwargs):
        name = Greeting.objects.filter(name=kwargs['name'])
        context = {'name': name}
        return render(request, 'meeting.html', context=context)


class IndexView(View):

    def get(self, request, *args, **kwargs):
        form = GreetingForm(request.POST or None)
        context = {'form': form}
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        form = GreetingForm(request.POST or None)

        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.name = form.cleaned_data['name']
            new_data.last_name = form.cleaned_data['last_name']
            new_data.email = form.cleaned_data['email']
            new_data.save()

            return HttpResponseRedirect(f'/greeting/{new_data.id}')

        if form.errors:
            for data in form.errors['name']:
                name = data
            return HttpResponseRedirect(f'/meeting/{name}')

        context = {'form': form}
        return render(request, 'index.html', context=context)


class ConnectionView(ListView):

    model = Greeting
    template_name = 'connection.html'
    context_object_name = 'users_list'
    paginate_by = 3

