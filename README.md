# OOP

### Установка
Клонируйте репозиторий: git@github.com:jirotakeo/OOP_SP.git


### Описание:
- Класс продуктов `Product`.
- Метод `__add__` для класса `Product` складывает стоимость товаров одного класса, иначе вызывает ошибку `TypeError`.
- Метод `__str__` для класса `Product` выводит строковое отображения в определенном формате.
- Метод `new_product` создает объект класса Product из словаря.
- Метод `price` меняет стоимость товара.
- Класс категорий `Category`.
- Метод `__str__` для класса `Category` выводит строковое отображения в определенном формате,
  где количество продуктов считается из общего числа всех продуктов на складе.
- Метод `add_product` добавляет продукт в категорию, таким образом.
  Реализован так, чтобы не было возможности добавить вместо продукта любой другой объект, в таком случае вызывает ошибку `TypeError`.
- Метод `products` выводит список продуктов в данной категории.
- В `utils.py` реализован функционал для считывания данных из JSON-файла.
- Класс `Smartphone` наследник класса `Product`.
- Класс `LawnGrass` наследник класса `Product`.

### Тестирование:
Для тестирования используется pytest.

Введите в терминале команду `pytest`, чтобы запустить тесты.
