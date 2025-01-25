from flask import Flask, render_template, request
from AIprompter2 import get_AI

app = Flask(__name__)

def convertCurrency(amount, from_currency, to_currency):
    prompt = (
        f"What is the conversion rate from {from_currency} to {to_currency}, "
        f"and how much is {amount} {from_currency} in {to_currency}?"
    )
    print(prompt)
    response = get_AI(prompt)
    return response

def getTraditionalFood(location):
    format = "For each food location place put it in a dictionary with key: name of place(string) value(int): average price but the response is in a string. no extra response at the top and bottom only the list, no hello at the start"
    prompt = f"What are some traditional dishes or cuisines in {location}? {format}"
    #print(prompt)
    response = get_AI(prompt)
    return response

def get_flight_info(start, stop, origin, destination):

    prompt = (
        f"Return the average flight costs to {destination} from {origin} if I am leaving on {start} "
        f"and want to return on {stop}. Have the cost be a at the end of the the response. This does not have to be real time Im looking for average for last 10 years"
    )

    response = get_AI(prompt)
    #print(response)

    return response


def get_transportation_price(destination):

    prompt = f"Give me a transportation plan for a vacation 2 sentences for {destination}"

    response = get_AI(prompt)
    #print(response)
    
    
    return response


def get_visa_requirement(destination):
    prompt = f"Is there a visa requirement for traveling to {destination}, respond either 'Yes' or 'No'"

    response = get_AI(prompt).split()
    #print(response)
    ret = response[-1].rstrip('.')

    return ret


def get_hotel_price(location):
    prompt = (
        f"Return the average price of a hotel in {location}, return it wih the price at the end"
    )

    response = get_AI(prompt)
    #print(response)

    return response

def getPopularTouristSpots(location):
    #format = "For each tourist place put it in a dictionary with key: location(string) value(int): average price but the response is in a string. no extra response at the top and bottom only the list, no hello at the start"
    prompt = f"What are the must-visit tourist spots in {location}?"
    #print(prompt)
    response = get_AI(prompt)
    return response

def getAverageWeatherPerLocation(location, month):

    prompt = f"What is the average weather in {location} during {month} ? Give the response"

    #print(prompt)

    response = get_AI(prompt)
    return response

def getAverageWeatherBrief(location, month):
    prompt = f"Give a one sentence response for the average weather in {location} during {month}"
    response = get_AI(prompt)
    return response





@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data directly from the request object
        departure_city = request.form.get('departure_city', '')
        city = request.form.get('city', '')
        start_date = request.form.get('start_date', '')
        end_date = request.form.get('end_date', '')
        activities = request.form.get('activities', '')
        budget = request.form.get('budget', '')

        flight_details = get_flight_info(start_date, end_date, departure_city, city)
        hotel_details = get_hotel_price(city)
        transportation_details = get_transportation_price(city)
        local_experience_details = getPopularTouristSpots(city)
        weather_experience_details = getAverageWeatherBrief(city, start_date)
        print(flight_details + "\n")
        print(hotel_details + "\n")
        print(transportation_details + "\n")
        print(local_experience_details + "\n")



        # Dummy data for demo purposes (replace with actual API calls or data)
        visa_requirements = "Visa on arrival available for most nationalities."
        currency_details = "1 USD = 10 local currency units."


        #Pass the data to result.html
        return render_template(
            'result.html',
            flight_details=flight_details,
            hotel_details=hotel_details,
            transportation_details=transportation_details,
            local_experience_details=local_experience_details,
            visa_requirements=visa_requirements,
            weather_details=weather_experience_details,
            currency_details=currency_details
        )

    # Render the index.html template for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
