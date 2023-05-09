from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith('.csv'):
            raise ValueError('Arquivo inválido')
        with open(path, mode="r") as file:
            return list(csv.DictReader(file))
