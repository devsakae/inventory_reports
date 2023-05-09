from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith('.json'):
            raise ValueError('Arquivo inválido')
        with open(path, mode="r") as file:
            return json.load(file)
