# Import the PLY library for syntax analysis
import ply.yacc as yacc

# Import the lexer tokens defined previously
from analisador_lexico import tokens

# Import cmath for handling complex numbers (e.g., square roots of negatives)
import cmath

# Symbol table to store variable names, types, and values
symbol_table = {}

# Operator precedence rules
precedence = (
    ('left', 'LESS', 'MORE'),  # Addition and subtraction
    ('left', 'MULTIPLICATION', 'DIVISION', 'MODULE'),  # Multiplication, division, modulus
    ('right', 'EXPONENTIAL'),  # Exponentiation
    ('right', 'UMINUS', 'UPLUS'),  # Unary operators (negative and positive signs)
)

# Define rules for handling multiple statements
def p_statements(p):
    '''statements : statements statement
                  | statement'''
    pass

# Rule for assigning typed variables
def p_statement_assign_typed(p):
    '''statement : type ID EQUALS expression'''
    var_type = p[1]
    var_name = p[2]
    var_value = evaluate_expression(p[4])  # Evaluate the expression's value
    if validate_type(var_type, var_value):  # Check type compatibility
        symbol_table[var_name] = (var_type, var_value)
    else:
        raise ValueError(f"Type mismatch: variable '{var_name}' of type '{var_type}' cannot hold value '{var_value}'.")

# Rule for assigning untyped variables
def p_statement_assign_untyped(p):
    '''statement : ID EQUALS expression'''
    var_name = p[1]
    var_value = evaluate_expression(p[3])  # Evaluate the expression's value
    symbol_table[var_name] = ("auto", var_value)  # Automatically assign type

# Rule for print statements
def p_statement_print(p):
    '''statement : PRINT LPAREN expression RPAREN'''
    result = evaluate_expression(p[3])  # Evaluate the expression's value
    print(f"Result: {result}")

# Rules for variable types (e.g., int and float)
def p_type(p):
    '''type : INT
            | FLOAT'''
    p[0] = p[1]

# Unary operators (positive and negative signs)
def p_expression_unary(p):
    '''expression : LESS expression %prec UMINUS
                  | MORE expression %prec UPLUS'''
    if p[1] == '-':
        p[0] = -p[2]
    else:
        p[0] = p[2]

# Arithmetic operations (binary operators)
def p_expression_arithmetic(p):
    '''expression : expression MORE expression
                  | expression LESS expression
                  | expression MULTIPLICATION expression
                  | expression DIVISION expression
                  | expression MODULE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            raise ZeroDivisionError("Division by zero is undefined.")
        p[0] = p[1] / p[3]
    elif p[2] == '%':
        p[0] = p[1] % p[3]

# Exponentiation (handles special cases like 0^0)
def p_expression_exponential(p):
    'expression : expression EXPONENTIAL expression'
    base = p[1]
    exp = p[3]
    if base == 0 and exp == 0:
        raise ValueError("The operation 0^0 is undefined (for certain cases, the result is 1).")
    elif base < 0 and exp == 0.5:  # Handle square roots of negatives
        p[0] = cmath.sqrt(base)
    else:
        p[0] = base ** exp

# Grouping with parentheses
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

# Numbers (int or float)
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

# Variables
def p_expression_variable(p):
    'expression : ID'
    var_name = p[1]
    if var_name in symbol_table:
        p[0] = symbol_table[var_name][1]  # Retrieve the variable's value
    else:
        raise NameError(f"Variable '{var_name}' is not defined.")

# Error handling for syntax issues
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at the end of the input.")

# Function to validate type compatibility
def validate_type(var_type, value):
    if var_type == 'int' and isinstance(value, int):
        return True
    if var_type == 'float' and isinstance(value, (int, float)):
        return True
    return False

# Function to evaluate expressions recursively
def evaluate_expression(expr):
    if isinstance(expr, tuple):
        op, left, right = expr
        left_val = evaluate_expression(left)
        right_val = evaluate_expression(right)
        if op == '+':
            return left_val + right_val
        elif op == '-':
            return left_val - right_val
        elif op == '*':
            return left_val * right_val
        elif op == '/':
            if right_val == 0:
                raise ZeroDivisionError("Division by zero is undefined.")
            return left_val / right_val
        elif op == '%':
            return left_val % right_val
        elif op == '^':
            return left_val ** right_val
    return expr

# Build the parser
parser = yacc.yacc()

# Main function for user interaction
def main():
    print("Enter your statements (use 'print(expr)' to display results). Type 'exit' to quit.")
    while True:
        try:
            input_data = input(">> ").strip()
            if input_data.lower() == "exit":
                break
            parser.parse(input_data)
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
