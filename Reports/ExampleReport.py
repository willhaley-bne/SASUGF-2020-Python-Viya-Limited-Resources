from .ReportBase import ReportBase
from .CASTableBase import CASTableBase


class ExampleReportTable(CASTableBase):
    source_sql = 'select top (10) from warehouse.dbo.orders'
    cas_table_name = 'SASUGF'
    caslib = ''


class ExampleReport(ReportBase):
    base_table = 'ExampleReportTable'

