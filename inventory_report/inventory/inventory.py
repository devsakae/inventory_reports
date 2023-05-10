from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        file = {
            "csv": CsvImporter,
            "json": JsonImporter,
            "xml": XmlImporter
        }
        filetype = path.split(".")[1]
        if type == "simples":
            return SimpleReport.generate(file[filetype].import_data(path))
        if type == "completo":
            return CompleteReport.generate(file[filetype].import_data(path))
