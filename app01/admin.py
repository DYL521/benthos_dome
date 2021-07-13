from django.apps import AppConfig
from django.contrib import admin

# Register your models here.
from app01.models import SummaryReportModel


def summary_report_view(request):
    pass


@admin.register(SummaryReportModel)
class SummaryReportAdmin(admin.ModelAdmin):
    """
    各街道汇总报表
    """

    def changelist_view(self, request, extra_context=None):
        return summary_report_view(request)