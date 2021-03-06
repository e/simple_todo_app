from django.conf.urls import url

from items.views import IndexView, ItemCreateView, ItemUpdateView, ItemDeleteView, ItemChangeStatusView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pending>pending)/$', IndexView.as_view(), name='list_pending'),
    url(r'^create/$', ItemCreateView.as_view(), name='item_create'),
    url(r'^(?P<pk>\d+)/update/$', ItemUpdateView.as_view(), name='item_update'),
    url(r'^(?P<pk>\d+)/delete/$', ItemDeleteView.as_view(), name='item_delete'),
    url(r'^(?P<pk>\d+)/status/$', ItemChangeStatusView.as_view(), name='item_change_status'),
]
