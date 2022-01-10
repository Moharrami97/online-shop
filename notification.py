# design pattern observer is used for everything that needed to be sent to the user.

from abc import ABC, abstractmethod


class Observer(ABC):
    @staticmethod
    @abstractmethod
    def send(message=""):
        pass


class EmailNotification(Observer):
    @staticmethod
    def send(message=""):
        print(f"sending email message {message}")


class SmsNotification(Observer):
    @staticmethod
    def send(message=""):
        print(f"sending SMS message {message}")


class PushNotification(Observer):
    @staticmethod
    def send(message=""):
        print(f"sending push message {message}")
