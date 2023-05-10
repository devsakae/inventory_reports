from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        1,
        "Whisky",
        "Dewars",
        "2020-01-01",
        "2030-01-01",
        "00010120",
        "em local seco e arejado",
    )

    response = produto.__repr__()
    assert 'O produto Whisky fabricado em 2020-01-01' in response
    assert 'por Dewars com validade até 2030-01-01' in response
    assert 'precisa ser armazenado em local seco e arejado.' in response
