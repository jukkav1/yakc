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
Builder.load_file("kv/yakc.kv")


class WeekDays(GridLayout):
    cols = 7
    rows = 1
    weekdays = ["Ma", "Ti", "Ke", "To", "Pe", "La", "Su"]
    color = (0, 0, 0, 1)

    def __init__(self, **kwargs):
        super(WeekDays, self).__init__(**kwargs)
        for _ in self.weekdays:
            self.add_widget(Label(text=_, color=self.color))


class MyCalendar:
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


class CalendarView(BoxLayout):
    pass


class MainWindow(BoxLayout):
    pass


class CalendarContainer(Screen):
    pass


class DayGrid(GridLayout):
    pass


class YAKC(App):
    def build(self, *args):
        self.calendar = MyCalendar()
        self.calendarview = CalendarView()
        self.daygrid = DayGrid()
        self.mw = MainWindow()
        return self.mw


if __name__ == "__main__":
    YAKC().run()
