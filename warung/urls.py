
from django.contrib import admin
from django.urls import path, include
from warung import views
urlpatterns = [
    path('warung/', views.warungView, name='indexToko'),
    path('warung/<int:id>', views.warungDetail, name='detailToko'),
    path('kategori/', views.CategoryViews, name='kategori'),
    path('kategori/<int:id>', views.CategoryDetailViews, name='detailKategori'),
    path('stocker/', views.StockerViews, name='stocker'),
    path('stocker/<int:id>', views.StockerDetailViews, name='detailStocker'),
    path('barang/', views.GoodsViews, name='barang'),
    path('barang/<int:id>', views.GoodsDetailViews, name='detailBarang'),
    path('titip/', views.DepositViews, name= 'titip'),
    path('titip/<int:id>', views.DepositDetailViews, name='detailTitip'),
    path('terjual/', views.SoldViews, name='terjual'),
    path('terjual/<int:id>', views.SoldDetailViews, name='detailTerjual'),
    path('hutang', views.DebtViews, name='hutang'),
    path('hutang/<int:id>', views.DebtDetailViews, name='detailHutuang'),
]
