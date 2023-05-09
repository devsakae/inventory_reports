from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(produtos):
        report = SimpleReport.generate(produtos)
        report += "\nProdutos estocados por empresa:"
        allproducts = Counter([p["nome_do_produto"] for p in produtos])
        for name, qty in allproducts.items():
            report += f"\n- {name}: {qty}"
        return report
