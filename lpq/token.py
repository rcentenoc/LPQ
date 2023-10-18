# vamos a definir los tokens que vamos a usar en el lenguaje
from enum import (
    Enum,
    auto,
    unique
)
# vamos a usar NamedTuple para definir los tokens
from typing import (
    Dict,
    NamedTuple
)
# vamos a usar un diccionario para definir los tokens
@unique
class TokenType(Enum):
    AND = auto() # AND = And
    ASSIGN = auto() # ASSIGN = Assign
    BOOLEAN = auto() # BOOLEAN = Boolean
    BREAK = auto() # BREAK = Break
    COMMA = auto() # COMMA = Comma
    ELSE = auto() # ELSE = Else
    EOF = auto() # EOF = End Of File
    FALSE = auto() # FALSE = False
    FOR = auto() # FOR = For
    FUNCTION = auto() # FUNCTION = Function
    IDENT = auto() # IDENT = Identifier
    IF = auto()  # IF = If
    ILLEGAL = auto() # ILLEGAL = Illegal
    INPUT = auto() # INPUT = Input
    INT = auto() # INT = Integer
    LBRACE = auto() # LBRACE = Left Brace
    LET = auto() # LET = Let
    LPAREN = auto() # LPAREN = Left Parenthesis
    MAIN = auto() # MAIN = Main
    MINUS = auto() # MINUS = Minus
    NOT = auto() # NOT = Not
    NULL = auto() # NULL = Null
    OR = auto() # OR = Or
    OUTPUT = auto() # OUTPUT = Output
    PLUS = auto() # PLUS = Plus
    RBRACE = auto() # RBRACE = Right Brace
    RETURN = auto() # RETURN = Return
    RPAREN = auto() # RPAREN = Right Parenthesis
    SEMICOLON = auto() # SEMICOLON = Semicolon
    STRING = auto() # STRING = String
    TRUE = auto() # TRUE = True
    VOID = auto() # VOID = Void
    WHILE = auto() # WHILE = While


# vamos a usar una NamedTuple para definir los tokens
class Token(NamedTuple):
    token_type: TokenType
    literal: str
    # vamos a definir un dunder method para que se pueda imprimir el token 
    # esto es para controlar lo que va a regresar str en el caso de que se imprima un token
    def __str__(self) -> str:
        return f"Token({self.token_type}, {self.literal})"

# vamos a definir un diccionario para los keywords
# def lookup_ident(ident: str) -> TokenType:
#     keywords = {
#         'mana': TokenType.AND,
#         'yuyay': TokenType.BOOLEAN,
#         'tukuchay': TokenType.BREAK,
#         'mana_huk': TokenType.ELSE,
#         'mana_chiqa': TokenType.FALSE,
#         'haykaq': TokenType.FOR,
#         'suyupaq': TokenType.FUNCTION,
#         'huk': TokenType.IF,
#         'kikin': TokenType.INPUT,
#         'intiru': TokenType.INT,
#         'nisqa': TokenType.LET,
#         'main': TokenType.MAIN,
#         'mana': TokenType.NOT,
#         'hamuy': TokenType.RETURN,
#         'qillqa': TokenType.STRING,
#         'chiqa': TokenType.TRUE,
#         'mana': TokenType.VOID,
#         'kuti': TokenType.WHILE,
#     }
#     return keywords.get(ident, TokenType.IDENT)

def lookup_token_type(literal:str)-> TokenType:
    keywords : Dict[str, TokenType] = { 
        'mana': TokenType.AND,
        'yuyay': TokenType.BOOLEAN,
        'tukuchay': TokenType.BREAK,
        'mana_huk': TokenType.ELSE,
        'mana_chiqa': TokenType.FALSE,
        'haykaq': TokenType.FOR,
        'suyupaq': TokenType.FUNCTION,
        'huk': TokenType.IF,
        'kikin': TokenType.INPUT,
        'intiru': TokenType.INT,
        'nisqa': TokenType.LET,
        'main': TokenType.MAIN,
        'mana': TokenType.NOT,
        'hamuy': TokenType.RETURN,
        'qillqa': TokenType.STRING,
        'chiqa': TokenType.TRUE,
        'mana': TokenType.VOID,
        'kuti': TokenType.WHILE,
    }
    return keywords.get(literal, TokenType.IDENT)
