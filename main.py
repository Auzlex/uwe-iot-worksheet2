import morse

def test_encode(): # perform 5 encodes
    assert morse.encode('us') == '..- ...', "Should be ..- ... "
    assert morse.encode('qwertyuiopasdfghjklzxcvbnm1234567890') == '--.- .-- . .-. - -.-- ..- .. --- .--. .- ... -.. ..-. --. .... .--- -.- .-.. --.. -..- -.-. ...- -... -. -- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----', "Should be --.- .-- . .-. - -.-- ..- .. --- .--. .- ... -.. ..-. --. .... .--- -.- .-.. --.. -..- -.-. ...- -... -. -- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
    assert morse.encode('dogecoin to the moon') == '-.. --- --. . -.-. --- .. -. / - --- / - .... . / -- --- --- -.', "Should be -.. --- --. . -.-. --- .. -. / - --- / - .... . / -- --- --- -."
    assert morse.encode('=') == '-...-', "Should be -...-"
    assert morse.encode('q') == '--.-', "Should be --.-"

def test_decode(): # perform 5 decodes
    assert morse.decode('..- ...') == 'us', "Should be us"
    assert morse.decode('--.- .-- . .-. - -.-- ..- .. --- .--. .- ... -.. ..-. --. .... .--- -.- .-.. --.. -..- -.-. ...- -... -. -- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----') == 'qwertyuiopasdfghjklzxcvbnm1234567890', "Should be qwertyuiopasdfghjklzxcvbnm1234567890"
    assert morse.decode('-.. --- --. . -.-. --- .. -. / - --- / - .... . / -- --- --- -.') == 'dogecoin to the moon', "Should be dogecoin to the moon"
    assert morse.decode('-...-') == '=', "Should be ="
    assert morse.decode('--.-') == 'q', "Should be q"

# test misc chars
def test_encode_misc_chars():
    assert morse.encode('.') == '.-.-.-', "Should be .-.-.-"
    assert morse.encode('(') == '-.--.', "Should be -.--."
    assert morse.encode(')') == '-.--.-', "Should be -.--.-"
    assert morse.encode('+') == '.-.-.', "Should be .-.-."
    assert morse.encode('?') == '..--.', "Should be ..--."
    assert morse.encode(',') == '--..--', "Should be --..--"
    assert morse.encode('-') == '-....-', "Should be -....-"
    assert morse.encode('"') == '.-..-.', "Should be .-..-."
    assert morse.encode(';') == '-.-.-.', "Should be -.-.-."
    assert morse.encode(':') == '---...', "Should be ---..."
    assert morse.encode('&') == '.-...', "Should be .-..."
    assert morse.encode('$') == '...-..-', "Should be ...-..-"
    assert morse.encode('!') == '-.-.--', "Should be -.-.--"
    assert morse.encode("'") == '.----.', "Should be .----."
    assert morse.encode('_') == '..--.-', "Should be ..--.-"
    assert morse.encode('¿') == '..-.- ', "Should be ..-.-"

def test_decode_misc_chars():
    assert morse.decode('.-.-.-') == '.'    ,   "Should be ."
    assert morse.decode('-.--.') == '('    ,   "Should be ("
    assert morse.decode('-.--.-') == ')'    ,   "Should be )"
    assert morse.decode('.-.-.') == '+'    ,   "Should be +"
    assert morse.decode('..--.') == '?'    ,   "Should be ?"
    assert morse.decode('--..--') == ','    ,   "Should be ,"
    assert morse.decode('-....-') == '-'    ,   "Should be -"
    assert morse.decode('.-..-.') == '"'    ,   "Should be \""
    assert morse.decode('-.-.-.') == ';'    ,   "Should be ;"
    assert morse.decode('---...') == ':'    ,   "Should be :"
    assert morse.decode('.-...') == '&'     ,   "Should be &"
    assert morse.decode('...-..-') == '$'   ,   "Should be $"
    assert morse.decode('-.-.--') == '!'    ,   "Should be !"
    assert morse.decode('.----.') == "'"    ,   "Should be '"
    assert morse.decode('..--.-') == '_'    ,   "Should be _"
    assert morse.decode('..-.-') == '¿'    ,   "Should be ¿"

if __name__ == "__main__":
    print("test start")
    print("test encodes")
    test_encode()
    print("encodes passed")
    print("\n")
    print("test decodes")
    test_decode()
    print("decodes passed")

    print("\n")
    print("testing encode misc charts")
    test_encode_misc_chars()
    print("encode misc charts passed!")

    print("testing decode misc charts")
    test_decode_misc_chars()
    print("decode misc charts passed!")

    print('Everything passed')