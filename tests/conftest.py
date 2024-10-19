import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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
def third_product():
    return Product(
        name="Iphone 16",
        description="128GB, white",
        price=250000.0,
        quantity=2,
    )


@pytest.fixture
def fourth_product():
    grass = LawnGrass("Газонная трава", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    return grass


@pytest.fixture
def fifth_product():
    smartphone5 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    return smartphone5


@pytest.fixture
def sixth_product():
    smartphone6 = Smartphone("Iphone 11", "128GB, Green", 60000.0, 8, 70.2, "11", 128, "Green")
    return smartphone6


@pytest.fixture(scope="function")
def category1():

    return Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации,"
            " но и получение дополнительных функций для удобства жизни"
        ),
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB," " Gray space", 210000.0, 8),
        ],
    )


@pytest.fixture(scope="function")
def category2():

    return Category(
        name="Телевизоры",
        description=(
            "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
        ),
        products=[
            Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7),
        ],
    )


@pytest.fixture
def sum1():
    return 2580000.0


@pytest.fixture
def sum2():
    return 1400000.0


@pytest.fixture
def sum3():
    return 2180000.0


@pytest.fixture
def data():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации,"
            " но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром,"
            " станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]
