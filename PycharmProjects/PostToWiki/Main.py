
import ldap

class ldapStorage:
  def __init__(self,
               host = 'ldap://ns-carina.carina.griddynamics.net',
               dn   = '',
               pw   = '',
               base = 'dc=griddynamics,dc=net'):

    self.addr = host
    self.dn = dn
    self.pw = pw
    self.base = base

    self.l = ldap.initialize(self.addr)
    self.l.simple_bind_s(self.dn, self.pw)

  def search_user(self,login):
    sFilter = 'uid=%s' % login
    attr = ['uid']
    try:
      return self.l.search_s(self.base, ldap.SCOPE_SUBTREE, sFilter, attr)[0][0]
    except:
      pass

  def bind(self,uid,password):
    try:
      return self.l.simple_bind_s(uid, password)
    except ldap.INVALID_CREDENTIALS, e:
      pass
    except:
      pass

if __name__ == "__main__":

#  L = ldapStorage(base='dc=griddynamics,dc=net')
#  print L.search_user('akornev')

  def denis_search(host, attr, n):
      open=ldap.open(host)
      search= open.search(base='ou=people,ou=griddynamics,dc=griddynamics,dc=net', scope=ldap.SCOPE_SUBTREE,
                       attrlist=[attr])
      result = open.result(msgid=search)[1][n][1]['cn'][0]
      return result

  host = 'ns-carina.carina.griddynamics.net'
  attr = 'cn'
  n=1

  while True:
      try:
        L2search = denis_search(host,attr,n)
        print L2search
        n+=1
      except :
          break

