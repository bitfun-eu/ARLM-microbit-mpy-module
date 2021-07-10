A2M = {
    'A':'.-', 'B':'-...',
	'C':'-.-.', 'D':'-..', 'E':'.',
	'F':'..-.', 'G':'--.', 'H':'....',
	'I':'..', 'J':'.---', 'K':'-.-',
	'L':'.-..', 'M':'--', 'N':'-.',
	'O':'---', 'P':'.--.', 'Q':'--.-',
	'R':'.-.', 'S':'...', 'T':'-',
	'U':'..-', 'V':'...-', 'W':'.--',
	'X':'-..-', 'Y':'-.--', 'Z':'--..',
	'1':'.----', '2':'..---', '3':'...--',
	'4':'....-', '5':'.....', '6':'-....',
	'7':'--...', '8':'---..', '9':'----.',
	'0':'-----', ',':'--..--', '.':'.-.-.-',
	'?':'..--..', '/':'-..-.', '-':'-....-',
	'(':'-.--.', ')':'-.--.-',
}

M2A = {}
for k,v in A2M.items():
    if v in M2A: raise Exception("not a one to one mapping")
    M2A[v] = k

def encode(s):
    assert isinstance(s, str), "input must be a string!"
    s = s.upper()
    r = ""
    for c in s:
        if c != " ":
            m = A2M[c]
            r = r + m + " "
        else:
            r = r + " "
    return r

def decode(s):
    assert isinstance(s, str), "input must be a string!"
    slist = s.split(" ")
    r = ""
    for m in slist:
        if m == "":
            r = r + " "
        else:
            r = r + M2A[m]
    return r
    
m = encode("ARLM")
print(decode(m))
