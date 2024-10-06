import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture()
def second_product():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
    )


@pytest.fixture()
def test_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            {"Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5},
            {"Iphone 15", "512GB, Gray space", 210000.0, 8},
        ],
    )
