import openai
import os
import requests
import shutil

with open('openai_key.txt', 'r') as f:
    api_key = f.read().strip('\n')
    assert api_key.startswith('sk-'), "Please enter a valid OpenAI API key"


openai.api_key = api_key

def create_meals(ingredients, kcal, type_of_meal):
    prompt= f'''Create a healthy daily {type_of_meal} meal plan for breakfast, lunch, and dinner based on the following ingredients: {ingredients}.
     Explain each recipe.
     The total daily intake of kcal should be below {kcal}.
     Assign a suggestive an concise name for each meal.
     Your answer should end with all the suggested titles like that:
     'Titles: 
     - title_1
     - title_2
     - title-3
     '''

    system_promote = 'You are an Expert and talented cook.'
    messages = [
        {"role": 'system', "content": system_promote},
        {"role": 'user', "content": prompt},
    ]


    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=1,
        max_tokens=1024,
        n = 1

    )
    r= response['choices'][0].message.content
    return r

def create_and_save_image(title, extra=''):
    
    image_prompt = f'{title}, {extra}, high quility food photograph'
    response = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size='1024x1024'
    )
    
    image_url = response['data'][0]['url']
    print()
    print(image_url)
    
    
    image_resource = requests.get(image_url, stream=True)
    print(image_resource.status_code)
    
    image_filename = f'{title}.png'
    if image_resource.status_code == 200:
        with open(image_filename, 'wb') as f:
            shutil.copyfileobj(image_resource.raw, f)
            return image_filename
    else:
        print('error accessing the image !')
        return False




ingredients = ['chicken', 'rice', 'tomatoes', 'onions', 'olive oil', 'salt', 'pepper']
ingredients_string = ', '.join(ingredients)

output = create_meals(ingredients=ingredients_string, kcal=2000, type_of_meal='Syrian')
meals = output.split('Titles:')[1].split('\n')[1: ]
meals = [m.strip('- ') for m in meals]
print(meals)

for _ in range(3):
    image_filename = create_and_save_image(meals[_], "white background")
    print(image_filename)

    
    
    
    
    
    
    
    
    
    
    