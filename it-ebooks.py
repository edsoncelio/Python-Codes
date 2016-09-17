# -*- coding: utf-8 -*- 
import demjson
import requests
import sys

def dados_livros(template):
	url = "http://it-ebooks-api.info/v1/search/"
	try:
		termo = sys.argv[1]
		_num_page = sys.argv[2]
		r = requests.get(url+termo+"/page/"+_num_page)
		data = (r.text)
		_result = demjson.decode(data) #converter pra json s2
	except IndexError:
		print "Usage :  python it-ebooks.py <titulo a ser buscado>"
		print "Usage :  python it-ebooks.py <titulo a ser pesquisado> <num da pagina>"
		exit(1)
	try:
		for i in range(0,len(_result['Books'])):
			print (template.format(titulo=_result['Books'][i]['Title'],
			descricao=_result['Books'][i]['Description'],subtitulo=_result['Books'][i]['SubTitle'],
			isbn=_result['Books'][i]['isbn'],
			resultados=_result['Total']))	
	except:
		print ("nenhum resultado!")
	

if __name__ == ("__main__"):
	template = ( '''		
   Título : {titulo}
   Subtitulo : {subtitulo}
   Descrição : {descricao}
   ISBN : {isbn}
   Total de Resultados : {resultados}
''')
dados_livros(template)
	
