from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.response import Response


class QuerysetResponse:
    def __init__(
        self, viewset: viewsets.GenericViewSet, queryset: QuerySet, *args, **kwargs
    ):
        self.viewset = viewset
        self.queryset = queryset
        self.args = args
        self.kwargs = kwargs

    def response(self, *args, **kwargs) -> Response:
        return Response(
            self.viewset.get_serializer(self.queryset).data, *args, **kwargs
        )

    def many(self, *args, **kwargs) -> Response:
        serializer = self.viewset.get_serializer(
            self.queryset, many=True, *args, **kwargs
        )
        return Response(serializer.data)

    def paginated(self, *args, **kwargs) -> Response:
        page = self.viewset.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.viewset.get_serializer(page, many=True)
            return self.viewset.get_paginated_response(serializer.data)
        return self.many(*args, **kwargs)
