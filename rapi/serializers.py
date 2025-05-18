from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework import serializers


class SnippetSerailizer(serializers.ModelSerializer):
    """
    Here we are using restframework model serializer"""

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

