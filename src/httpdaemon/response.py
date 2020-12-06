def htmlresponse(responsebody):
    """
    Returns a binary string representation an HTTP response that can be sent on a socket.
    """

    header = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\n\n"
    body = responsebody.encode("utf-8")

    return header + body

def filenotfound(message):
    """
    HTML response for file not found error
    """

    htmlbody = f"""
    <html>
    <head>
    <title>File not found</title>
    </head>
    <body>
    <h1>File not found</h1>
    <p>The resource that you are trying to access can't be located.</p>
    <p>Please check your path and try again.</p>
    <p>{message}<p>
    </body>
    """

    return htmlresponse(htmlbody)