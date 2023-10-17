from unittest import TestCase
from typing import List
from LPQ.lexer import Lexer

from LPQ.token import (
    Token,
    TokenType,
)

class LexerTest(TestCase):
    def test_illegal(self) -> None:
        source: str = "¡¿@" # illegal characters
        lexer: Lexer = Lexer(source)  

        tokens: List[Token] = []
        for i in range (len(source)):
            # print("aquí: " + str(i))
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, "¡"),
            Token(TokenType.ILLEGAL, "¿"),
            Token(TokenType.ILLEGAL, "@"),
        ]

        self.assertEquals(tokens, expected_tokens)
    
    def test_one_character_operator(self) -> None:
        source:str = "=+" # one character tokens
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ASSIGN, "="),
            Token(TokenType.PLUS, "+"),
        ]

        self.assertEquals(tokens, expected_tokens)

    def test_eof(self) -> None:
        source: str = "+"
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source) + 1):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.PLUS, "+"),
            Token(TokenType.EOF, ""),
        ]

        self.assertEquals(tokens, expected_tokens)
    
    def test_delimeters(self) -> None:
        source: str = "(){},;"
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []

        for i in range (len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LPAREN, "("),
            Token(TokenType.RPAREN, ")"),
            Token(TokenType.LBRACE, "{"),
            Token(TokenType.RBRACE, "}"),
            Token(TokenType.COMMA, ","),
            Token(TokenType.SEMICOLON, ";"),
        ]
        self.assertEquals(tokens, expected_tokens)
    
    def test_assigment(self) -> None:
        source: str = " nisqa cinco = 5;"
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []

        for i in range (len(source)):
            tokens.append(lexer.next_token())
            print(tokens[i])
        
        expected_tokens: List[Token] = [
            Token(TokenType.LET, "nisqa"),
            Token(TokenType.IDENT, "cinco"),
            Token(TokenType.ASSIGN, "="),
            Token(TokenType.INT, "5"),
            Token(TokenType.SEMICOLON, ";"),
        ]
        self.assertEquals(tokens, expected_tokens)
        self.assertEquals(len(tokens), expected_tokens.__len__())
