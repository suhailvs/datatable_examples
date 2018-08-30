from django.shortcuts import render
from myapp.models import Blog
# Create your views here.

from django_datatables_view.base_datatable_view import BaseDatatableView

class OrderListJson(BaseDatatableView):
    # The model we're going to show
    model = Blog

    # define the columns that will be returned
    columns = ['name', 'tagline',]

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = ['name', '']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    def render_column(self, row, column):
        if column == 'id':
            return '<input type="checkbox" name="cid[]" value="%s" class="cid_checkbox flat"/>' % row.id
        # elif column == 'status':
        #    return 'Publish' if int(row.status) == 1 else 'UnPublish'
        else:
            return super().render_column(row, column)

    def filter_queryset(self, qs):
        """
        filter_trashed = self.request.GET.get(u'filter_trashed', None)

        if (filter_trashed == '1'):
            qs = qs.filter(deleted_at__isnull=False)
        else:
            qs = qs.filter(deleted_at__isnull=True)
        """
        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)
        return qs