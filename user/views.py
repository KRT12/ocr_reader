from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from django.views.generic.base import TemplateView
from rest_framework.views import APIView

from .forms import UserForm, FileUploadForm
# Create your views here.
from .models import User, FileUpload
from .utils import extract_pan_details


class BaseView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        self.context = super(BaseView, self).get_context_data(**kwargs)
        user_form = UserForm()
        image_form = FileUploadForm()
        self.context['user_form'] = user_form
        self.context['image_form'] = image_form
        return self.render_to_response(self.context)


class UploadImage(APIView):

    def post(self, request, *args, **kwargs):
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            pan_file = FileUpload.objects.last()
            pan_details = extract_pan_details(pan_file.file.path)
            pan_file.delete()
        else:
            pan_details = {}
        return Response(pan_details)


class RegisterUser(APIView):
    def post(self,request,*args,**kwargs):
        user = UserForm(request.POST, request.FILES)
        if user.is_valid():
            user.save()
            return Response({"success":True,"msg":"User Successfully Registered"})
        else:
            return Response({"success":False,"msg":user.errors})