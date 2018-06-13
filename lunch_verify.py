import requests
import json
from utils import make_instruction_verify
from utils import make_cml_verify
from utils import file_parser_verify

api_key="xGxMendqyvbVgjEjXoH-"
ì

#Creating data for the playload

API_KEY = "xGxMendqyvbVgjEjXoH-"
request_url = "https://api.figure-eight.com/v1/jobs.json"
headers = {'content-type': 'application/json'}


#file with find and fixed explanation
file_data = file_parser("fixed_exp.txt")


#loop until and of file is reach
while True:
	data = file_data.next()

	job_title= "Which Is The Best Explanation? "+str(data[0][0])+" "+str(data[0][1])+" "+str(data[0][2])

	print(job_title)

	#make personalized istruction
	instructions=make_instruction(data[0][0])

	ratings = data[1]


	cml=make_cml(data[3],data[4],data[5],data[1],data[2])


	payload = {
	'key': API_KEY,
	'job':{
	'title': job_title,
	'instructions': instructions,
	'cml': cml}}

	response=requests.post(request_url, data=json.dumps(payload), headers=headers)
	print(response.content)

	#find job id and save it
	workJson = json.loads(response.content)
	job_id = workJson['id'+str(job_id)]
	print(job_id)	

print("\n\n\n\t\tEND")
