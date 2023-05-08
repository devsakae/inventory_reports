from inventory_report.inventory.product import Product


def test_cria_produto():
    arroz = Product(
        id=1,
        nome_do_produto="Kiarroz",
        nome_da_empresa="Fumacense",
        data_de_fabricacao=2023,
        data_de_validade=2024,
        numero_de_serie="0010052023",
        instrucoes_de_armazenamento="Guardar em local seco e arejado",
    )

    assert arroz.id == 1
    assert arroz.nome_do_produto == "Kiarroz"
    assert arroz.nome_da_empresa == "Fumacense"
