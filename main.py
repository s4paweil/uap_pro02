from triplalex import lexer
import triplayacc

# Test for Lexer
def test_lexer(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
        lexer.input(code)

        # Token ausgeben
        for token in lexer:
            print(token)

def test_parser(name):
    source = "\n".join(open(name).readlines())
    ast = triplayacc.parser.parse(source)  # ,debug=True)
    print("AST:")
    print(ast)
    triplayacc.export_parse_tree(source)

def program_to_string(path):
    try:
        # Datei öffnen und Inhalt zeilenweise lesen
        with open(path, 'r') as datei:
            zeilen = datei.readlines()

        # Zeilennummern hinzufügen und Inhalt mit Zeilennummern zusammenstellen
        ausgabe = ""
        for nummer, zeile in enumerate(zeilen, start=1):
            ausgabe += f"{nummer}:\t {zeile}"

        return ausgabe

    except FileNotFoundError:
        return f"Die Datei '{path}' wurde nicht gefunden."



if __name__ == '__main__':
    code = "triplaprograms/ggT_euclid_rec.tripla"
    print(program_to_string(code) + '\n')
    #test_lexer(code)
    test_parser(code)


