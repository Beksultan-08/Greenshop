from django.db import models


class Checkout(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name='Фамилия'
    )
    country = models.CharField(
        max_length=255,
        verbose_name='Страна'
    )
    street_address = models.CharField(
        max_length=255,
        verbose_name='Улица и номер дома'
    )
    city = models.CharField(
        max_length=255,
        verbose_name='Город'
    )
    mail_index = models.IntegerField(
        verbose_name='Почтовый индекс'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Электронная почта'
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )
    order_notes = models.TextField(
        verbose_name='Примечания к заказу',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        bot_token = '7840260904:AAFAtkwX8pJXR0EBKN2_bDB39cfhy-TLdmI'
        chat_id = '7076712137'

        bot = telebot.Telebot(bot_token)
        message_text = (f"ФИО: {self.first_name} {self.last_name}\n"
                        f"Номер: {self.phone_number}\n"
                        f"Страна {self.country}\n"
                        f'Город {self.city}\n'
                        f'Адрес {self.street_address}\n,'
                        f'Почтовый индекс {self.mail_index}\n'
                        f'Электронная почта {self.email}\n'
                        f'{self.order_notes if self.order_notes else None}')
        bot.send_message()