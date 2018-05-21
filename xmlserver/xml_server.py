from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler


# Restrict to a particular path.
# class RequestHandler(SimpleXMLRPCRequestHandler):
#     rpc_paths = ('/RPC2',)


def ping():
    return True


# server = SimpleXMLRPCServer(('localhost', 9000), requestHandler=RequestHandler, allow_none=True)
server = SimpleXMLRPCServer(('0.0.0.0', 9000))
server.register_introspection_functions()
server.register_function(pow)
server.register_function(ping)

if __name__ == '__main__':
    server.serve_forever()
