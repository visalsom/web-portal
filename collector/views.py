from rest_framework.generics import ListCreateAPIView
from .models import Contact
from .serializers import ContactSerializer

class ContactCreateView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer




