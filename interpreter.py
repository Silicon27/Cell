# interpreter.py

from re import Match
from tokenizer import ConvertToToken
from brace import matchbrace
from helper import scope
import json
import os

class Interpreter:
    def __init__(self, config_path):
        self.variables = {}
        self.functions = {}
        self.funcData = {}
        self.keywords = ["defn", "import", "int", "str", "bool", "float", "double", "char", "vcel", "root", "var"]
        self.tokens = ["DEFN", "IMPORT", "INT", "STR", "BOOL", "FLOAT", "DOUBLE", "CHAR", "VCEL", "ROOT", "VAR"]
        self.SYMBOL = ["=", "+", "-", "*", "/", "%", "(", ")", "{", "}", "[", "]",
                       ";", ":", ",", "==", "!=", "<", ">", "<=", ">=", "&&", "||",
                       "!", "&", "|", "...", "->", "=>", "++", "--", "+=", "-=",
                       "*=", "/=", "%=", "'", '"']
        self.config_path = config_path
        self.tokenized_output = []
        self.tokenized_dict = {}
        self.tokenized_output_w_spaces = []
        self.MatchedBrace = {}
        self.scope_list = []
        self.scope_list_w_space = []
        self.root_list = []

    def load_config(self):
        with open(os.path.abspath(self.config_path), "r") as file:
            config = json.load(file)
        return config["FileConfig"]["target"]

    def tokenize(self, target_file):
        tokenizer = ConvertToToken(self.keywords, target_file, self.tokens, self.SYMBOL)
        self.tokenized_output, self.tokenized_dict, self.tokenized_output_w_spaces = tokenizer.tokenize()

    def match_braces(self):
        self.MatchedBrace = matchbrace.match_braces(self.tokenized_output)

    def analyze_scope(self):
        self.scope_list, self.root_list, self.scope_list_w_space = scope.analyzer(self.tokenized_output, self.MatchedBrace, self.tokenized_output_w_spaces)

    def visualize_scope(self):
        scope.visualizer(self.scope_list)


    #________________________________ Handler functions ___________________________________#

    def _defn_handler(self, scope):
        pass

    #______________________________________________________________________________________#

    def run(self):
        target_file = self.load_config()
        self.tokenize(target_file)
        self.match_braces()
        self.analyze_scope()
        self.visualize_scope()
        # Add more steps to run the interpreter as needed

# Example usage
if __name__ == "__main__":
    interpreter = Interpreter("cellconfig/config.json")
    interpreter.run()
    # print(interpreter.tokenized_output_w_spaces)
    # print(interpreter.scope_list)
    # print(interpreter.scope_list_w_space)
    # print(interpreter.root_list)
    # print(interpreter.tokenized_output_w_spaces)