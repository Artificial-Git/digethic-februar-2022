from src.api import app

# Wenn dieses Skript direkt ausgeführt wird, ist der Name, der gesetzt wird 'main'. Wenn wir ein
# anderes Python-Skript ausführen, oder importieren, wie oben, dann wäre der Check
# if __name__ == '__main__' falsch, weil wir nicht api.py direkt ausführen, sondern wsgi.py.
if __name__ == '__main__':
    # Durch aktives Debugging wird sofort neugestartet, wenn wir eine Änderung machen
    app.run(debug=True)
    # app.run()
