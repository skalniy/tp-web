html = """
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
    <p>привет, мир</p>
    <table>
        <thead><th>key</th><th>value</th></thead>
        %(GET)s
    </table>
    <form action="http://localhost:8081?page=4" method="">
        <input type="text" name="textfield" value="4" hidden>
        <input type="submit" name="button">
    </form>
</body>
</html>
"""

def app(environ, start_response):
    get = ''.join([ '<tr><td>'+k+'</td><td>'+v+'</td></tr>' for k,v in 
                    { y[0] : y[1] for y in [ x.split('=') for x in environ.get('QUERY_STRING').split('&') ] }.items()
                ]) if environ.get('QUERY_STRING') else ''
    status = '200 OK';
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [ bytes(html % { 'GET' : get }, 'utf-8') ]
