# Импорт необходимых библиотек

from os.path import basename
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTextEdit, QMenu, QMessageBox
from PyQt5.QtWidgets import QFileDialog, QFontDialog
from PyQt5.QtWidgets import QAction, QToolBar
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtPrintSupport import QPrintDialog

# Название приложения
APP_NAME = 'Simplopad'

# Информация о приложении
APP_INFO = """Simplopad - simple text editor and a basic text-editing program. \
It helps computer users to create and edit text documents and print them on paper.\n
The resulting files are saved with the ".txt" extension.\n
Simplopad also supports multi-font text."""


# Класс "Simplopad"
class Simplopad(QMainWindow):
    def __init__(self):
        super().__init__()

        # Установка иконки программы
        self.setWindowIcon(QIcon('icons/main_icon.png'))

        # Установка дефолтного шрифта,
        # который пользователь будет использовать при написании текста
        self.text_font = QFont("Lucida Console", 10, QFont.Normal)

        # Создание виджета QTextEdit, где пользователь будет писать текст,
        # иными словами, создание рабочей области
        self.text_editor = QTextEdit()

        # Установка рабочей области как центральный виджет окна приложения
        self.setCentralWidget(self.text_editor)

        # Путь к открытому на данный момент файлу
        self.path_to_file = ''

        # Имя открытого на данный момент файла
        self.file_name = ''

        # Добавление в строку меню пункта "Файл (File)"
        self.menu_FILE = self.menuBar().addMenu('File')

        # Создание в панели инструментов группы инструментов "Файл (File)"
        self.tools_FILE = QToolBar('File')

        # Установка размеров иконок инструментов группы "Файл (File)"
        self.tools_FILE.setIconSize(QSize(16, 16))

        # Инструмент "Создать (Create)"
        self.action_create_file = QAction(QIcon('icons/create_file.png'), 'Create', self)
        self.action_create_file.triggered.connect(self.create_file)
        self.menu_FILE.addAction(self.action_create_file)
        self.tools_FILE.addAction(self.action_create_file)

        # Инструмент "Открыть... (Open...)"
        self.action_open_file = QAction(QIcon('icons/open_file_icon.jpg'), 'Open...', self)
        self.action_open_file.triggered.connect(self.open_file)
        self.menu_FILE.addAction(self.action_open_file)
        self.tools_FILE.addAction(self.action_open_file)

        # Инструмент "Сохранить (Save)"
        self.action_save_file = QAction(QIcon('icons/save_file_icon.jpg'), 'Save', self)
        self.action_save_file.triggered.connect(self.save_file)
        self.menu_FILE.addAction(self.action_save_file)
        self.tools_FILE.addAction(self.action_save_file)

        # Инструмент "Сохранить как... (Save as...)"
        self.action_save_as = QAction(QIcon('icons/save_as_icon.png'), 'Save as...', self)
        self.action_save_as.triggered.connect(self.file_save_as)
        self.menu_FILE.addAction(self.action_save_as)
        self.tools_FILE.addAction(self.action_save_as)

        # Инструмент "Печать... (Print...)"
        self.action_print = QAction(QIcon('icons/print_icon.png'), 'Print...', self)
        self.action_print.triggered.connect(self.print_file)
        self.menu_FILE.addAction(self.action_print)
        self.tools_FILE.addAction(self.action_print)

        # Добавление в меню "Файл (File)" разделителя
        self.menu_FILE.addSeparator()

        # Инструмент "Закрыть окно (Close)"
        self.action_close = QAction(QIcon('icons/close_icon.jpg'), 'Close', self)
        self.action_close.triggered.connect(self.close)
        self.menu_FILE.addAction(self.action_close)
        self.tools_FILE.addAction(self.action_close)

        # Добавление в панель инструментов группы инструментов "Файл (File)"
        self.addToolBar(self.tools_FILE)

        # Добавление в строку меню пункта "Правка (Edit)"
        self.menu_EDIT = self.menuBar().addMenu('Edit')

        # Создание в панели инструментов группы инструментов "Правка (Edit)"
        self.tools_EDIT = QToolBar('Edit')

        # Установка размеров иконок инструментов группы "Правка (Edit)"
        self.tools_EDIT.setIconSize(QSize(16, 16))

        # Инструмент "Отменить изменение (Undo)"
        self.action_undo = QAction(QIcon('icons/undo_icon.png'), 'Undo', self)
        self.action_undo.triggered.connect(self.text_editor.undo)
        self.menu_EDIT.addAction(self.action_undo)
        self.tools_EDIT.addAction(self.action_undo)

        # Инструмент "Вернуть изменение (Redo)"
        self.action_redo = QAction(QIcon('icons/redo_icon.png'), 'Redo', self)
        self.action_redo.triggered.connect(self.text_editor.redo)
        self.menu_EDIT.addAction(self.action_redo)
        self.tools_EDIT.addAction(self.action_redo)

        # Добавление в меню "Правка (Edit)" 1-ого разделителя
        self.menu_EDIT.addSeparator()

        # Инструмент "Вырезать (Cut)"
        self.action_cut = QAction(QIcon('icons/cut_icon.png'), 'Cut', self)
        self.action_cut.triggered.connect(self.text_editor.cut)
        self.menu_EDIT.addAction(self.action_cut)
        self.tools_EDIT.addAction(self.action_cut)

        # Инструмент "Копировать (Copy)"
        self.action_copy = QAction(QIcon('icons/copy_icon.png'), 'Copy', self)
        self.action_copy.triggered.connect(self.text_editor.copy)
        self.menu_EDIT.addAction(self.action_copy)
        self.tools_EDIT.addAction(self.action_copy)

        # Инструмент "Вставить (Paste)"
        self.action_paste = QAction(QIcon('icons/paste_icon.png'), 'Paste', self)
        self.action_paste.triggered.connect(self.text_editor.paste)
        self.menu_EDIT.addAction(self.action_paste)
        self.tools_EDIT.addAction(self.action_paste)

        # Инструмент "Удалить всё (Clear all)"
        self.action_clear_all = QAction(QIcon('icons/clear_icon.png'), 'Clear all', self)
        self.action_clear_all.triggered.connect(self.text_editor.clear)
        self.menu_EDIT.addAction(self.action_clear_all)
        self.tools_EDIT.addAction(self.action_clear_all)

        # Добавление в меню "Правка (Edit)" 2-ого разделителя
        self.menu_EDIT.addSeparator()

        # Инструмент "Выделить всё (Select all)"
        self.action_select_all = QAction(QIcon('icons/select_all_icon.png'), 'Select all', self)
        self.action_select_all.triggered.connect(self.text_editor.selectAll)
        self.menu_EDIT.addAction(self.action_select_all)
        self.tools_EDIT.addAction(self.action_select_all)

        # Добавление в панель инструментов группы инструментов "Правка (Edit)"
        self.addToolBar(self.tools_EDIT)

        # Добавление в строку меню пункта "Формат (Format)"
        self.menu_FORMAT = self.menuBar().addMenu('Format')

        # Создание в панели инструментов группы инструментов "Формат (Format)"
        self.tools_FORMAT = QToolBar('Format')

        # Установка размеров иконок инструментов группы "Формат (Format)"
        self.tools_FORMAT.setIconSize(QSize(16, 16))

        # Инструмент "Выбрать шрифт (Font)"
        self.action_choose_font = QAction(QIcon('icons/font_icon.png'), 'Font', self)
        self.action_choose_font.triggered.connect(self.choose_font)
        self.menu_FORMAT.addAction(self.action_choose_font)
        self.tools_FORMAT.addAction(self.action_choose_font)

        # Добавление в панель инструментов группы инструментов "Формат (Format)"
        self.addToolBar(self.tools_FORMAT)

        # Добавление в строку меню пункта "Вид (View)"
        self.menu_VIEW = self.menuBar().addMenu('View')

        # Создание в панели инструментов группы инструментов "Вид (View)"
        self.tools_VIEW = QToolBar('View')

        # Установка размеров иконок инструментов группы "Вид (View)"
        self.tools_VIEW.setIconSize(QSize(16, 16))

        # Создание в меню "Вид (View)" подменю "Масштаб (Scale)"
        self.submenu_SCALE = QMenu('Scale', self)
        self.submenu_SCALE.setIcon(QIcon('icons/scale_icon.png'))

        # Добавление подменю "Масштаб (Scale)" в меню "Вид (View)"
        self.menu_VIEW.addMenu(self.submenu_SCALE)

        # Инструмент "Увеличить масштаб (Zoom in)"
        self.action_zoom_in = QAction(QIcon('icons/zoom_in_icon.png'), 'Zoom in', self)
        self.action_zoom_in.triggered.connect(self.text_editor.zoomIn)
        self.submenu_SCALE.addAction(self.action_zoom_in)
        self.tools_VIEW.addAction(self.action_zoom_in)

        # Инструмент "Уменьшить масштаб (Zoom out)"
        self.action_zoom_out = QAction(QIcon('icons/zoom_out_icon.png'), 'Zoom out', self)
        self.action_zoom_out.triggered.connect(self.text_editor.zoomOut)
        self.submenu_SCALE.addAction(self.action_zoom_out)
        self.tools_VIEW.addAction(self.action_zoom_out)

        # Добавление в панель инструментов группы инструментов "Вид (View)"
        self.addToolBar(self.tools_VIEW)

        # Добавление в строку меню пункта "Справка (Info)"
        self.menu_INFO = self.menuBar().addMenu('Info')

        # Инструмент "О программе (About Simplopad)"
        self.action_about_box = QAction(QIcon('icons/question_icon.png'), 'About Simplopad', self)
        self.action_about_box.triggered.connect(self.show_info_about_app)
        self.menu_INFO.addAction(self.action_about_box)

        # Подменю "Информация о функциях работы с файлом (File work functions info)"
        # меню "Справка (Help)"
        self.submenu_FUN_INFO = QMenu('File work functions info', self)
        self.submenu_FUN_INFO.setIcon(QIcon('icons/main_icon.png'))

        # Добавление подменю "Информация о функциях работы с файлом (File work functions info)"
        # в меню "Справка (Help)"
        self.menu_INFO.addMenu(self.submenu_FUN_INFO)

        # Инструмент "Информация о функции "Открыть..." ("Open..." function info)"
        self.action_info_open_file = QAction(QIcon('icons/open_file_icon.jpg'),
                                             '"Open..." function info', self)
        self.action_info_open_file.triggered.connect(self.show_info_open_file)
        self.submenu_FUN_INFO.addAction(self.action_info_open_file)

        # Инструмент "Информация о функции "Сохранить" ("Save" function info)"
        self.action_info_save_file = QAction(QIcon('icons/save_file_icon.jpg'),
                                             '"Save" function info', self)
        self.action_info_save_file.triggered.connect(self.show_info_save_file)
        self.submenu_FUN_INFO.addAction(self.action_info_save_file)

        # Инструмент "Информация о функции "Сохранить как..." ("Save as..." function info)"
        self.action_info_save_as = QAction(QIcon('icons/save_as_icon.png'),
                                           '"Save as..." function info', self)
        self.action_info_save_as.triggered.connect(self.show_info_save_as)
        self.submenu_FUN_INFO.addAction(self.action_info_save_as)

        # Инструмент "Информация о функции "Печать..." ("Print..." function info)"
        self.action_info_print = QAction(QIcon('icons/print_icon.png'),
                                         '"Print..." function info', self)
        self.action_info_print.triggered.connect(self.show_info_print)
        self.submenu_FUN_INFO.addAction(self.action_info_print)

        # Инструмент "Информация о функции "Закрыть" ("Close" function info)"
        self.action_info_close = QAction(QIcon('icons/close_icon.jpg'),
                                         '"Close" function info', self)
        self.action_info_close.triggered.connect(self.show_info_close)
        self.submenu_FUN_INFO.addAction(self.action_info_close)

        # Обновление заголовка программы
        self.update_title()

        # Обновление шрифта
        self.update_font()

    # Функция "show_info_open_file", показывающая информацию о функции "Открыть... (Open...)"
    def show_info_open_file(self):
        info_box = QMessageBox(self)
        info_box.setIcon(QMessageBox.Question)
        info_box.setWindowTitle('Open...')
        info_box.setText('Opens file on PC')
        info_box.show()

    # Функция "show_info_open_file", показывающая информацию о функции "Сохранить (Save)"
    def show_info_save_file(self):
        info_box = QMessageBox(self)
        info_box.setIcon(QMessageBox.Question)
        info_box.setWindowTitle('Save file')
        info_box.setText('Saves text to opened in app file')
        info_box.show()

    # Функция "show_info_open_file",
    # показывающая информацию о функции "Сохранить как... (Save as...)"
    def show_info_save_as(self):
        info_box = QMessageBox(self)
        info_box.setIcon(QMessageBox.Question)
        info_box.setWindowTitle('Save as...')
        info_box.setText('Saves text to specified file')
        info_box.show()

    # Функция "show_info_print", показывающая информацию о функции "Печать... (Print...)"
    def show_info_print(self):
        info_box = QMessageBox(self)
        info_box.setIcon(QMessageBox.Question)
        info_box.setWindowTitle('Print...')
        info_box.setText('Prints text on paper')
        info_box.show()

    # Функция "show_info_close", показывающая информацию о функции "Закрыть (Close)"
    def show_info_close(self):
        info_box = QMessageBox(self)
        info_box.setIcon(QMessageBox.Question)
        info_box.setWindowTitle('Close')
        info_box.setText("Stops Simplopad's work and closes it")
        info_box.show()

    # Функция "show_info_about_app", показывающая информацию о программе
    def show_info_about_app(self):
        info_box = QMessageBox(self)
        info_box.setIcon(QMessageBox.Question)
        info_box.setWindowTitle('About Simplopad')
        info_box.setText(APP_INFO)
        info_box.show()

    # Функция "update_font", обновлящая шрифт в рабочей области
    def update_font(self):
        # Обновление шрифта в рабочей области
        self.text_editor.setFont(self.text_font)

    # Функция "choose_font", позволяющая изменить шрифт на любой другой
    def choose_font(self):
        # Получение шрифта, выбранного пользователем
        font, ok_pressed = QFontDialog.getFont()
        # Возможно, что пользователь нажал Cancel,
        # поэтому идёт проверка, нажал ли пользователь на OK
        if ok_pressed:
            self.text_font = font
            self.update_font()

    # Функция "update_title", обновляющая заголовок программы
    def update_title(self):
        # Если открытый в приложении в данный момент файл существует
        if self.path_to_file:
            self.setWindowTitle(f"{self.file_name} - {APP_NAME}")
        else:
            # Иначе файла не существует, следовательно,
            # надо дать файлу дефолтное имя - "Безымянный (Untitled)"
            self.setWindowTitle(f"Untitled - {APP_NAME}")

    # Функция "report_error", уведомляющая пользователя об ошибке
    def report_error(self, error_text):
        # Окно, уведомляющее об ошибке
        error_box = QMessageBox(self)
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle('Error')
        error_box.setText(error_text)
        error_box.show()

    # Функция "save_to_path", позволяющая сохранить файл,
    # который находится по пути path
    def save_to_path(self, path):
        # Возможно, что данный путь некорректный,
        # поэтому используется try-except
        try:
            # Открытие файла
            f = open(path, 'w')
            # Запись в файл текста из рабочей области
            f.write(self.text_editor.toPlainText())
            # Сохранение информации о файле:
            # 1) путь к файлу
            self.path_to_file = path
            # 2) имя файла
            self.file_name = basename(path)
            # Обновление заголовка, т.к. имя файла поменялось
            self.update_title()
            f.close()

        except Exception as error:
            # Сообщение пользователю об ошибке
            self.report_error(str(error))

    # Функция "create_file", позволяющая создать файл
    def create_file(self):
        if self.path_to_file:
            self.report_error('File already opened!')
            return
        # Создание файла, получение пути к нему
        temp_path, ok_pressed = QFileDialog.getSaveFileName(self, 'Create file', 'Untitled',
                                                            'Text documents (*.txt);;'
                                                            'All files (*.*)')
        # Если пользователь создал файл и выбрал OK
        if ok_pressed:
            # Сохранение текста в файл,
            # к которому был получен путь
            self.save_to_path(temp_path)

    # Функция "open_file", позволяющая открытить файл
    def open_file(self):
        # Получение пути к файлу
        temp_path, ok_pressed = QFileDialog.getOpenFileName(self, 'Open file', '',
                                                            'Text documents (*.txt);;'
                                                            'All files (*.*)')
        # Возможно, пользователь нажал Cancel, поэтому идёт проверка,
        # нажал ли пользователь на OK
        if ok_pressed:
            # Возможно, что будет открыт некорректный файл,
            # поэтому используется try-except
            try:
                # Открытие файла
                f = open(temp_path, 'r')
                # Получение содержимого
                txt = f.read()
                # Обновление рабочей области,
                # замена старого текста на текст, который находится в файле,
                # к которому получен путь
                self.text_editor.setText(txt)
                # Сохранение информации о файле:
                # 1) путь к файлу
                self.path_to_file = temp_path
                # 2) имя файла
                self.file_name = basename(temp_path)
                # Обновление заголовка, т.к. имя файла поменялось
                self.update_title()
                f.close()

            except Exception as error:
                # Сообщение пользователю об ошибке
                self.report_error(str(error))

    # Функция "file_save_as", позволяющая сохранить текст в файл
    def file_save_as(self):
        # Получение пути к файлу
        path, ok_pressed = QFileDialog.getSaveFileName(self, 'Save file', '',
                                                       'Text documents (*.txt);;All files(*.*)')
        # Если пользователь выбрал файл и нажал на OK
        if ok_pressed:
            # Сохранение текста в файл,
            # для которого был запрошен путь
            self.save_to_path(path)
        else:
            # Иначе, если путь к файлу не был указан, диалог был отменен,
            # т.е. была нажата кнопка Cancel, следовательно,
            # необходимо завершить работу функции
            return

    # Функция "save_file", позволяющая сохранить текущий файл
    def save_file(self):
        # Если в приложении открыт файл
        if self.path_to_file:
            # Сохраняем его в открытый в данный момент файл
            self.save_to_path(self.path_to_file)
        else:
            # Иначе нужно создать файл
            self.create_file()

    # функция "print_file", позволяющая распечатать файл через принтер
    def print_file(self):
        # Диалоговое окно выбора принтера и согласия печатания
        ask_printer = QPrintDialog()
        if ask_printer.exec():
            self.text_editor.print(ask_printer.printer())

    # Функция "keyPressEvent", обрабатывающая нажатия на клавиши
    def keyPressEvent(self, event):
        # Если было нажато сочетание клавиш "Ctrl + N"
        if int(event.modifiers()) == Qt.ControlModifier:
            if event.key() == Qt.Key_N:
                # Значит надо создать файл,
                # поэтому вызывается метод "create_file"
                self.create_file()
                return

        # Если было нажато сочетание клавиш "Ctrl + S"
        if int(event.modifiers()) == Qt.ControlModifier:
            if event.key() == Qt.Key_S:
                # Значит надо сохранить файл,
                # поэтому вызывается метод "save_file"
                self.save_file()
                return

        # Если было нажато сочетание клавиш "Ctrl + O"
        if int(event.modifiers()) == Qt.ControlModifier:
            if event.key() == Qt.Key_O:
                # Значит надо открыть файл,
                # поэтому вызывается метод "open_file"
                self.open_file()
                return

        # Если было нажато сочетание клавиш "Ctrl + P"
        if int(event.modifiers()) == Qt.ControlModifier:
            if event.key() == Qt.Key_P:
                # Значит надо распечатать файл,
                # поэтому вызывается метод "print_file"
                self.print_file()
                return

        # Если было нажато сочетание клавиш "Ctrl + Shift + S"
        if int(event.modifiers()) == (Qt.ControlModifier + Qt.ShiftModifier):
            if event.key() == Qt.Key_S:
                # Значит надо сохранить содержимое текста в каком-то файле,
                # поэтому вызывается метод "file_save_as"
                self.file_save_as()
                return

    # Функция "closeEvent", обрабатывающая завершение программы
    def closeEvent(self, event):
        # Вопрос у пользователя, на уверенность в завершении программы
        want_to_close = QMessageBox.question(self,
                                             APP_NAME,
                                             'Are you sure want to close Simplopad?',
                                             QMessageBox.Yes | QMessageBox.No)
        if want_to_close == QMessageBox.Yes:
            # Если пользователь согласен, значит надо закрыть файл
            # Если в программе открыт существующий файл
            if self.text_editor.toPlainText() or self.path_to_file:
                # Вопрос у пользователя, хочет ли он сохранить изменения,
                # сделанные в файле
                path_ask = self.path_to_file
                if path_ask == '':
                    # Возможно, пользователь не открывал файл в приложении
                    path_ask = 'Untitled'
                want_to_save = QMessageBox.question(self,
                                                    APP_NAME,
                                                    'Do you want to save changes in:\n'
                                                    f'"{path_ask}"?',
                                                    QMessageBox.Yes |
                                                    QMessageBox.No | QMessageBox.Cancel)
                # Возможно, пользователь перехотел закрывать программу,
                # поэтому необходимо обработать этот случай
                if want_to_save == QMessageBox.Cancel:
                    # Значит пользователь отменил выход из программы,
                    # следовательно, надо продолжить работу программы
                    event.ignore()
                    return
                if want_to_save == QMessageBox.Yes:
                    # Если пользователь отвечает "Да", необходимо сохранить изменения,
                    # поэтому вызывается метод save_file
                    self.save_file()
            # Завершение программы
            event.accept()
        else:
            # Продолжение работы программы
            event.ignore()


if __name__ == '__main__':
    # Создание класса приложения PyQT
    app = QApplication(sys.argv)
    # Создание и показ пользователю экземпляра MainWindow класса Notepad
    ex = Simplopad()
    ex.show()
    # Ожидание, пока пользователь не завершит исполнение app (QApplication),
    # и затем завершение программы
    sys.exit(app.exec())
