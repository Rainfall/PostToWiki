# coding=utf-8>
from xmlrpclib import Server

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

  def list_name_group(host, group):
      open=ldap.open(host)
      result = []

      filter='cn=%s' % group

      search_name = open.search(base='ou=groups,dc=griddynamics,dc=net', scope=ldap.SCOPE_SUBTREE,
                      filterstr=filter, attrlist=['member'])

      result_name = open.result(msgid=search_name)[1][0][1]['member']

      for i in range(0,len(result_name),1):

           search_people = open.search(base=result_name[i], scope=ldap.SCOPE_BASE, attrlist=['uid', 'cn'])
           result_people = open.result(msgid=search_people)

           result.append({"ID": result_people[1][0][1]['uid'][0], "Name":result_people[1][0][1]['cn'][0]})

      return result

  wikiURL = 'https://payu-wiki.carina.griddynamics.net:8443/display/~'
  host = 'ns-carina.carina.griddynamics.net'
  group = 'microsoft-management'


  L2search = list_name_group(host, group)
  print L2search
  L2search_for_posting=''
  userLink = ''
  for i in L2search:
      userLink = wikiURL+i["ID"]
      L2search_for_posting += '* ['+i['Name']+'|'+userLink+']\n'
  print L2search_for_posting

  import SOAPpy
  from SOAPpy import Types

  url = 'https://payu-wiki.carina.griddynamics.net:8443/rpc/soap-axis/confluenceservice-v1?wsdl'
  soap = SOAPpy.WSDL.Proxy(url)
  user='student'
  passwd='Aeju1lu6'
  spaceKey = 'STD'
  auth = soap.login(user, passwd)
  
  space = soap.getSpace(auth, spaceKey)

  soap.storePage(auth, {"space":spaceKey, "title": group, "content": L2search_for_posting})

  logout = soap.logout(auth)
  print logout
