import requests
import json
from utils import make_instruction
from utils import make_cml
from utils import file_parser


#Creating verify task for each explanation

API_KEY = "xGxMendqyvbVgjEjXoH-"
request_url = "https://api.figure-eight.com/v1/jobs.json"
headers = {'content-type': 'application/json'}


file_data = file_parser_fid_fix("fixed_exp.txt")



while True:

	data = file_data.next()

	job_title= "Which Is The Best Explanation? "+str(data[0])

	print(job_title)
	exit()
	instructions=make_instruction(data[0][0])

	ratings = data[1]



	cml=make_cml(data[3],data[4],data[5],data[1],data[2])

	print(cml)

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
job_id = workJson['id']
print("\n\n\n\t\tEND")
print(job_id)