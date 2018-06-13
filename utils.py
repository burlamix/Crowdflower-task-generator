
def file_parser_verify(file_name):
	with open(file_name, 'rb') as f:

		for i in range (0,7):

			#print("----------------------"+str(i))
			#group type
			content = f.readline()
			group_type = content.split()

			#print(group_type[0])

			#ratings
			content = f.readline()
			content = content.split()
			content = content[0].split(":")
			ratings = content[1].split(",")
			#print(ratings)

			#sequence
			content = f.readline()
			sequence = content.split()
			sequence = sequence[0]
			#print(sequence)

			#none
			f.readline()

			#explanation 1
			exp1 = f.readline().splitlines()

			#print(exp1[0])

			#none
			f.readline()

			#explanation 2 
			exp2 = f.readline().splitlines()
			#print(exp2[0])

			#none
			f.readline()

			#explanation 3
			exp3 = f.readline().splitlines()
			#print(exp3[0])
			#print(exp3[0])
			#none
			f.readline()

			yield group_type,ratings,sequence,exp1[0],exp2[0],exp3[0]



def file_parser_fid_fix(file_name):
	with open(file_name, 'rb') as f:

		while True:

			#print("----------------------"+str(i))
			#group type
			content = f.readline()
			group_type = content.split()

			print(group_type)

			#ratings
			content = f.readline()
			
			if (content == ""): 
				exit()
			content = content.split()
			content = content[0].split(":")
			ratings = content[1].split(",")
			print(ratings)

			#sequence
			content = f.readline()
			sequence = content.split()
			sequence = sequence[0]
			print(sequence)

			#none
			f.readline()

			#explanation 1
			exp1 = f.readline().splitlines()

			f.readline()

			yield group_type,ratings,sequence,exp1[0]

def make_instruction_verify(group_type):
	instructions="<h1>Introduction</h1><p>We are doing a study on the best way to explain the choices given by \
	our group recommendation system to users.</p><p>Imagine you are planning a trip with your "+group_type+". You decide \
	to use a recommender system to select the order of 10 places/Points of Interest(POI) you want to visit in a city. You\
	 will be provided with your list of preferences and the sequence of places that the system has recommended you to visit. \
	 Each preference has been given a rating from 1 to 10, 1 being the least liked and 10 being the most liked.</p><hr><h1>Steps</h1><ol>\
	 	<li>Have a look at your likes and dislikes in the given preferences list.</li>	<li>Have a look at the sequence our system has \
	 	recommended your "+group_type+" to visit.</li>	<li>Read the explanation given for the sequence generated.</li>	<li>Select the option \
	 	that you like the most.</li></ol><hr><h1>Rules &amp; Tips</h1><ul>	<li>Point of Interest is also referred to by the short\
	 	 form, POI.</li>	<li>To write the comment in the box is not mandatory.</li></ul><p>	<br></p><hr><h1>Example</h1><p>Answer\
	 	  in the text box:</p><p>Out of these three sentence I choose the first one because it is more clear.</p><hr>"

	return instructions


def make_instruction_fid_fix(group_type):
	instructions="<h1>Introduction</h1><p>We are doing a study on the best way to explain the choices given by our group recommendation \
	system to users and whether the explanations provided by our system can be improved.&nbsp;</p><p>Imagine you are planning a trip with\
	 your "+group_type+". You decide to use a recommender system to select the order of 10 places/Points of Interest(POI) you want to visit in a \
	 city. You will be provided with your list of preferences and the sequence of places that the system has recommended you to visit. Each\
	  preference has been given a rating from 1 to 10, 1 being the least liked and 10 being the most liked.</p><hr><h1>Steps</h1><ol><li>\
	  Have a look at your likes and dislikes in the given preferences list.</li><li>Have a look at the sequence our system has recommended\
	   your "+group_type+" to visit.</li><li>Read the explanation given for the sequence generated.</li><li>In the following questions, choose whether\
	    you like or dislike the sentence.</li><li>If you dislike it, select the \"I do not like it\" option (text-box will appear below) and \
	    rewrite the sentence in your desired way, or delete it altogether by simply writing a dash(-).</li><li>If you like it, select the \
	    \"I like it\" option and move on to the next question.</li></ol><hr><h1>Rules &amp; Tips</h1><p>Point of Interest is also referred to\
	     by the short form, POI.</p><p>What to look for in a sentence:</p><ul><li>Style, is the sentence well written? Or could the English\
	      be improved?</li><li>Specificity, is the sentence specific enough? Or is it missing important details?</li><li>Any other improvements\
	       that come to mind</li><li>If you would like to completely change a particular sentence, feel free to do so!</li></ul><hr><h1>\
	       Example</h1><p>Sentence: I am going to drink some coffee right now.</p><p>Suppose, for example, you do not like this sentence \
	       and would like to change it, then you could write:</p><p>Answer: I am going to drink a glass of milk now.</p><p>Another possible\
	        option, if you do not like the sentence at all, or believe it does not fit in the explanation, is:</p><p>Answer: -</p><hr>"
	return instructions







