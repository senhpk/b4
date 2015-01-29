from documents.models import Document
from django.views.generic import ListView


class DocumentListView(ListView):
    model = Document