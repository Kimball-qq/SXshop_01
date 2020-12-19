from django.urls import path,include,re_path
import xadmin
from django.views.static import serve
from SXshop.settings import MEDIA_ROOT,STATICFILES_DIRS
# from goods.view_base import GoodsListView

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token
from user.views import SmsCodeViewset,UserViewset
from user_operation.views import UserFavViewset,LeavingMessageViewset,AddressViewset
from goods.views import GoodsListViewSet,CategoryViewSet,BannerViewset,IndexCategoryViewset
from trade.views import ShoppingCartViewset,OrderViewset,AlipayView
from django.views.generic import TemplateView

router = DefaultRouter()

#配置goods的url
router.register(r'goods', GoodsListViewSet,basename='goods')
# 配置Category的url
router.register(r'categorys', CategoryViewSet, basename="categorys")

# 配置codes的url
router.register(r'code', SmsCodeViewset, basename="code")
#配置用户的url
router.register(r'users', UserViewset, basename="users")
# 配置用户收藏的url
router.register(r'userfavs', UserFavViewset, basename="userfavs")
# 配置用户留言的url
router.register(r'messages', LeavingMessageViewset, basename="messages")
# 配置收货地址
router.register(r'address',AddressViewset , basename="address")

# 配置购物车的url
router.register(r'shopcarts', ShoppingCartViewset, basename="shopcarts")
#配置订单URL
router.register(r'orders', OrderViewset, basename="orders")

# 配置首页轮播图的url
router.register(r'banners', BannerViewset, basename="banners")
# 首页系列商品展示url
router.register(r'indexgoods', IndexCategoryViewset, basename="indexgoods")


urlpatterns = [

    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    # 文件
    re_path('^static/(?P<path>.*)$', serve, {'document_root': STATICFILES_DIRS}, name='static'),
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),

    # drf文档，title可自定义
    path('docs/',include_docs_urls(title='生鲜超市')),
    path('api-auth/',include('rest_framework.urls')),

    # token
    path('api-token-auth/',obtain_auth_token),
    # jwt的token认证接口
    path('jwt-auth/',obtain_jwt_token),
    # jwt的认证接口
    path('login/',obtain_jwt_token),

    re_path('^',include(router.urls)),
    #支付宝支付
    path('alipay/return/', AlipayView.as_view()),
    # 首页
    path('index/', TemplateView.as_view(template_name='index.html'),name='index')
]
