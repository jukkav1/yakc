from calendar import *
from datetime import *
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button

Window.size = (360, 640)
Builder.load_file("kv/weekdays.kv")
Builder.load_file("kv/yakc.kv")


class DayGrid(GridLayout):
    pass


class WeekDays(GridLayout):
    pass


class MyCalendar:
    """generic Kalenteri object defs and some functions"""

    list_of_months = [
        "Tammi",
        "Helmi",
        "Maalis",
        "Huhti",
        "Touko",
        "Kesä",
        "Heinä",
        "Elo",
        "Syys",
        "Loka",
        "Marras",
        "Joulu",
    ]
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_date = datetime.now().strftime("%d.%m.%Y")
    cal_month = current_month
    cal_year = current_year

    def set_entry(day: int, month: int, year: int, text: str):
        """create one text entry by date on database (N/A)"""
        pass

    def get_single_entry(day: int, month: int, year: int) -> str:
        """get single entry by date from database (N/A)"""
        pass

    def get_multi_entry(month: int, year: int) -> list:
        """get a list of days with entries from database (N/A)"""
        pass


class CalendarView(BoxLayout):
    pass


class MainWindow(BoxLayout):
    """Main placehodler for the app"""

    pass


class CalendarContainer(Screen):
    """Container screen for calendar"""

    pass


class YAKC(App):
    """Yet Another Kivy Calander"""

    def build(self, *args):
        """Building methods"""

        # kalenteri Kalenteri = new Kalenteri :Kappa:
        self.calendar = MyCalendar()
        self.calendarview = CalendarView()
        self.daygrid = DayGrid()
        mw = MainWindow()
        return mw


if __name__ == "__main__":
    YAKC().run()
