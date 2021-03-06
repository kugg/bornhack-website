from psycopg2.extras import DateTimeTZRange

from django.db.models import QuerySet
from django.utils import timezone


class ProductQuerySet(QuerySet):

    def available(self):
        now = timezone.now()
        return self.filter(
            available_in__contains=DateTimeTZRange(now, None)
        )


class OrderQuerySet(QuerySet):

    def not_cancelled(self):
        return self.filter(cancelled=False)

    def open(self):
        return self.filter(open__isnull=True)

    def paid(self):
        return self.filter(paid=True)

    def unpaid(self):
        return self.filter(paid=False)

    def cancelled(self):
        return self.filter(cancelled=True)