def make_cml_verify(exp1,exp2,exp3,ratings,sequence):

	exp1 = "\""+exp1+"\""
	exp2 = "\""+exp2+"\""
	exp3 = "\""+exp3+"\""




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
        <td style="width: 10.0000%;">"""+str(ratings[0])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[1])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[2])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[3])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[4])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[5])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[6])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[7])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[8])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[9])+"""</td>
      </tr>
    </tbody>
  </table>
  <p dir="ltr">
    <br />
  </p>
  <p dir="ltr">
    <span style="background-color: initial; text-align: initial;">SEQUENCE:</span>
  </p>
  <p dir="ltr">"""+sequence+"""</p>
</div>
<cml:radios label="Choose the explanation that you like more" validates="required" gold="true">
	<cml:radio label="""+str(exp1)+""" />
	<cml:radio label="""+str(exp2)+""" />
	<cml:radio label="""+str(exp3)+""" />
  </cml:radios>"""

	return cml

def make_cml_find_fix(exp,ratings,sequence):

	#exp1 = "\""+exp1+"\""
	arr_exp= exp.split(".")




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
        <td style="width: 10.0000%;">"""+str(ratings[0])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[1])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[2])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[3])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[4])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[5])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[6])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[7])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[8])+"""</td>
        <td style="width: 10.0000%;">"""+str(ratings[9])+"""</td>
      </tr>
    </tbody>
  </table>
  <p dir="ltr">
    <br />
  </p>
  <p dir="ltr">
    <span style="background-color: initial; text-align: initial;">SEQUENCE:</span>
  </p>
  <p dir="ltr">"""+sequence+"""</p>
  <p dir="ltr">Explanation:</p>
  <p>"""+str(exp)+"""</p>
</div>
<cml:radios label="Sentence 1: """+arr_exp[0]+"""" validates="required" gold="true">
  <cml:radio label="I do not like it" value="i_do_not_like_it" />
  <cml:radio label="I like it" value="i_like_it" />
</cml:radios>
<cml:text label="Change in the sentence 1 the part that you do not like  and rewrite it" validates="required" only-if="sentence_1_"""+arr_exp[0].replace(" ","_").replace(",","").lower()+""":[0]" gold="true" />
<cml:radios label="Sentence 2:"""+arr_exp[1]+"""" validates="required" gold="true">
  <cml:radio label="I do not like it" value="i_dont_like_it" />
  <cml:radio label="I like it" value="i_like_it" />
</cml:radios>
<cml:text label="Change in the sentence 2 the part that you do not like  and rewrite it" validates="required" only-if="sentence_2"""+arr_exp[1].replace(" ","_").replace(",","").lower()+""":[0]" gold="true" />
<cml:radios label="Sentence 3:"""+arr_exp[2]+"""" validates="required" gold="true">
  <cml:radio label="I do not like it" value="i_do_not_like_it" />
  <cml:radio label="I like it" value="i_like_it" />
</cml:radios>
<cml:text label="Change in the sentence 3 the part that you do not like  and rewrite it" validates="required" only-if="sentence_3"""+arr_exp[2].replace(" ","_").replace(",","").lower()+""":[0]" gold="true" />"""

	return cml

