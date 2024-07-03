from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.views.generic import CreateView
from django.urls import reverse_lazy

from users.forms import CreationForm
from users.models import UserProfile
from users.helper import paginator


def index(request):
    user_list = UserProfile.objects.all()
    # В словаре context отправляем информацию в шаблон
    return render(
        request,
        'users/index.html',
        {'page_obj': paginator(request, user_list)},
    )


def user_detail(request, pk):
    user = get_object_or_404(UserProfile, id=pk)
    form = CreationForm()
    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'users/user_detail.html', context)


@login_required
def user_edit(request, pk):
    user = get_object_or_404(UserProfile, id=pk)
    if user != request.user:
        return HttpResponseForbidden(
            "У вас нет прав для редактирования этого профиля.")
    form = CreationForm(
        request.POST or None,
        instance=user,
        files=request.FILES or None,
    )
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('users:user_detail', pk)
    context = {
        'form': form,
        'is_edit': True,
        'user_id': pk,
    }
    return render(request, 'users/signup.html', context)


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('users:index')
    template_name = 'users/signup.html'
