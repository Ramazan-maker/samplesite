from django.contrib import admin
from django.db.models import F
from django.urls import reverse

from .models import Bb, Rubric


class PriceListFilter(admin.SimpleListFilter):
    title = 'Категория цен'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('low', 'Низкая'), ('medium', 'средняя цена '), ('high', 'высокая цена')
        )

    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(price__lt=100)
        elif self.value() == 'medium':
            return queryset.filter(price__gte=500, price__lte=5000)
        elif self.value() == 'high':
            return queryset.filter(price__gte=5000)


class BbInline(admin.StackedInline):
    model = Bb
    # extra = 1
    verbose_name = 'Обьявление рубрики'
    verbose_name_plural = 'Добавить обяьвления'
    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 1
        return 3
@admin.register(Rubric)
class RubricsAdmin(admin.ModelAdmin):
    inlines = [BbInline]


@admin.register(Bb)
class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    # list_display = (#'title',
    #                 #'title_and_price',
    #                 #'__str__',
    #                 'title_and_rubric',
    #                 'price',
    #                 'published',
    #                 'rubric')
    #
    # list_display_links = ('title',
    #                       'content'
    #                       )
    # list_display_links = None
    # list_editable = ('title', 'content', 'price')
    search_fields = ('title', 'content')
    # ordering = ['title', 'rubric']
    # list_filter = ('title', 'rubric__name')

    list_filter = (PriceListFilter,)

    # list_per_page = 5
    # list_max_show_all = 200
    # actions_on_top = False
    # actions_on_bottom = True

    # fields = (('title', 'price'), 'content')
    # exclude = ('rubric', 'kind')
    readonly_fields = ('published',)
    # view_on_site = True
    # save_as = True

    actions = ('discount')
    def title_and_rubric(self, rec):
        return f'{rec.title} ({rec.rubric.name})'

    title_and_rubric.short_description = 'Название и рубрика'
    # title_and_rubric.admin_order_field = 'title'
    # title_and_rubric.admin_order_field = 'rubric__name'

    # def get_list_display(self, request):
    #     ld = ['title', 'content', 'price']
    #     if request.user.is_superuser:
    #         ld += ['published', 'rubric']
    #     return ld
    # def get_list_display_links(self, request, list_display):
    #     return list_display

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_active=True)

    # def get_fields(self, request, obj=None):
    #     f = ['title', 'content', 'price']
    #     if not obj:
    #         f.append('rubric')
    #     return f
    def view_on_site(self, rec):
        return reverse('bboard:bb-detail', kwargs={'pk': rec.pk})

    def discount(self, request, queryset):
        f = F('price')
        for rec in queryset:
            rec.price = f / 2
            rec.save()
        self.message_user(request, 'Действия выполнено!')

    discount.short_description = 'Уменьщить цену вдвое'

# admin.site.register(Bb, BbAdmin)
# admin.site.register(Rubric)
