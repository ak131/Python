import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:9000')

print s.system.listMethods()
print(s.ping())