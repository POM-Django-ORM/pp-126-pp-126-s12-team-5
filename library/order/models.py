from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime

# Модель для замовлення
class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')  # Зв'язок з користувачем
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='orders')  # Зв'язок з книгою
    created_at = models.DateTimeField(auto_now_add=True)  # Дата створення замовлення
    end_at = models.DateTimeField(null=True, blank=True)  # Дата повернення книги (після реального повернення)
    plated_end_at = models.DateTimeField()  # Запланована дата повернення книги
    
    def __str__(self):
        """
        Magic method is redefined to show all information about Order.
        :return: order id, user, book, created_at, end_at, plated_end_at
        """
        return f"Order {self.id} for {self.user} - {self.book.name}"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Order object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'

    def to_dict(self):
        """
        :return: dict contains order id, book id, user id, order created_at, order end_at, order plated_end_at
        :Example:
        | {
        |   'id': 8,
        |   'book': 8,
        |   'user': 8',
        |   'created_at': 1509393504,
        |   'end_at': 1509393504,
        |   'plated_end_at': 1509402866,
        | }
        """
        return {
            'id': self.id,
            'book': self.book.id,
            'user': self.user.id,
            'created_at': int(self.created_at.timestamp()),
            'end_at': int(self.end_at.timestamp()) if self.end_at else None,
            'plated_end_at': int(self.plated_end_at.timestamp()),
        }

    @staticmethod
    def create(user, book, plated_end_at):
        """
        Creates and returns a new order object which is also written into the DB.
        :param user: the user who took the book
        :type user: CustomUser
        :param book: the book they took
        :type book: Book
        :param plated_end_at: planned return of data
        :type plated_end_at: int (timestamp)
        :return: new order object
        """
        order = Order.objects.create(
            user=user,
            book=book,
            plated_end_at=datetime.fromtimestamp(plated_end_at),
        )
        return order

    @staticmethod
    def get_by_id(order_id):
        """
        :param order_id: ID замовлення
        :type order_id: int
        :return: об'єкт замовлення або None, якщо замовлення не знайдено
        """
        try:
            return Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return None

    def update(self, plated_end_at=None, end_at=None):
        """
        Оновлює замовлення в базі даних з зазначеними параметрами.
        :param plated_end_at: нова запланована дата повернення
        :type plated_end_at: int (timestamp)
        :param end_at: реальна дата повернення
        :type end_at: int (timestamp)
        :return: None
        """
        if plated_end_at:
            self.plated_end_at = datetime.fromtimestamp(plated_end_at)
        if end_at:
            self.end_at = datetime.fromtimestamp(end_at)
        self.save()

    @staticmethod
    def get_all():
        """
        :return: всі замовлення
        """
        return Order.objects.all()

    @staticmethod
    def get_not_returned_books():
        """
        :return: всі замовлення, де не вказана дата повернення
        """
        return Order.objects.filter(end_at__isnull=True)

    @staticmethod
    def delete_by_id(order_id):
        """
        Видаляє замовлення по ID.
        :param order_id: ID замовлення
        :type order_id: int
        :return: True, якщо замовлення було видалено, False якщо не знайдено
        """
        order = Order.get_by_id(order_id)
        if order:
            order.delete()
            return True
        return False
