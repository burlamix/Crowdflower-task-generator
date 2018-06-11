import requests
import json
api_key="xGxMendqyvbVgjEjXoH-"
#creating blank task

#Getting the response of the api call into a json file
response=requests.post("https://api.figure-eight.com/v1/jobs.json?key="+api_key)

#response status code
print(response.status_code)

#response object
print(response)

#response content, job details
print(response.content)

#Creating task with title, instructions and data

API_KEY = "xGxMendqyvbVgjEjXoH-"
job_title= "Captcha Api task with instruction "
instructions="<h1>Introduction</h1><p>We are doing a study on the best way to explain the choices given by our group recommendation system to users.</p><p>Imagine you are planning a trip with your family. You decide to use a recommender system to select the order of 10 places/Points of Interest(POI) you want to visit in a city. You will be provided with your list of preferences and the sequence of places that the system has recommended you to visit. Each preference has been given a rating from 1 to 10, 1 being the least liked and 10 being the most liked.</p><hr><h1>Steps</h1><ol>	<li>Have a look at your likes and dislikes in the given preferences list.</li>	<li>Have a look at the sequence our system has recommended your family to visit.</li>	<li>Read the explanation given for the sequence generated.</li>	<li>Select the option that you like the most.</li></ol><hr><h1>Rules &amp; Tips</h1><ul>	<li>Point of Interest is also referred to by the short form, POI.</li>	<li>To write the comment in the box is not mandatory.</li></ul><p>	<br></p><hr><h1>Example</h1><p>Answer in the text box:</p><p>Out of these three sentence I choose the first one because it is more clear.</p><hr>"

request_url = "https://api.figure-eight.com/v1/jobs.json"
headers = {'content-type': 'application/json'}

cml="""<div class="html-element-wrapper">
  <p dir="ltr">Your preferences:</p>
  <table style="width: 100%;">
    <tbody>
      <tr>
        <td style="width: 10.0000%;">POI1</td>
        <td style="width: 10.0000%;">POI2</td>
        <td style="width: 10.0000%;">POI3
          <br />
        </td>
        <td style="width: 10.0000%;">POI4
          <br />
        </td>
        <td style="width: 10.0000%;">POI5
          <br />
        </td>
        <td style="width: 10.0000%;">POI6
          <br />
        </td>
        <td style="width: 10.0000%;">POI7
          <br />
        </td>
        <td style="width: 10.0000%;">POI8
          <br />
        </td>
        <td style="width: 10.0000%;">POI9
          <br />
        </td>
        <td style="width: 10.0000%;">POI10
          <br />
        </td>
      </tr>
      <tr>
        <td style="width: 10.0000%;">1</td>
        <td style="width: 10.0000%;">9</td>
        <td style="width: 10.0000%;">8</td>
        <td style="width: 10.0000%;">9</td>
        <td style="width: 10.0000%;">7</td>
        <td style="width: 10.0000%;">9</td>
        <td style="width: 10.0000%;">6</td>
        <td style="width: 10.0000%;">9</td>
        <td style="width: 10.0000%;">3</td>
        <td style="width: 10.0000%;">8</td>
      </tr>
    </tbody>
  </table>
  <p dir="ltr">
    <br />
  </p>
  <p dir="ltr">
    <span style="background-color: initial; text-align: initial;">SEQUENCE:</span>
  </p>
  <p dir="ltr">POI1, POI6, POI4, POI7, POI5, POI8, POI3, POI9</p>
</div>
<cml:radios label="Choose the explanation that you like more" validates="required" gold="true">
  <cml:radio label="Hey John, we recommend you to visit POI1 first in your trip. We know that you do not really prefer visiting that place but your family rates this place highly. The POI you want to visit most is disliked by your mother and your sister. In fact, POI1 is the place where your father wants to visit the most." value="hey_john_we_recommend_you_to_visit_poi1_first_in_your_trip_we_know_that_you_do_not_really_prefer_visiting_that_place_but_your_family_rates_this_place_highly_the_poi_you_want_to_visit_most_is_disliked_by_your_mother_and_your_sister_in_fact_poi1_is_the_place_where_your_father_wants_to_visit_the_most" />
  <cml:radio label="Hey John, we recommend you to visit POI1 first in your trip. We know that you would prefer not to visit this place, but your family rates it highly. The POI you want to visit most is disliked by your mother and your sister.In fact, POI1 is the place your father wants to see the most." value="hey_john_we_recommend_you_to_visit_poi1_first_in_your_trip_we_know_that_you_would_prefer_not_to_visit_this_place_but_your_family_rates_it_highly_the_poi_you_want_to_visit_most_is_disliked_by_your_mother_and_your_sisterin_fact_poi1_is_the_place_your_father_wants_to_see_the_most" />
  <cml:radio label="Hey John, your mother, brother and father rated POI3 as 10/10! We know that this place is not your favourite but your family rates this place highly. Your mother and your sister didn&#x27;t like the place you want to visit. In fact, POI1 is the place where your father wants to visit the most." value="hey_john_your_mother_brother_and_father_rated_poi3_as_1010_we_know_that_this_place_is_not_your_favourite_but_your_family_rates_this_place_highly_your_mother_and_your_sister_didnt_like_the_place_you_want_to_visit_in_fact_poi1_is_the_place_where_your_father_wants_to_visit_the_most" />
</cml:radios>"""

payload = {
'key': API_KEY,
'job':{
'title': job_title,
'instructions': instructions,
'cml': cml
}
}

response=requests.post(request_url, data=json.dumps(payload), headers=headers)
print(response.content)


#find job id and save it
workJson = json.loads(response.content)
job_id = workJson['id']
print(job_id)