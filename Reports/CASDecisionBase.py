import pandas as pd


class CASDecisionBase(object):
    model_lib = None
    model_table_name = None

    rule_name = None

    dependency = None
    input_table_name = None
    input_caslib = None

    output_table_name = None
    output_caslib = None

    def __init__(self, conn_warehouse, conn_viya):
        self.warehouse = conn_warehouse
        self.viya = conn_viya
        self.viya.conn.loadactionset('ds2')
        self.viya.conn.loadactionset('table')

        if self.dependency is None:
            return

        module = __import__('Reports')

        if hasattr(module, self.dependency):
            self.dependency_class = getattr(module, self.dependency)
            self.input_table_name = self.dependency_class.cas_table_name
            self.input_caslib = self.dependency_class.caslib
            d = self.dependency_class(self.warehouse, self.viya)
            d.update_from_source()

    def exec(self):
        self._clean_before_decision()
        self._run_model()

    def get_results(self):
        return pd.DataFrame(self.viya.conn.CASTable(name=self.output_table_name, caslib=self.output_caslib).to_records())

    # Drop existing tables
    def _clean_before_decision(self):
        self.viya.conn.table.dropTable(name=self.output_table_name)
        self.viya.conn.table.dropTable(name=self.output_table_name, caslib=self.output_caslib)

    # Run the Business Rule / Decision / Model against set input table
    # Promote output table for global use.
    def _run_model(self):
        self.viya.conn.ds2.runModel(
            modelName=self.rule_name,
            table={'caslib': self.input_caslib, 'name': self.input_table_name},
            modelTable={'caslib': self.model_lib, 'name': self.model_table_name},
            casOut={'name': self.output_table_name}
        )
        self.viya.conn.table.promote(
            targetlib=self.output_caslib,
            name=self.output_table_name
        )

    def run_dependencies(self):
        pass