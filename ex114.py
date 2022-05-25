import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[031mO site pudim não está acessível.\033[m')
else:
    print('O site pudim foi acessado com sucesso!')
