import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )
        # --- PUNTO 1: Dropdown Lingua (Riga 1) ---
        self.ddLanguage = ft.Dropdown(
            value="Choose Language",
            options=[
                ft.dropdown.Option("italian"),
                ft.dropdown.Option("english"),
                ft.dropdown.Option("spanish"),
            ],
            on_change=self.__controller.handleLanguageSelection,
            label="Select language",
        )
        # --- PUNTO 2: Modalità + Input Frase + Bottone (Riga 2) ---
        self.ddSelectModality = ft.Dropdown(
            value="",
            options=[
                ft.dropdown.Option("Default"),
                ft.dropdown.Option("Linear"),
                ft.dropdown.Option("Dichotomic"),
            ],
            on_change=self.__controller.handleSelectSearchMode,
            width=200,
            label="Search Modality",
        )
        self.txtInput = ft.TextField(label="Add your sentence here", width=420)

        self.btnSpellCheck = ft.ElevatedButton(
            text="Spell Check",
            on_click=self.__controller.handleSpellCheck
        )
        row2 = ft.Row(
            controls=[self.ddSelectModality, self.txtInput, self.btnSpellCheck],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        # --- PUNTO 3: Area di Output (Riga 3) ---
        self.txtOut = ft.ListView(expand=1, spacing=10)
        # --- PUNTO 4: Aggiungiamo le righe alla pagina ---
        self.page.add(self.ddLanguage, row2, self.txtOut)
        self.page.update()


    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
