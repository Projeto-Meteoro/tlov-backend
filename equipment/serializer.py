from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    power = serializers.DecimalField(max_digits=3, decimal_places=1)
    equipment = serializers.CharField(max_length=50)
    data_created = serializers.DateTimeField()
    status = serializers.BooleanField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)