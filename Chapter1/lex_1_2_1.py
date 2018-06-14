import kukibanshee.symmtera as fsm

SYMBOL_TABLE = [
    None,
    "position",
    "initial",
    "rate"
]

OPERATORS = [
    "=",
    "+",
    "*"
]

NUMBERS = [
    60
]

WHITE_SPACES = [
    "\x20"
]

CODE = "position = initial + rate * 60"

def is_symbol_char(c):
    regex = re.compile("[a-z]")
    m = regex.search(c)
    if(m):
        return(True)
    else:
        return(False)

def is_number_char(c):
    regex = re.compile("[0-9]")
    m = regex.search(c)
    if(m):
        return(True)
    else:
        return(False)

def is_op_char(c):
    cond = (c in OPERATORS)
    if(cond):
        return(True)
    else:
        return(False)

def is_wsp_char(c):
    cond = (c in WHITE_SPACES)
    if(cond):
        return(True)
    else:
        return(False)
    
#######
INPUT = ""
SYMBOL_BUF = ""
OP_BUF = ""
NUMBER_BUF = ""
WSP_BUF = ""
#######


def append_buf(input,buf):
    buf = buf + input
    return(buf)

def clear_buf(buf):
    buf = ""
    return(buf)


def append_symbol_buf(input):
    return(append_buf(input,SYMBOL_BUF))

def append_number_buf(input):
    return(append_buf(input,NUMBER_BUF))

def append_op_buf(input):
    return(append_buf(input,OP_BUF))

###############
STACK = []
###############

def close_symbol_buf():
    symbol = SYMBOL_BUF
    index = SYMBOL_TABLE.index(symbol)
    ele = ("id",index)
    STACK.append(ele)
    clear_buf(SYMBOL_BUF)







machine = fsm.FSM()
machine.add("INIT",is_symbol_char,append_symbol_buf,"SYMBOL")
machine.add("INIT",is_number_char,append_number_buf,"NUMBER")
machine.add("INIT",is_op_char,append_op_buf,"OP")
machine.add("INIT",is_wps_char,None,"INIT")
machine.add("SYMBOL",is_symbol_char,append_symbol_buf,"SYMBOL")
machine.add("SYMBOL",is_number_char,close_symbol_buf,"NUMBER")
machine.add("SYMBOL",is_op_char,close_symbol_buf,"OP")
machine.add("SYMBOL",is_wps_char,close_symbol_buf,"INIT")




