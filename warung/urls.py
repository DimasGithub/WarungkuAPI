
from django.contrib import admin
from django.urls import path, include
from warung.views import warungView, warungDetail, CategoryDetailViews, CategoryViews, GoodsViews, GoodsDetailViews, SoldViews
from debt.views import DebtViews, DebtDetailViews
from deposit.views import DepositDetailViews, DepositViews
from stocker.views import StockerViews, StockerDetailViews
from debt.views import DebtViews
urlpatterns = [
    path('warung/', warungView, name='indexToko'),
    path('warung/<int:id>', warungDetail, name='detailToko'),
    path('kategori/', CategoryViews, name='kategori'),
    path('kategori/<int:id>', CategoryDetailViews, name='detailKategori'),
    path('stocker/', StockerViews, name='stocker'),
    path('stocker/<int:id>', StockerDetailViews, name='detailStocker'),
    path('barang/', GoodsViews, name='barang'),
    path('barang/<int:id>', GoodsDetailViews, name='detailBarang'),
    path('titip/', DepositViews, name= 'titip'),
    path('titip/<int:id>', DepositDetailViews, name='detailTitip'),
    path('terjual/<int:id>', SoldViews, name='terjual'),
    path('hutang', DebtViews, name='hutang'),
    path('hutang/<int:id>', DebtDetailViews, name='detailHutuang'),
]
