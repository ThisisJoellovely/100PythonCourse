from flask import Flask, render_template
import requests 
import datetime



app = Flask(__name__)
 
#CONSTANTS
FIRST_NAME = 'Joel' 
LAST_NAME = 'Lovely'
CURRENT_YEAR = int(datetime.datetime.now().year)
LINKS = ['https://api.genderize.io?', 'https://api.agify.io?' ]



def getApiResponse(links, variable_name): 

    api_response = {}
    api_response['name'] = f"Hey {variable_name},"

    for link in links:
        connection = requests.get(link,{'name' : f'{variable_name}'})

        try: 
            response = connection.json()

            if 'gender' in response:
                api_response['genderify'] = f"I think you are a {response['gender']}"
            if 'age' in response:
                api_response['ageify'] = f"and maybe {response['age']} years old"             
        except requests.RequestException as e:
             print(f'There was an error with this api connection: {e}')
    
    return api_response



@app.route('/')
def homepage():
    return render_template('index.html', current_year=CURRENT_YEAR, first_name=FIRST_NAME, last_name=LAST_NAME)

@app.route('/<NAME>')
def apiroute(NAME):
    api_response = getApiResponse(links=LINKS, variable_name=NAME)
    return render_template('api_response.html',ageify=api_response['ageify'], genderify=api_response['genderify'], name=api_response['name'])
@app.route('/blog')
def get_blog():
    blog_url = 'https://www.npoint.io/docs/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)

