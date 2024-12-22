from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Field  
from .forms import formt  
from .serializers import FieldSerializer  
import requests
# Create your views here.
BOT_TOKEN = "7549129332:AAEJbNGxnUWyPskPobTGUEmdoaLKr6mcwxs"
CHAT_ID = "6919865060"

def send_telegram_message(chat_id, message, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"  
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML",
    }
    response = requests.post(url, data=data)
    return response.json()


class FildsViews(CreateView):
    model = Field
    form_class = formt
    context_object_name = "Filds"
    template_name = "api/form.html"
    success_url = "good"
    def form_valid(self, form):
        response = super().form_valid(form)
        instance = form.save()
        message = f"""
    <b>New Form Submission:</b>
    Name: {instance.First_Name}{instance.Middle_Name} {instance.Last_Name}
    Email: {instance.Email}
    Phone number: {instance.Phone_Number}
    Service Type: {instance.Service_Type}
    Location: {instance.Location}
    details: {instance.details}    
    """ 
        send_telegram_message(CHAT_ID, message, BOT_TOKEN)
        return response
    
    

class FieldAPI(ListCreateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

    def perform_create(self, serializer):
        # Save the instance and create a new Field object
        instance = serializer.save()

        # Prepare the message for Telegram
        message = f"""
        <b>New Form Submission:</b>\n
        Name: {instance.First_Name} {instance.Middle_Name} {instance.Last_Name}\n
        Email: {instance.Email}\n
        Phone number: {instance.Phone_Number}\n
        Service Type: {instance.Service_Type}\n
        Location: {instance.Location}\n
        Details: {instance.details}\n
        """ 
        send_telegram_message(CHAT_ID, message, BOT_TOKEN)

    @swagger_auto_schema(request_body=FieldSerializer)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            # Call perform_create to save the data
            self.perform_create(serializer)

            # Optionally, return all fields in the response
            all_fields = self.get_queryset()
            all_fields_serializer = self.get_serializer(all_fields, many=True)

            return Response(
                {
                    "message": "Form submission successful!",
                    "fields": all_fields_serializer.data,  # Optional to return all fields
                },
                status=status.HTTP_201_CREATED,
            )

        # Return errors if validation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)