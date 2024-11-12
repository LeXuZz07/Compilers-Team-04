import ply.yacc as yacc # We use the ply library
from analisador_lexico import tokens  # We use the tokens we created in the lexical analyzer we already made

# We create a symbol table
symbol_table = {}

# Parser start rule
start = 'statement'

# Production rules
def p_statement_assign(p):
    'statement : type ID EQUALS value'
    var_type = p[1]  # Type of variable it accepts (int, float, bool)
    var_name = p[2]  # Variable name
    var_value = p[4]  # Variable value
    
    # Check the type of the variable with the assigned value
    if validate_type(var_type, var_value):
        # If the type matches, add the variable to the symbol table and display a message that we were successful
        symbol_table[var_name] = var_type
        print("Parsing Success! SDT Verified!")
    else:
        # If there is a semantic error, we show this message Parsing success but SDT error
        print("Parsing Success! SDT error!")

# We define the `type` rule, which allows us to specify the type of the variable that is
def p_type(p):
    '''type : INT
            | FLOAT
            | BOOL'''
    p[0] = p[1]

# We define the `value` rule to handle integer values
def p_value_int(p):
    'value : NUMBER'
    # We assign a tuple to `p[0]` with type 'int' and the value of the number it has
    p[0] = ('int', p[1])

# We define the `value` rule to handle floating point values
def p_value_float(p):
    'value : SPOT'
    # We assign a tuple to `p[0]` with type 'float' and the value of the floating point literal
    p[0] = ('float', p[1])

# We define the `value` rule to handle boolean values
def p_value_bool(p):
    '''value : BOOL_TRUE
             | BOOL_FALSE'''
    # We assign a tuple to `p[0]` with type 'bool' and boolean value (`true` or `false`)
    p[0] = ('bool', p[1])

# Handling syntax errors in the string
def p_error(p):
    print("Parsing error! SDT error!")

# Helper function to validate variable type and value
def validate_type(var_type, value):
    val_type, val_value = value  # `value` is a tuple (val_type, val_value)
    if var_type == 'int' and val_type == 'int':
        # If type is `int`, value must be an integer
        return isinstance(val_value, int)
    elif var_type == 'float' and val_type == 'float':
        # If type is `float`, the value must be floating point
        return isinstance(val_value, float)
    elif var_type == 'bool' and val_type == 'bool':
        # If type is `bool`, the value must be `true` or `false`
        return val_value in ['true', 'false']
    return False

# We build the parser
parser = yacc.yacc()

# Load input file
with open("ejemplo.txt", "r") as file:
    input_string = file.read()  # Read the entire contents of the file

# We pass the example to the parser
result = parser.parse(input_string)
