def test_category_count(category1, category2):
    assert category1.category_count == 2
    assert category2.category_count == 2


def test_product_count(category1, category2):
    assert category1.product_count == 6
    assert category2.product_count == 6


def test_category_init(category1, category2):
    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert category2.name == "Телевизоры"
    assert category2.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
