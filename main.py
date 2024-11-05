import sys

from PySide6.QtWidgets import QApplication

from widget.loginWnd import LoginWnd
from widget.mainWnd import MainWnd

if __name__ == "__main__":

    app = QApplication(sys.argv)
    login_window = LoginWnd()
    main_window = MainWnd()

    def on_first_window_closed():
        main_window.show()

    # We override the closeEvent to trigger the second window to be shown
    def first_window_close_event(event):
        on_first_window_closed()
        event.accept()  # Accept the close event to proceed

    login_window.closeEvent = first_window_close_event
    login_window.show()
    sys.exit(app.exec())
