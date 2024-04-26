import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime as dt
import os

from data import country_dict
from urls import Urls
from scraper import Scraper

FONT = "Arial"
BG = "lightgrey"
TABLEAU_PATH = 'OddsTableau.twbx'


def create_input(text, row, values, base_value):
    label = Label(text=text, font=FONT, bg=BG)
    label.grid(row=row, column=0, sticky=W, pady=10)

    box = ttk.Combobox(values=values,
                       width=10,
                       state="readonly",
                       font=FONT,
                       justify="center")
    box.set(base_value)
    box.grid(row=row, column=1, sticky=E)

    return box


def create_button(text, command, row):
    button = Button(text=text, command=command, font=FONT, width=40)
    button.grid(row=row, column=0, padx=30, pady=14, columnspan=2)


class GUI:
    def __init__(self):
        minimum_year = 2018
        year = dt.datetime.today().year
        start_of_season = list(range(minimum_year, year - 1))
        end_of_season = [year + 1 for year in start_of_season]
        countries = list(country_dict.keys())
        capitalized_countries = sorted(list(map(str.title, countries)), key=str.title)
        self.urls_list = None

        # Root
        root = Tk()
        root.title("Odds Scraper")
        root.resizable(False, False)
        root.config(padx=16, pady=30, background=BG)

        # Title
        welcome_label = Label(text="Welcome to the scraper\n"
                                   "interface ⛏️",
                              font=(FONT, 24, "bold"),
                              background=BG)
        welcome_label.grid(row=0, column=0, padx=30, pady=26, columnspan=2)

        # Inputs
        start_of_season_box = create_input(text="Start of Season:", row=1, values=start_of_season,
                                           base_value=min(start_of_season))
        end_of_season_box = create_input(text="End of Season:", row=2, values=end_of_season,
                                         base_value=max(end_of_season))
        country_box = create_input(text="Country:", row=3, values=capitalized_countries,
                                   base_value=min(capitalized_countries))

        # All Countries
        def all_countries_command():
            if is_all_countries.get():
                country_box.config(state="disabled")
            else:
                country_box.config(state="readonly")

        is_all_countries = tkinter.BooleanVar()
        all_countries = tkinter.Checkbutton(root,
                                            text="All countries",
                                            variable=is_all_countries,
                                            font=FONT,
                                            bg=BG,
                                            command=all_countries_command)
        all_countries.grid(row=4, column=1, sticky=E)

        # Submit
        def submit_command():
            submitted_start_of_season = int(start_of_season_box.get())
            submitted_end_of_season = int(end_of_season_box.get())
            submitted_country = countries if is_all_countries.get() else country_box.get().lower()

            if submitted_start_of_season >= submitted_end_of_season:
                messagebox.showerror("Date Error", "The provided input is not valid")
                return

            self.urls_list = Urls(start_of_season=submitted_start_of_season,
                                  end_of_season=submitted_end_of_season,
                                  country=submitted_country).get_urls_list()

        create_button(text="Submit", command=submit_command, row=5)

        def open_tableau():
            os.startfile(TABLEAU_PATH)

        create_button(text="Open Dashboard", command=open_tableau, row=6)

        def start_button_command():
            if not self.urls_list:
                print("Please add seasons!")
                return
            Scraper(self.urls_list)

        create_button(text="Start", command=start_button_command, row=7)

        root.mainloop()
