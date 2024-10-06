def test_category_init(test_category, first_product, second_product):
    assert test_category.name == "Смартфоны"
    assert (
        test_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert test_category.category_count == 1
    assert test_category.product_count == 2
