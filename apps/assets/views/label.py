# -*- coding: utf-8 -*-
#

from django.views.generic import TemplateView, CreateView, \
    UpdateView, DeleteView, DetailView
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy

from common.mixins import AdminUserRequiredMixin
from common.const import create_success_msg, update_success_msg
from ..models import Label
from ..forms import LabelForm


__all__ = (
    "LabelListView", "LabelCreateView", "LabelUpdateView",
    "LabelDetailView", "LabelDeleteView",
)


class LabelListView(AdminUserRequiredMixin, TemplateView):
    template_name = 'assets/label_list.html'

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Assets'),
            'action': _('Label list'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class LabelCreateView(AdminUserRequiredMixin, CreateView):
    model = Label
    template_name = 'assets/label_create_update.html'
    form_class = LabelForm
    success_url = reverse_lazy('assets:label-list')
    success_message = create_success_msg

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Assets'),
            'action': _('Create label'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class LabelUpdateView(AdminUserRequiredMixin, UpdateView):
    model = Label
    template_name = 'assets/label_create_update.html'
    form_class = LabelForm
    success_url = reverse_lazy('assets:label-list')
    success_message = update_success_msg

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Assets'),
            'action': _('Update label'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class LabelDetailView(AdminUserRequiredMixin, DetailView):
    pass


class LabelDeleteView(AdminUserRequiredMixin, DeleteView):
    pass
