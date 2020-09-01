from .models import Info
import django_filters

class InfoFilter(django_filters.FilterSet):
    class Meta:
        model = Info
        fields = [ 'user_id' ]