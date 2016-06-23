from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from items.models import Item
from items.forms import ItemForm


class IndexView(ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'items'


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_create.html'
    success_url = '/list/'


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_create.html'
    success_url = '/list/'


class ItemDeleteView(DetailView):
    model = Item
    success_url = '/list/'

    def get(self, request, *args, **kwargs):
        item = self.get_object()
        item.delete()
        return HttpResponseRedirect('/list')


class ItemChangeStatusView(DetailView):
    model = Item

    def get(self, request, *args, **kwargs):
        item = self.get_object()
        if item.is_done:
            item.is_done = False
        else:
            item.is_done = True
        item.save()
        return HttpResponseRedirect('/list')


class ListPendingView(ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['items'] = Item.objects.filter(is_done=False)
        return context
