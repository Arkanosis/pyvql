# pyvql v0.1.0-dev
# (C) 2017 Jérémie Roquet <jroquet@arkanosis.net>
# Released under the ISC license
# https://github.com/Arkanosis/pyvql/

__version__ = '0.1.0-dev'

class ParseException(Exception):
    pass

class Parser:

    def __init__(self):
        self.__selects = []
        self.__froms = []
        self.__wheres = []
        self.__ins = []

    @staticmethod
    def __tokenize(query):
        return query.split()

    def __scanToken(self):
        token = self.__tokens[0]
        del self.__tokens[0]
        return token

    def __eatToken(self, token):
        if self.__tokens[0] == token:
            del self.__tokens[0]
            return True
        return False

    def __parseQuery(self):
        return self.__parseSelect() and self.__froms and self.__end()

    def __parseSelect(self):
        if self.__eatToken('SELECT'):
            while not self.__end() and not self.__parseFrom():
                self.__selects.append(self.__scanToken())
        return self.__selects

    def __parseFrom(self):
        if self.__eatToken('FROM'):
            while not self.__end() and not self.__parseWhere():
                self.__froms.append(self.__scanToken())
        return self.__froms

    def __parseWhere(self):
        if self.__eatToken('WHERE'):
            while not self.__end() and not self.__parseIn():
                self.__wheres.append(self.__scanToken())
        return self.__wheres

    def __parseIn(self):
        if self.__eatToken('IN'):
            while not self.__end():
                self.__ins.append(self.__scanToken())
        return self.__ins

    def __end(self):
        return not self.__tokens

    def parse(self, query):
        self.__tokens = Parser.__tokenize(query)
        return self.__parseQuery()

    @property
    def selects(self):
        return self.__selects

    @property
    def froms(self):
        return self.__froms

    @property
    def wheres(self):
        return self.__wheres

    @property
    def ins(self):
        return self.__ins

def parse(query):
    parser = Parser()
    if parser.parse(query):
        return parser.selects, parser.froms, parser.wheres, parser.ins
    else:
        raise ParseException()
