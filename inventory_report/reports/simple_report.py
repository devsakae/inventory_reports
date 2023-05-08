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
        dfma = min(df)
        dvmp = min(dv)
        ecmp = max(empresas, key=empresas.get)

        return (
            f"Data de fabricação mais antiga: {dfma}\n"
            f"Data de validade mais próxima: {dvmp}\n"
            f"Empresa com mais produtos: {ecmp}"
        )
