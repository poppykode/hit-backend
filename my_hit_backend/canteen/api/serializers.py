from rest_framework import serializers
from canteen.models import Meal


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'user', 'number_of_meals',
                  'total_cost', 'paid', 'timestamp')
