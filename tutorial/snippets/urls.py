from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from snippets import views
from snippets.views import SnippetViewSet, UserViewSet  # api_root
"""
snippet_list = SnippetViewSet.as_view({
    'get': 'retrieve',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
"""
"""
urlpatterns = [
    path('', views.api_root),
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    # path('snippets_classes/', views.SnippetList.as_view()),
    # path('snippets_classes/<int:pk>/', views.SnippetDetail.as_view()),
    # path('snippets_mix/', views.SnippetListMix.as_view()),
    # path('snippets_mix/<int:pk>/', views.SnippetDetailMix.as_view()),
    path('snippets_gen/', views.SnippetListGen.as_view(), name='snippet-list'),
    path('snippets_gen/<int:pk>/', views.SnippetDetailGen.as_view(), name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('snippets_gen/<int:pk>/highlight', views.SnippetHighLight.as_view(), name='snippet-highlight'),
]
"""
"""
urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippet/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippet/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])
"""

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='users')
urlpatterns = [
    path('', include(router.urls))
]
