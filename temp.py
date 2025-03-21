def app(environ, respond):
    respond('200 OK', [('Content-type', 'text/html; charset=utf-8')])

    from urllib.parse import parse_qs
    query = parse_qs(environ.get('QUERY_STRING', ''))
    age = query.get('age', [None])[0]

    if age:
        yield f"Sinun ikäsi on: {age} vuotta!".encode('utf-8')
    else:
        html_form = """
        <form method="get">
            <label for="age">Anna ikäsi:</label>
            <input type="text" id="age" name="age">
            <input type="submit" value="Lähetä">
        </form>
        """
        yield html_form.encode('utf-8')

from wsgiref.simple_server import make_server

with make_server('', 8000, app) as server:
    print("Palvelin käynnissä portissa 8000...")
    server.serve_forever()
