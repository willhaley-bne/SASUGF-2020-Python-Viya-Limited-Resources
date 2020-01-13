from .ReportBase import ReportBase
from .CASTableBase import CASTableBase


class MarketingMenuItemsData(CASTableBase):
    source_sql = 'SELECT ' \
                 '      MenuID, ' \
                 '      MenuDesc, ' \
                 '      MenuCategory' \
                 '      MenuPrice' \
                 '      ActiveDate' \
                 '      RetiredDate' \
                 '  from marketing_datamart.dbo.menu_items'

    cas_table_name = 'Menu Items'
    caslib = 'Marketing'


class MarketingMenuItems(ReportBase):
    base_table = 'MarketingMenuItemsData'
