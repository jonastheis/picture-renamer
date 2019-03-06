import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from renamer import Renamer


class MainWindowWidget(QWidget):
    def __init__(self):
        super(MainWindowWidget, self).__init__()

        self.setWindowTitle('Picture Renamer')
        self.drop_zone = DropZoneWidget(self)
        self.settings = SettingsWidget()

        # A Vertical layout to include the button layout and then the image
        layout = QVBoxLayout()
        layout.addWidget(self.drop_zone)
        layout.addWidget(QHLine())
        layout.addWidget(self.settings)

        self.setLayout(layout)
        self.setFixedSize(500, 500)
        self.show()
        self.setFocus()

    def start_renamer(self, folder_path):
        if folder_path:
            count = Renamer(folder_path, self.settings.get_time_shift()).start()
            self.drop_zone.set_successful_state(count)


class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)


class SettingsWidget(QWidget):
    def __init__(self):
        super(SettingsWidget, self).__init__()

        time_shift_layout, self.time_shift = self.init_time_shift()

        settings_label = QLabel('<font size=5>Settings</font>')

        layout = QVBoxLayout()
        layout.addWidget(settings_label)
        layout.addLayout(time_shift_layout)


        self.setLayout(layout)

        self.show()

    def init_time_shift(self):
        time_shift_layout = QHBoxLayout()

        description_label = QLabel('Time shift in hours:')
        time_shift_layout.addWidget(description_label)

        time_shift = QSpinBox()
        time_shift.setRange(-23, 23)
        time_shift.setValue(0)

        time_shift_layout.addWidget(time_shift)

        return time_shift_layout, time_shift

    def get_time_shift(self):
        shift = self.time_shift.value()
        return shift


class DropZoneWidget(QWidget):
    def __init__(self, main_widget):
        super(DropZoneWidget, self).__init__()
        self.main_widget = main_widget
        self.successful = False

        self.drop_label = QLabel('<font size=40>Drop parent folder</font>')
        self.drop_label.setAlignment(Qt.AlignCenter)
        self.or_label = QLabel('or')
        self.or_label.setAlignment(Qt.AlignCenter)
        self.select_button = QPushButton('Select parent folder')
        self.select_button.clicked.connect(self.select_button_click)

        # A Vertical layout to include the button layout and then the image
        self.info_layout = QVBoxLayout()
        self.info_layout.addStretch()
        self.info_layout.addWidget(self.drop_label)
        self.info_layout.addWidget(self.or_label)
        self.info_layout.addWidget(self.select_button)
        self.info_layout.addStretch()

        self.setLayout(self.info_layout)

        # Enable dragging and dropping onto the GUI
        self.setAcceptDrops(True)

        self.show()

    # The following three methods set up dragging and dropping for the app
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasUrls:
            e.setDropAction(Qt.CopyAction)
            e.accept()

            # only get 1 element from drop
            path = e.mimeData().urls()[0].path()
            self.set_folder(path)
        else:
            e.ignore()

    def select_button_click(self):
        if self.successful:
            self.set_inital_state()
        else:
            path = QFileDialog.getExistingDirectory(self, 'Select folder')
            self.set_folder(path)

    def set_folder(self, folder_name):
        self.main_widget.start_renamer(folder_name)

    def set_inital_state(self):
        self.successful = False
        self.drop_label.setText('<font size=40>Drop parent folder</font>')
        self.or_label.setText('or')
        self.select_button.setText('Select parent folder')

    def set_successful_state(self, count):
        self.successful = True
        self.drop_label.setText('<font size=40>Successfully renamed %s pictures</font>' % count)
        self.or_label.setText('')
        self.select_button.setText('Rename more pictures')


if __name__ == '__main__':
    app = QApplication([])

    main_widget = MainWindowWidget()
    sys.exit(app.exec_())
