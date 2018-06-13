import requests
import json
from utils import make_instruction_fid_fix
from utils import make_cml_find_fix
from utils import file_parser_fid_fix


#Creating data for the playload

API_KEY = "xGxMendqyvbVgjEjXoH-"
request_url = "https://api.figure-eight.com/v1/jobs.json"
headers = {'content-type': 'application/json'}


#file with automatic explanation
file_data = file_parser_fid_fix("2018-06-13T12_01_50+00_00-Friends Trip.txt")


#loop until and of file is reach
while True:

	data = file_data.next()

	job_title= "Group Recommendation Survey "+str(data[0][0])+" "+str(data[0][1])#+" "+str(data[0][2])

	print(job_title)

	#make personalized istruction
	instructions=make_instruction_fid_fix(data[0][0])

	ratings = data[1]


	cml=make_cml_find_fix(data[3],data[1],data[2])


	payload = {
	'key': API_KEY,
	'job':{
	'title': job_title,
	'instructions': instructions,
	'cml': cml}}

	response=requests.post(request_url, data=json.dumps(payload), headers=headers)
	print(response.content)

	exit()

	#find job id and save it
	workJson = json.loads(response.content)
	job_id = workJson['id'+str(job_id)]
	print(job_id)
print("\n\n\n\t\tEND")
