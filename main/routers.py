from django.urls import path, include
from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class API(APIView):
    def get(self, request):
        patterns = {}
        for url in urlpatterns:
            pattern = str(url.pattern)
            if pattern and '$' not in pattern:
                patterns[pattern[:-1] if pattern[-1] == '/' else pattern] = f'{request.build_absolute_uri()}{pattern}'
        return Response(patterns)


schema_view = get_schema_view(
    openapi.Info(
        title="ZDRAVO CLINIC API",
        default_version='v1',
        description="ZDRAVO CLINIC API ОПИСАНИЕ",
    ),
    public=False,
    permission_classes=(permissions.IsAdminUser,),
)
urlpatterns = [
    path('', API.as_view()),
    path('', include('main.api')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
