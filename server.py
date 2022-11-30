import random
import time
from queue import Queue
import threading


class Server:
    """
    Класс создает сервер для обработки сообщений.
    Args:
        database: Queue
        server_name: str
        workers_count: int
    Attributes:
        self.database: Queue база данных для связи сервера и клиентов
        self.name: str имя сервера
        sef.status: str состояние сервера
        self.workers_count: int количество потоков для self.run
    """
    def __init__(self, database: Queue, server_name='server', workers_count=1):
        self.database = database
        self.name = server_name
        self.status = 'stop'
        self.workers_count = workers_count

    def get_message(self):
        """
        Метод получает сообщение из базы данных и обрабатывает его.
        :return: None
        """
        message = self.database.get()
        print(f'Сервер {self.name} обработал собщение от {message}')

    def run(self):
        """
        Метод запускает потоки обработки сообщений
        :return: None
        """
        if self.status != 'run':
            self.status = 'run'
            for worker in self.workers():
                worker.start()
        else:
            print(f'{self.name} уже работает!')

    def _run_server(self):
        """
        Метод запускает постоянное получение и обработку сообщений их в базу данных пока метод не остановят.
        Для работы используется метод def get_message(self).
        :return: None
        """
        while self.status == 'run':
            self.get_message()
            time.sleep(random.randint(1, 3))

    def stop(self):
        """
        Метод останавливает метод def run.
        :return: None
        """
        self.status = 'stop'

    def workers(self):
        """
        Метод создает потоки обрабоки сообщений согласно self.workers_count
        :return: list - threading.Thread
        """
        return [threading.Thread(target=self._run_server) for i in range(self.workers_count)]
