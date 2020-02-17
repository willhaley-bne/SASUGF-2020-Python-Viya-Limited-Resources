from .ReportBase import ReportBase
from .CASTableBase import CASTableBase
from .CASDecisionBase import CASDecisionBase


class MarketingProductDecision(CASDecisionBase):
    model_lib = 'Public'
    model_table_name = 'dm_table'

    rule_name = 'MarketingProductTrackingItemList1_0'

    input_table_name = 'Menu Items'
    input_caslib = 'Marketing'

    output_table_name = 'Marketing Product Tracking Menu Items'
    output_caslib = 'Marketing'


class MarketingProductionMenuItems(CASTableBase):
    decision_source = 'MarketingProductDecision'

    def post_process_source_data(self):
        self.source_data = self.source_data.query('InReport == 1')


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

    def post_process_source_data(self):
        menu_items_data = MarketingProductionMenuItems(self.conn_db, self.conn_viya)
        self.source_data = self.source_data.merge(menu_items_data.get_source_data(), on="MenuID")


class MarketingProductTracking(ReportBase):

    base_table = 'MarketingProductTrackingData'
