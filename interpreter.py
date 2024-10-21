from re import Match

from tokenizer import ConvertToToken
import json
from brace import matchbrace
import os
from helper import scope

# Although the tokens are just capitalized keywords, they are used to identify the type of token.
# If by chance there is a word that contains a keyword although not one,
# the capitalized keyword will be used to identify the "true" keyword
keywords = ["defn", "import", "int", "str", "bool", "float", "double", "char", "vcel"]
tokens = ["DEFN", "IMPORT", "INT", "STR", "BOOL", "FLOAT", "DOUBLE", "CHAR", "VCEL"]

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

MatchedBrace = matchbrace.match_braces(tokenized_output)

scope_list = scope.analyzer(MatchedBrace, tokenized_output)

print(MatchedBrace)
print(tokenized_output)




