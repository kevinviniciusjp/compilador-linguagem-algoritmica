from io import TextIOWrapper
from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListenerVisitor(ErrorListener):
    def __init__(self, file: TextIOWrapper):
        super().__init__()
        self._file = file
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """ Erro semantico """

        self._file.write("Linha " + str(line) + ": " + msg + "\n")
