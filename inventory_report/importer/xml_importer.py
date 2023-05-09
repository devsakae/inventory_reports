import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith('.xml'):
            raise ValueError('Arquivo inválido')
        # with open(path, mode="r") as file:
        #     return xmltodict.parse(file)["dataset"]["record"]
        fileread = open(path).read()
        return xmltodict.parse(fileread)["dataset"]["record"]
