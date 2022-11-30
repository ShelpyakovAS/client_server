import random
import threading
import time
from queue import Queue


class Client:
    """
    Класс создает клиента для отправки сообщений на сервер.
    Args:
        database: Queue
        client_name: str
    Attributes:
        self.database: Queue база данных для связи сервера и клиентов
        self.name: str имя клиента
        sef.status: str состояние клиента
    """
    def __init__(self, database: Queue, client_name='client'):
        self.database = database
        self.name = client_name
        self.status = 'stop'
        self.message_counter = 0

    def send_message(self):
        """
        Метод генерирует сообщение и передает его базу данных.
        :return: None
        """
        self.message_counter += 1
        message = f'{self.name} номер {self.message_counter}'
        self.database.put(message)

    def run(self):
        """
        Метод запускает _run_client в отдельном потоке.
        :return: None
        """
        if self.status != 'run':
            self.status = 'run'
            worker = threading.Thread(target=self._run_client)
            worker.start()
        else:
            print(f'{self.name} уже работает!')

    def _run_client(self):
        """
        Метод запускает постоянную генерацию и передачу их в базу данных пока метод не остановят.
        Для работы используется метод def send_message(self).
        :return: None
        """
        while self.status == 'run':
            self.send_message()
            time.sleep(random.randint(1, 3))

    def stop(self):
        """
        Метод останавливает метод def run.
        :return: None
        """
        self.status = 'stop'