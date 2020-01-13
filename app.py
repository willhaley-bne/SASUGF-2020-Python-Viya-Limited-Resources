import click
from Connections.ConnectionFactory import ConnectionFactory


@click.command()
@click.option('--report', default="test", help="Selects the report or dataset to update")
def app(report):

    module_obj = __import__('Reports')

    if hasattr(module_obj, report):
        report_module = getattr(module_obj, report)

        report_class = report_module(ConnectionFactory())
        report_class.run()
        return

    raise Exception('Requested Report Does Not Exist')


if __name__ == '__main__':
    app("test", False)
