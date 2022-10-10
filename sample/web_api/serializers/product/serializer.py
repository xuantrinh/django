from rest_framework import serializers
from ...models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['score'] >10:
            raise serializers.ValidationError("score is not existed in range 0-10.")
        return data
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'category': {
                'write_only': True
            }
        }
    
class ProductCreateSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ['category_id', 'name', 'title', 'price', 'image', 'score']
        
        extra_kwargs = {
            'category_id': {
            }
        }