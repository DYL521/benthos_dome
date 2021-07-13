from django.apps import AppConfig
from django.contrib import admin

# Register your models here.
from django.shortcuts import render

from app01.models import SummaryReportModel


def summary_report_view(request):
    return render(request, "summary_report.html")


@admin.register(SummaryReportModel)
class SummaryReportAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        return summary_report_view(request)
