from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect

from .forms import UserRegistrationForm


def index(request):
    user_regist_form = UserRegistrationForm()
    context = {'user_regist_form': user_regist_form}

    return render(request,
                  "account_ext/register.html",
                  context=context)


def register(request):
    if request.method == "POST":
        user_regist_form = UserRegistrationForm(request.POST)
        if user_regist_form.is_valid():
            new_user = user_regist_form.save(commit=False)
            new_user.set_password(user_regist_form.cleaned_data['password'])
            new_user.save()
            return redirect('/account_ext/register/done/')
        else:
            return render(request,
                          "account_ext/register.html",
                          {'user_regist_form': user_regist_form})
    elif request.method == "GET":
        return redirect('/account_ext/')


# def register_done(request):
#     return render(request, 'account_ext/register_done.html', {})
