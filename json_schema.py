import sys
import re
import json
import ast
from pprint import pprint
global strAvro,arrTab,countTab,fieldTab,dictinArr,missingKeys
strAvro = ""
countTab = 1
fieldTab = 1
dictinArr = 0
def createArraySchema(array_val):
	arr_type = type(array_val)
	if arr_type is dict:
		return createSchema(array_val)
	elif arr_type is int or arr_type is long or arr_type is float:
		return "int"
	elif arr_type is bool:
		return "boolean"
	elif arr_type is str or arr_type is unicode:
		return "string"

def createSchema(doc):
	## create object schema
	schema = {}

	## loop through keys
	for key in doc:
		## get key type
		key_type = type(doc[key])
		#print(key_type)

		## change key from unicode to string
		key = str(key)

		## Check which type this is
		if key_type is int:
			schema[key] = "int"
			
		elif key_type is long:
			schema[key] = "long"
			
		elif key_type is float:
			schema[key] = "float"
			
		elif key_type is bool:
			schema[key] = "boolean"
		elif key_type is str or key_type is unicode:
			schema[key] = "string"
		elif key_type is list:
			## create array and add to current schema
			schema[key] = [createArraySchema(doc[key][0])]
		elif key_type is dict:
			## create object and add to current schema
			schema[key] = createSchema(doc[key])
		else:
			print("unknown type:"), key_type
	
	## return fnished schema
	return schema
	

def array(abc):
	global strAvro,arrTab,countTab,dictinArr
	tamp = 0
	for x in abc:
		if(type(x) == dict): 
			for key , val in x.items() :
				if isinstance(val,dict):
					
					temp = "{'"+key+"':"+str(val)+"}"
					temp = ast.literal_eval(temp)
					
					if(dictinArr == 1):
						arrTabNumber = countTab + 1
					else:
						arrTabNumber = 1
					strAvro = flatten_new(temp,arrTabNumber)
					strAvro = strAvro[:-1]+'\n\t]\n\t}\t},'
					
				elif isinstance (val,list):
					val = ''.join(val)
					strAvro = strAvro+'\n'+arrTab+'\t'+'{'+'\n'+arrTab+'\t'+'"name":"'+key+'",\n'+arrTab+'\t'+'"type":"'+val+'"\n'+arrTab+'\t'+'},'

				else:

					strAvro = strAvro+'\n'+arrTab+'\t'+'{'+'\n'+arrTab+'\t'+'"name":"'+key+'",\n'+arrTab+'\t'+'"type":"'+val+'"\n'+arrTab+'\t'+'},'

		elif(type(x)== list):
			array(x)
	return strAvro
	
def flatten_new(d,tabNumber):
	
	global strAvro,arrTab,countTab,fieldTab,dictinArr

	for key in d:
		
		tab = '\t'
		generalTab = tab * tabNumber
		strAvro	= strAvro+'\n'+generalTab+'{'+'\n'+generalTab+'"name" :"'+key+'",'+'\n'+generalTab+'"type":{'+'\n'+generalTab+'   '+'"name":"'+key+'details",'+'\n'+generalTab+'   '+'"type":"record",'+'\n'+generalTab+'   '+'"fields":['
		countTab = countTab + 1
		fieldTab = fieldTab + 1
	for val in d.values():
		val = d[key]

		if isinstance(val, dict):
			for inner_key, inner_val in val.items():
				if isinstance(inner_val, list):
					
					listab = tab*countTab
					countTab = countTab +1
					arrTab = tab*countTab
					strAvro = strAvro+'\n'+listab+'{'+'\n'+arrTab+'"name":"'+inner_key+'",\n'+arrTab+'"type":{\n'+arrTab+'  '+'"type":"array",'+'\n'+arrTab+'  '+'"items":{'+'\n'+arrTab+'    '+'"name":"'+inner_key+'details",\n'+arrTab+'    '+'"type":"record",'+'\n'+arrTab+'    '+'"fields":['
					dictinArr = 1
					strAvro = array(inner_val)

					strAvro = strAvro[:-1]+'\n\t]\n\t}\t}\t},'
					
				elif isinstance(inner_val,dict):
					if(dictinArr == 1):
						temp = "{'"+inner_key+"':"+str(inner_val)+"}"
						temp = ast.literal_eval(temp)
						#print temp
						dictnumber = tabNumber + 1
						strAvro = flatten_new(temp,dictnumber)
						strAvro = strAvro[:-1]+'\n\t]\n\t}\t},' 
					else:
						temp = "{'"+inner_key+"':"+str(inner_val)+"}"
						temp = ast.literal_eval(temp)

						dictnumber = tabNumber
						strAvro = flatten_new(temp,dictnumber)

						strAvro = strAvro[:-1]+'\n\t]\n\t}\t},'
				
				else:
					if(dictinArr == 1) :
						if(inner_key in missingKeys):
							dictTab = generalTab + '\t'
							strAvro = strAvro + ('\n'+dictTab+'{'+'\n'+dictTab+'"name" : "' +inner_key+'",\n'+dictTab+'"type" : ["'+inner_val+'","null"]\n'+dictTab+'},')
						else:
							dictTab = generalTab + '\t'
							strAvro = strAvro + ('\n'+dictTab+'{'+'\n'+dictTab+'"name" : "' +inner_key+'",\n'+dictTab+'"type" : "'+inner_val+'"\n'+dictTab+'},')
					else:
						if(inner_key in missingKeys):
							valtab = tab*fieldTab
							strAvro = strAvro + ('\n'+tab+'{'+'\n'+valtab+'"name" : "' +inner_key+'",\n'+valtab+'"type" : ["'+inner_val+'","null"]\n'+tab+'},')
						else:
							valtab = tab*fieldTab
							strAvro = strAvro + ('\n'+tab+'{'+'\n'+valtab+'"name" : "' +inner_key+'",\n'+valtab+'"type" : "'+inner_val+'"\n'+tab+'},')

	return strAvro
			
		

