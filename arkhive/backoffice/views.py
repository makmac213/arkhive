import calendar
import json
from datetime import datetime, timedelta

# django
from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.db.models import Q
from django.db.models.loading import get_model
from django.http import HttpResponseRedirect, QueryDict, HttpResponseForbidden
from django.shortcuts import (HttpResponse, redirect, render_to_response, 
                                get_object_or_404, render)
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.base import View 

# news
from news.models import News


class BackofficeView(object):

    class Dashboard(View):

        def get(self, request, *args, **kwargs):
            return HttpResponse('ok')

        @method_decorator(login_required)
        def dispatch(self, *args, **kwargs):
            return super(BackofficeView.Dashboard,
                            self).dispatch(*args, **kwargs)


    class Login(View):
        pass


class BackofficeNews(object):

    class Manage(ListView):
        model = News
        template_name = 'backoffice/news/manage.html'
        context_object_name = 'news'
        paginate_by = 20

        """
        def get(self, request, *args, **kwargs):
            news = News.objects.filter()

            context = {
                'news': news,
            }

            return render(request, self.template_name, context)
        """

    class Display(View):
        template_name = 'backoffice/news/display.html'

        def get(self, request, *args, **kwargs):
            id = kwargs.get('id')
            # TODO: research get single query
            instance = None
            for n in News.objects.filter():
                if n.id.__str__() == id:
                    instance = n

            context = {
                'instance': instance,
            }
            return render(request, self.template_name, context)

    class Spin(View):
        pass