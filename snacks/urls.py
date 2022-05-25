from django.urls import path

from .views import SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('<int:pk>', SnackDetailView.as_view(), name='snack_detail'),  # Integer, Primary Key
    path('create/', SnackCreateView.as_view(), name='snack_create'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name='snack_update'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name='snack_delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
