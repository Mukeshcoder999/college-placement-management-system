from django.urls import path
from .views import (
    StudentDashboardAPIView, CompanyDashboardAPIView, PlacementDashboardAPIView, 
    StudentReportAPIView, StudentExcelReportAPIView, StudentPDFReportAPIView, 
    CompanyReportAPIView, CompanyExcelReportAPIView, CompanyPDFReportAPIView,
    JobReportAPIView, JobExcelReportAPIView, JobPDFReportAPIView,
    ApplicationReportAPIView, ApplicationExcelReportAPIView, ApplicationPDFReportAPIView,
    DashboardSummaryAPIView, ApplicationStatusChartAPIView, MonthlyJobsAPIView,
)

urlpatterns = [
    path(
        "student-dashboard/",
        StudentDashboardAPIView.as_view(),
        name="student-dashboard", 
    ),
    path(
        "company-dashboard/",
        CompanyDashboardAPIView.as_view(),
        name="company-dashboard",
    ),
    path(
        "placement-dashboard/",
        PlacementDashboardAPIView.as_view(),
        name="placement-dashboard",
    ),
    path(
        "students/",
        StudentReportAPIView.as_view(),
        name="student-report",
    ),
    path(
        "students/excel/",
        StudentExcelReportAPIView.as_view(),
        name="students-excel-report",
    ),
    path(
        "students/pdf/",
        StudentPDFReportAPIView.as_view(),
        name="students-pdf-report",
    ),
    path(
        "companies/",
        CompanyReportAPIView.as_view(),
        name="company-report",
    ),

    path(
        "companies/excel/",
        CompanyExcelReportAPIView.as_view(),
        name="company-excel-report",
    ),

    path(
        "companies/pdf/",
        CompanyPDFReportAPIView.as_view(),
        name="company-pdf-report",
    ),
    path(
        "jobs/",
        JobReportAPIView.as_view(),
        name="job-report",
    ),

   path(
        "jobs/excel/",
        JobExcelReportAPIView.as_view(),
        name="job-excel-report",
    ),

   path(
        "jobs/pdf/",
        JobPDFReportAPIView.as_view(),
        name="job-pdf-report",
    ),
    path(
        "applications/",
        ApplicationReportAPIView.as_view(),
        name="application-report",
    ),

   path(
        "applications/excel/",
        ApplicationExcelReportAPIView.as_view(),
        name="application-excel-report",
   ),

    path(
        "applications/pdf/",
        ApplicationPDFReportAPIView.as_view(),
        name="application-pdf-report",
    ),
    path(
        "dashboard-summary/",
        DashboardSummaryAPIView.as_view(),
        name="dashboard-summary",
    ),
    path(
        "application-status-chart/",
        ApplicationStatusChartAPIView.as_view(),
        name="application-status-chart",
    ),
    path(
        "monthly-jobs-chart/",
        MonthlyJobsAPIView.as_view(),
        name="monthly-jobs-chart",
    ),

]
