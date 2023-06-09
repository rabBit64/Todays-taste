from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.create,name='create'),
    path('<int:article_pk>/',views.detail,name='detail'),
    path('<int:article_pk>/update/',views.update,name='update'),
    path('<int:article_pk>/delete/',views.delete,name='delete'),
    path('<int:article_pk>/create_comment/',views.create_comment,name='create_comment'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:article_pk>/comments/<int:comment_pk>/comment_like/', views.comment_like,name='comment_like'),
    path('<int:article_pk>/likes/', views.likes, name='likes'),
    path('search/', views.search, name='search'),
    # path('<int:article_pk>/scrap/', views.scrap, name='scrap'),
    path('<int:product_pk>/scrap/', views.scrap, name='scrap'),
    path('<int:product_pk>/basket/', views.basket, name='basket'),
    path('product/', views.product, name='product'),
     #관리자 상품 업로드
    # path('add/',views.addProduct,name='add_product'),
    # path('product_create/',views.product_create,name='product_create'),
    path('category/<str:subject>/',views.category , name='category'),
    path('<int:product_pk>/product_detail/',views.product_detail,name='product_detail'),
    
]
