from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        if path.endswith(".csv"):
            produtos = CsvImporter.import_data(path)
        if path.endswith(".json"):
            produtos = JsonImporter.import_data(path)
        if path.endswith(".xml"):
            produtos = XmlImporter.import_data(path)
        if type == "simples":
            return SimpleReport.generate(produtos)
        if type == "completo":
            return CompleteReport.generate(produtos)
