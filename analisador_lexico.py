# Import the PLY library for lexical analysis
import ply.lex as lex

# Reserved words for the language
reserved_words = {
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'do': 'DO',
    'break': 'BREAK',
    'int': 'INT',
    'float': 'FLOAT',
    'bool': 'BOOL',
    'null': 'NULL',
    'return': 'RETURN',
    'true': 'BOOL_TRUE',
    'false': 'BOOL_FALSE',
    'print': 'PRINT'  # Added reserved word for printing
}

# List of tokens, including reserved words
tokens = [
    'NUMBER', 'ID', 'LESS', 'LPAREN', 'RPAREN', 'EXPONENTIAL',
    'MORE', 'DIVISION', 'MULTIPLICATION', 'BRACKETS',
    'OPERATORS', 'MODULE', 'EQUALS',
    'SIMPLE_LITERAL', 'SPECIAL', 'LKEY', 'RKEY',
] + list(reserved_words.values())

# Token patterns using regular expressions
t_LKEY = r'\{'
t_RKEY = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MULTIPLICATION = r'\*'
t_BRACKETS = r'[\[\]]'
t_OPERATORS = r'==|!=|<=|>=|<|>'
t_MODULE = r'%'
t_EQUALS = r'='
t_LESS = r'-'
t_MORE = r'\+'
t_EXPONENTIAL = r'\^'
t_DIVISION = r'/'
t_SPECIAL = r'[@#$%&_¿?]'
t_ignore = " \t"  # Ignore spaces and tabs

# Define token for numbers (integers and decimals, supporting negatives)
def t_NUMBER(t):
    r'(-?\d+(\.\d+)?)'  # Matches integers and decimals
    if '.' in t.value:
        t.value = float(t.value)  # Convert to float if decimal
    else:
        t.value = int(t.value)  # Convert to int if not decimal
    return t

# Define token for string literals enclosed in single quotes
def t_SIMPLE_LITERAL(t):
    r"'([^'\\]|\\.)*'"
    return t

# Define token for identifiers (variable or function names)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_words.get(t.value, 'ID')  # Check if identifier is a reserved word
    return t

# Handle newlines to update the line number count
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Handle errors for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
