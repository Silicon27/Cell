from re import Match
from tokenizer import ConvertToToken
from brace import matchbrace
from helper import scope
from syntax import parsec, parsers
import json
import os


#____________________________ Important Variables ____________________________#
variables = {}
functions = {}
funcData = {}
#_____________________________________________________________________________#


# Although the tokens are just capitalized keywords, they are used to identify the type of token.
# If by chance there is a word that contains a keyword although not one,
# the capitalized keyword will be used to identify the "true" keyword
keywords = ["defn", "import", "int", "str", "bool", "float", "double", "char", "vcel", "root", "var"]
tokens = ["DEFN", "IMPORT", "INT", "STR", "BOOL", "FLOAT", "DOUBLE", "CHAR", "VCEL", "ROOT", "VAR"]

SYMBOL = ["=", "+", "-", "*", "/", "%", "(", ")", "{", "}", "[", "]",
          ";", ":", ",", "==", "!=", "<", ">", "<=", ">=", "&&", "||",
          "!", "&", "|", "...", "->", "=>", "++", "--", "+=", "-=",
          "*=", "/=", "%=",]

(tokenized_output,
 tokenized_dict,
 tokenized_output_w_spaces) = ConvertToToken(keywords,
                                             json.load(open(os.path.abspath("cellconfig/config.json"), "r"))["FileConfig"]["target"],
                                             tokens,
                                             SYMBOL).tokenize()
# print(tokenized_output)
MatchedBrace = matchbrace.match_braces(tokenized_output)

scope_list, root_list = scope.analyzer(tokenized_output, MatchedBrace)

# print(MatchedBrace)

_embedded_function_call_syntax = parsec.seq(parsers.str_parser, parsers.opening_square_bracket_parser, parsers.closing_square_bracket_parser)

#______________________________ Parsers ______________________________#

def argument_parser(text, pos):
    if pos < len(text):
        for i in text[pos:]:
            if i == ",":
                pass
            elif i == "{":
                _embedded_function_call_syntax(text, pos)
            elif i == "]":
                return text, pos
            else:
                pass

#______________________________ Parser Functions ______________________________#
_defn_syntax = parsec.seq(parsers.defn_parser, parsers.str_parser, parsers.opening_square_bracket_parser, parsers.)


