from faq.models import Faq
from django.views.generic import ListView


class FaqListView(ListView):
    model = Faq
