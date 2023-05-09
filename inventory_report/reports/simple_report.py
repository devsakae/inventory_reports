from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(produtos):
        df = []
        dv = []
        empresas = {}
        for produto in produtos:
            df.append(produto["data_de_fabricacao"])
            if (
                datetime.strptime(produto["data_de_validade"], "%Y-%m-%d")
                >= datetime.today()
            ):
                dv.append(produto["data_de_validade"])
            if produto["nome_da_empresa"] not in empresas:
                empresas[produto["nome_da_empresa"]] = 0
            empresas[produto["nome_da_empresa"]] += 1

        return (
            f"Data de fabricação mais antiga: {min(df)}\n"
            f"Data de validade mais próxima: {min(dv)}\n"
            f"Empresa com mais produtos: {max(empresas, key=empresas.get)}"
        )
