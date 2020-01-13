class CASDecisionBase(object):
    model_lib = None
    model_table_name = None

    rule_name = None

    input_table_name = None
    input_caslib = None

    output_table_name = None
    output_caslib = None

    def __init__(self, viya_connection):
        self.viya = viya_connection
        self.viya.loadactionset('ds2')
        self.viya.loadactionset('table')

    def exec(self):
        self._clean_before_decision()
        self._run_model()

    def get_results(self):
        return self.viya.CASTable(name=self.output_table_name, caslib=self.output_caslib)

    # Drop existing tables
    def _clean_before_decision(self):
        self.viya.table.dropTable(name=self.output_table_name)
        self.viya.table.dropTable(name=self.output_table_name, caslib=self.output_caslib)

    # Run the Business Rule / Decision / Model against set input table
    # Promote output table for global use.
    def _run_model(self):
        self.viya.ds2.runModel(
            modelName=self.rule_name,
            table={'caslib': self.input_caslib, 'name': self.input_table_name},
            modelTable={'caslib': self.model_lib, 'name': self.model_table_name},
            casOut={'name': self.output_table_name}
        )
        self.viya.table.promote(
            targetlib=self.output_caslib,
            name=self.output_table_name
        )
