from django.urls import path
from . import views

app_name='kito'

urlpatterns = [

    path('',views.kito_list,name='kito_list'),
    path('add', views.add_daykito, name='add_daykito'),
    path('<str:slug>/edit',views.edit,name='edit'),
    path('list_delete/<str:slug>',views.deleteList,name='list_delete'),



    path('add-haeder', views.add_haeder, name='add_haeder'),
    path('<str:slug>/edit-header',views.edit_header,name='edit_header'),
    path('header_delete/<str:slug>',views.delete_header,name='delete_header'),


    path('add-cook', views.add_cook, name='add_cook'),
    path('<str:slug>/edit-cook',views.edit_cook,name='edit_cook'),
    path('cook_delete/<str:slug>',views.delete_cook,name='delete_cook'),
    
    # path('categories',views.all_categories,name='all_categories'),
    # path('categories/<int:id>',views.category_ads,name='category_ads'),
    # path('<int:id>/edit',views.post_edit,name='post_edit'),
    # path('delete/<int:id>/',views.delete_List, name='delete_list'),

]