from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры

    class AdvertisementFilter(filters.FilterSet):
        status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)
        created_at = filters.DateFromToRangeFilter()

        class Meta:
            model = Advertisement
            fields = ['status', 'created_at', 'creator']
