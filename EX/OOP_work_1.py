class BankAccount:
    """Класс для управления банковским счетом клиента."""

    def __init__(self, client_id, client_first_name, client_last_name, balance=0.0):
        """
        Инициализация банковского счета.

        Args:
            client_id: ID клиента
            client_first_name: Имя клиента
            client_last_name: Фамилия клиента
            balance: Начальный баланс (по умолчанию 0.0)
        """
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = balance

    def deposit(self, amount):
        """
        Пополнение счета.

        Args:
            amount: Сумма пополнения

        Returns:
            bool: True если операция успешна
        """
        if amount <= 0:
            print("Сумма пополнения должна быть положительной")
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        """
        Снятие средств со счета.

        Args:
            amount: Сумма для снятия

        Returns:
            bool: True если операция успешна, False если недостаточно средств
        """
        if amount <= 0:
            print("Сумма снятия должна быть положительной")
            return False
        if amount > self.balance:
            print(f"Недостаточно средств. Доступно: {self.balance:.2f}")
            return False
        self.balance -= amount
        return True

    def get_balance(self):
        """Получить текущий баланс."""
        return self.balance

    def get_full_name(self):
        """Получить полное имя клиента."""
        return f"{self.client_first_name} {self.client_last_name}"

    def __str__(self):
        """Строковое представление счета."""
        return (f"Счет #{self.client_id}: {self.get_full_name()}, "
                f"Баланс: {self.balance:.2f}₽")

    def __repr__(self):
        """Техническое представление объекта."""
        return (f"BankAccount({self.client_id}, "
                f"'{self.client_first_name}', "
                f"'{self.client_last_name}', {self.balance})")

# Пример использования
bank_1 = BankAccount(1, "John", "Smith", 1000)
print(bank_1)  # Красивый вывод информации о счете

bank_1.deposit(100)
print(f"После пополнения: {bank_1.get_balance():.2f}₽")

bank_1.withdraw(100)
print(f"После снятия: {bank_1.get_balance():.2f}₽")

# Попытка снять больше, чем есть на счете
bank_1.withdraw(2000)

print(f"\nПолное имя клиента: {bank_1.get_full_name()}")
print(f"Итоговый баланс: {bank_1.balance:.2f}₽")
