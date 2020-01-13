from .ReportBase import ReportBase
from .CASTableBase import CASTableBase
from .CASDecisionBase import CASDecisionBase


class MarketingProductTrackingData(CASTableBase):
    source_sql = 'select ' \
                 '      BusinessDate, ' \
                 '      StoreNum, ' \
                 '      TransactionHour, ' \
                 '      MenuID, ' \
                 '      MenuDescription, ' \
                 '      count(QuantitySold)' \
                 '  FROM marketing_datamart.dbo.sales' \
                 '  WHERE BusinessDate >= LAST_TWO_WEEKS' \
                 '  GROUP BY ' \
                 '      BusinessDate, ' \
                 '      StoreNum, ' \
                 '      TransactionHour, ' \
                 '      MenuID, ' \
                 '      MenuDescription'

    cas_table_name = 'Marketing Two Week Product Tracking'
    caslib = 'Marketing'


class MarketingProductDecision(CASDecisionBase):
    model_lib = 'Public'
    model_table_name = 'dm_table'

    rule_name = 'MarketingProductTrackingItemList1_0'

    input_table_name = 'Menu Items'
    input_caslib = 'Marketing'

    output_table_name = 'Marketing Product Tracking Menu Items'
    output_caslib = 'Marketing'


class MarketingProductTracking(ReportBase):

    def preprocess(self):
        selected_menu_items_decision = MarketingProductDecision(self.conn_viya)
        selected_menu_items_decision.exec()
        selected_menu_items = selected_menu_items_decision.get_results().query('IncludeInReport = 1')
        self.base_data = self.base_data.merge(selected_menu_items, on='MenuID')
