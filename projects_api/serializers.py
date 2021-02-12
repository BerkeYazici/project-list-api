from rest_framework import serializers

from projects_api import models

class PersonelSerializer(serializers.ModelSerializer):
    """Serializes a name field for personel"""

    class Meta:
        model = models.Personel
        fields = ('id', 'personel_adi')

class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = (
            'id',
            'proje_adi',
            'bolge',

        )


class ProjectDetailSerializer(serializers.ModelSerializer):
    proje_personeli = PersonelSerializer(many=True)
    class Meta:
        model = models.Project
        fields = (
            'id',
            'proje_adi',
            'bolge',
            'proje_muduru',
            'proje_mudur_yrd',   
            'proje_personeli',
        )
