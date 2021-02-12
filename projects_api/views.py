from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from projects_api import serializers
from projects_api import models

class PersonelListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PersonelSerializer
    queryset = models.Personel.objects.all()

class ProjectListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectListSerializer
    detail_serializer_class = serializers.ProjectDetailSerializer
    queryset = models.Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class

        return super(ProjectListViewSet, self).get_serializer_class()
