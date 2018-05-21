import xmlrpclib

host = "127.0.0.1"
s = xmlrpclib.ServerProxy('http://{}:9000'.format(host))

print s.system.listMethods()
print(s.ping())
print(s.cwd())