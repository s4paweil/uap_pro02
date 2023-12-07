# uap_pro02

- requirements.txt enthält alle erforderlichen Abhängigkeiten. Die Pakete können per Konsolenbefehl (pip install -r requirements.txt) oder über PyCharm (fragt nach öffnen der Datei, ob Pakete installiert werden sollen) geladen werden
- Um das Programm auszuführen, starte main.py
  - über file_path kann Pfad zum Tripla-Programm angegeben werden, das ausgeführt werden soll
  - Methode tokens_to_string(file_path) gibt die durch den Lexer erkannten Tokens aus
  - ast_to_string(ast) gibt den vom Parser erzeugten AST als String aus
  - generate_parse_tree_dot_file(ast, file_path, extensive=False) erzeugt den Parse-Tree im Dot-Format. Über Parameter extensive=True/False kann Art des Baums entschieden werden (ausführlich oder kompakt)
