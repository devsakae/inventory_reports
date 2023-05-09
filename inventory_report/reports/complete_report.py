from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(produtos):
        report = SimpleReport.generate(produtos)
        report += "\nProdutos estocados por empresa:\n"
        allproducts = Counter([p["nome_da_empresa"] for p in produtos])
        for name, qty in allproducts.items():
            report += f"- {name}: {qty}\n"
        return report
