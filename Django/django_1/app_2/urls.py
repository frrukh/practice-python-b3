from django.urls import path
from . import views


urlpatterns = [
    path('render_html/',views.render_html),
    path('get_id/<id>',views.get_value),
    path('get_specific/<int:id>',views.get_specific),
    path('send_to_html/',views.send_data),
    path('bisects/',views.bisects)
]