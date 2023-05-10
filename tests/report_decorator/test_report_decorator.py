from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.json_importer import JsonImporter

dfma = "\033[32mData de fabricação mais antiga:\033[0m"
dfma_value = "\033[36m2020-09-06\033[0m"
dvmp = "\033[32mData de validade mais próxima:\033[0m"
dvmp_value = "\033[36m2023-09-17\033[0m"
ecmp = "\033[32mEmpresa com mais produtos:\033[0m"
ecmp_value = "\033[31mTarget Corporation\033[0m"


def test_decorar_relatorio():
    data = JsonImporter.import_data("./inventory_report/data/inventory.json")
    report = ColoredReport(SimpleReport)
    colored_report = report.generate(data)
    assert dfma in colored_report
    assert dfma_value in colored_report
    assert dvmp in colored_report
    assert dvmp_value in colored_report
    assert ecmp in colored_report
    assert ecmp_value in colored_report
