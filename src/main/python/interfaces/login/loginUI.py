from fbs_runtime.application_context.PyQt5 import ApplicationContext

from abc import ABCMeta, abstractmethod

from PyQt5.QtCore import pyqtSignal
from ..widgets import Frame, MoveAnimation
from PyQt5.QtWidgets import QDialog
from .loginPageUI import LoginPageUI
from .loginCreateUI import CreatePageUI

class LoginUI(QDialog):
    
     # metaclass for defining abstract base classes
    __metaclass__ = ABCMeta
    
    login: Frame = None
    create: Frame = None

    _to_login_signal = pyqtSignal()
    _to_create_signal = pyqtSignal()

    def __init__(self, cxt:ApplicationContext, *args, **kwargs):
        super(LoginUI, self).__init__(*args, **kwargs)

        self.setObjectName("dialog")
        self.cxt = cxt

        self._to_login_signal.connect(self.to_login)
        self._to_create_signal.connect(self.to_create)

        self.login = LoginPageUI(self, self._to_create_signal, self.cxt)

        # connect function
        # self.login.login_button.clicked.connect(self.login_action)
        # self.login.to_create_button.clicked.connect(self.to_create)

        self.create = CreatePageUI(self, self._to_login_signal, self.cxt)

        # connect function
        # self.create.create_button.clicked.connect(self.create_action)
        # self.create.to_login_button.clicked.connect(self.to_login)

        self._init_ui()
        self.setStyleSheet(self.cxt.login_style)

    @abstractmethod
    def login_action(self):
        pass

    @abstractmethod
    def create_action(self):
        pass

    def _init_ui(self):
        # set window init size
        self.resize(580, 580)

        # set window resize constrains
        self.setFixedSize(580, 580)

        # set title name
        self.setWindowTitle("Login")

        # set login initial position
        self.login.move(0, 0)

        # set create initial position
        self.create.move(0-self.width(), 0)

    def to_login(self):
        self._build_check()
        # self.clean_create_page()

        login_animation = MoveAnimation(self.login, self.width(), 0, 0, 0)
        create_animation = MoveAnimation(self.create, 0, 0, 0 - self.width(), 0)

        login_animation.start()
        create_animation.start()

    def to_create(self):
        self._build_check()

        login_animation = MoveAnimation(self.login, 0, 0, self.width(), 0)
        create_animation = MoveAnimation(self.create, 0-self.width(), 0, 0, 0)

        login_animation.start()
        create_animation.start()

    def _build_check(self):
        not self.login or not self.create and print(
            "Error: either login/create has not been set!"
        )