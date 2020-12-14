from rest_framework.views import APIView
from goods.serializers import GoodsSerializer,CategorySerializer,BannerSerializer
from .models import Goods,GoodsCategory,GoodsImage,GoodsCategoryBrand,Banner,HotSearchWords
from rest_framework import generics
from rest_framework import mixins
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .filters import GoodsFilter
from django_filters.rest_framework import DjangoFilterBackend


# class GoodsListView(APIView):
#     '''
#     商品列表
#     '''
#     def get(self,request,format=None):
#         goods = Goods.objects.all()
#         goods_serialzer = GoodsSerializer(goods,many=True)
#         return Response(goods_serialzer.data)

class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 10
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100



class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
    list:商品列表，分页，搜索，过滤，排序
    retrieve:获取商品详情
    '''
    #这里必须要定义一个默认的排序,否则会报错
    queryset = Goods.objects.all().order_by('id')
    # 分页
    pagination_class = GoodsPagination
    #序列化
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)

    # 设置filter的类为我们自定义的类
    #过滤
    filter_class = GoodsFilter
    #搜索
    search_fields = ('name', 'goods_brief', 'goods_desc')
    #排序
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:商品分类列表数据
    '''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页轮播图
    """
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer





























