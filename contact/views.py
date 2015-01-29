from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render


def send_email(request):
    subject = request.POST.get('name', '')
    from_email = request.POST.get('email', '')
    message = request.POST.get('comments', '')

    if message and from_email:
        try:
            send_mail(subject, "email: " + from_email + "\nmessage: " + message, from_email, ['senhpk@yandex.ru'],
                      fail_silently=False)
        except BadHeaderError:
            return render(request, 'contact/error.html')
        return render(request, 'contact/thank.html')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return render(request, 'contact/error.html')



