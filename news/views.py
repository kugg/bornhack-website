from django.views.generic import ListView, DetailView
from django.utils import timezone
from . import models


class NewsIndex(ListView):
    model = models.NewsItem
    template_name = 'news_index.html'
    context_object_name = 'news_items'

    def get_queryset(self):
        return self.model.objects.public()


class NewsDetail(DetailView):
    model = models.NewsItem
    template_name = 'news_detail.html'
    context_object_name = 'news_item'

    def get_context_data(self, **kwargs):
        context = super(NewsDetail, self).get_context_data(**kwargs)
        news_item = self.get_object()
        timed = news_item.published_at > timezone.now()

        if news_item.public and timed:
            context['not_public'] = True
            context['timed'] = True
        elif not news_item.public:
            context['not_public'] = True
            context['timed'] = False

        return context