def getSchema(file_name):
	'''
	Open file and pass the json document to createSchema
	'''
	global missingKeys
	missingKeys = []
	file = open(file_name,'r')
	data = file.read()
	file.close()
	temp = data.strip()
	data = data.strip()
	data = data.split('\n')
	dicttem = {}

	if (len(data)>1):
		for x in data:
			try:
				test = json.loads(x)
				dicttem.update(test)
			except:
				continue
		for x in data:
                        try :
                                test = json.loads(x)
                                tempKeys = set(dicttem.keys()) - set(test.keys())
                                tempKeys = list(tempKeys)
                                if tempKeys:
                                        missingKeys.append(tempKeys)
                        except:
                                continue
		missingKeys = list(set(missingKeys[0]))
		doc = str(dicttem)
		doc = re.sub(r"\dL","",doc)
		doc = doc.replace("u'",'"')
		doc = doc.replace("'",'"')
		doc = doc.replace(" ","")
		doc = doc.replace(":FALSE,",':"FALSE",')
		doc = doc.replace(":False,",':"False",')
		doc = doc.replace(":TRUE,",':"TRUE",')
		doc = doc.replace(":True,",':"True",')
	else :
		doc = str(temp)
	doc = json.loads(doc)
	return createSchema(doc)

def generateAvroSchema(file_name):
	global strAvro,countTab,fieldTab
	avro =  json.dumps(getSchema(file_name))
	avro = avro.replace("@", "")
	avro = avro.replace("-", "")
	avro = avro.replace(".", "")
	avro = ast.literal_eval(avro)
	global finalAvro
	finalAvro = ""
	for key,val in avro.items():
		if isinstance(val, dict):
			dicttemp = "{'"+key+"':"+str(val)+"}"
			dicttemp = ast.literal_eval(dicttemp)
			
			strAvro = ""
			countTab = 1
			fieldTab = 1
			intAvro = flatten_new(dicttemp , 1)
			finalAvro = finalAvro + intAvro[:-1]+'\n\t]\n}\t},'
			
		elif isinstance(val,list):
			finalAvro = finalAvro+'\n'+'\t'+'{'+'\n'+'\t\t'+'"name":"'+key+'",\n'+'\t\t'+'"type":{\n'+'\t\t'+'  '+'"type":"array",'+'\n'+'\t\t'+'  '+'"items":{'+'\n'+'\t\t'+'    '+'"name":"'+key+'details",\n'+'\t\t'+'    '+'"type":"record",'+'\n'+'\t\t'+'    '+'"fields":['
			strAvro = ""
			countTab = 1
			fieldTab = 1
			arrAvro = array(val)
			finalAvro = finalAvro + arrAvro[:-1]+'\n\t]\n\t}\t}\t},'
		else:
			if key in missingKeys:
				finalAvro = finalAvro+('\n\t'+'{'+'\n\t\t'+'"name" : "' +key+'",\n\t\t'+'"type" : ["'+val+'","null"]\n\t'+'},')
			else:
				finalAvro = finalAvro+('\n\t'+'{'+'\n\t\t'+'"name" : "' +key+'",\n\t\t'+'"type" : "'+val+'"\n\t'+'},')
	return finalAvro
	
