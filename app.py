from flask import Flask, render_template, request

app = Flask(__name__)

departure_city = ""
city = ""
start_date = ""
end_date = ""
activities = ""
budget = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        departure_city = request.form['departure_city']
        city = request.form['city']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        activities = request.form['activities']
        budget = request.form['budget']

        print(type(departure_city))
        print(type(start_date))
        print(type(city))
        print(type(end_date))
        print(type(activities))
        print(type(budget))

        # Dummy data for demo purposes (replace with actual API calls or data)
        flight_details = f"Flight from {departure_city} to {city}, departing on {start_date} and returning on {end_date}."
        hotel_details = "5-star hotel with sea view."
        transportation_details = "Rent a car available for your trip."
        local_experience_details = "Guided city tour and local food experiences."
        visa_requirements = "Visa on arrival available for most nationalities."
        weather_details = "Sunny, 25°C (77°F) throughout your stay."
        currency_details = "1 USD = 10 local currency units."

        # Pass the data to result.html
        return render_template('result.html', 
                               flight_details=flight_details,
                               hotel_details=hotel_details,
                               transportation_details=transportation_details,
                               local_experience_details=local_experience_details,
                               visa_requirements=visa_requirements,
                               weather_details=weather_details,
                               currency_details=currency_details)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
