import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleLanguageSelection(self, e):
        self._view.txtOut.controls.append(
            ft.Text(value="Language correctly selected: " + self._view.ddLanguage.value)
        )
        self._view.update()

    def handleSelectSearchMode(self, e):
        self._view.txtOut.controls.append(
            ft.Text(value="Search mode correctly selected: " + self._view.ddSelectModality.value)
        )
        self._view.update()

    def handleSpellCheck(self, e):
        # 1. Lettura dei valori dalla View
        txtCurrentSentence = self._view.txtInput.value
        language = self._view.ddLanguage.value
        modality = self._view.ddSelectModality.value
        # 2. Validazione degli input
        if txtCurrentSentence == "" or txtCurrentSentence is None:
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Add a sentence!"))
            self._view.update()
            return
        if language == "" or language == "Choose Language" or language is None:
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Select language!"))
            self._view.update()
            return
        if modality == "" or modality is None:
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Select modality!"))
            self._view.update()
            return
        # 3. Chiamata al Model (tramite handleSentence)
        parole, elapsedTime = self.handleSentence(txtCurrentSentence, language, modality)
        # 4. Aggiornamento dell'interfaccia con i risultati
        self._view.txtOut.controls.clear()
        self._view.txtOut.controls.append(ft.Text("Frase inserita: " + txtCurrentSentence))
        self._view.txtOut.controls.append(ft.Text("Parole errate: " + parole))
        self._view.txtOut.controls.append(
            ft.Text(value="Tempo richiesto dalla ricerca: " + str(elapsedTime) + " secondi"))
        # Opzionale (richiesto dalla traccia): svuotare il campo testo della frase
        self._view.txtInput.value = ""
        self._view.update()

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text