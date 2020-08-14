from rest_framework import serializers

from .models import Blogpost


class BlogpostSerialier(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = ('id', 'post_title', 'psot_desscription')
