# WeatherClient.py
# World Weather Station - College Version
#
# Run WeatherServer.py first.
#
# Your job is to complete the three functions below.
# The program will connect to the server and retrieve the
# weather information for you.

import socket

SERVER_HOST = "127.0.0.1"  # Do not change this
SERVER_PORT = 26459


def connect_to_server():
    """Connect to the server and retrieve the weather information."""

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_HOST, SERVER_PORT))

    # Send a request to the server.
    client.sendall("GET_WEATHER\n".encode("utf-8"))

    weather_data = ""

    # Receive the weather information one line at a time.
    with client.makefile("r", encoding="utf-8") as response_file:
        for line in response_file:
            line = line.strip()

            if line == "END":
                break

            weather_data = weather_data + line + "\n"

    client.close()

    return weather_data


def process_weather_data(data):
    """
    -------------------------------------------------------
    Organizes the received weather information into a list.
    -------------------------------------------------------
    Parameters:
       data - Weather information received from the server,
              with each city on a separate line (str).
    Returns:
       cities - A list containing the information for each
                city. Each city is stored as a list containing
                the city name, country and temperature (list).
    -------------------------------------------------------
    Hints:
    - Create an empty list called cities.
    - Use .splitlines() to separate the city records.
    - Use a for loop to go through each record.
    - Use .split("|") to separate the information.
    - Add each city's information to the cities list.
    - Return the completed list.
    -------------------------------------------------------
    Each city list should look like:
    [city, country, temperature]
    """
    cities = []

    # Separate the data into individual city records.
    records = data.splitlines()

    for record in records:
        # Separate each record into its five fields.
        #Hint: use record.split("|")
        information = record.split("|")
        cities.append(information)

    return cities

def display_all_cities(cities):
    """
    -------------------------------------------------------
    Displays the weather information for every city.
    -------------------------------------------------------
    Parameters:
       cities - A list containing the information for each
                city (list).
    Returns:
       None
    -------------------------------------------------------
    Hints:
    - Use a for loop to go through the cities list.
    - Each city is stored as a list.
    - city[0] contains the city name.
    - city[1] contains the country.
    - city[2] contains the temperature in Celsius.
    - Use print() to display the information.
    -------------------------------------------------------
    """

    for i in cities:
        print(i)


def search_city(cities):
    """
    -------------------------------------------------------
    Searches for a city and displays its weather information.
    -------------------------------------------------------
    Parameters:
       cities - A list containing the information for each
                city (list).
    Returns:
       None
    -------------------------------------------------------
    Hints:
    - Ask the user to enter a city name.
    - Use a for loop to check each city.
    - Compare the search with the city name at index [0].
    - Display the city information if it is found.
    - Display a message if the city cannot be found.
    -------------------------------------------------------
    """
    name = input("Enter a name of a city: ").strip()
    found = False

    for city in cities:
        if city[0].lower() == name.lower():
            print(f"{city[0]}, {city[1]}, {city[2]}")
    if found == False:
        print("Sorry, that city was not found")
    

def display_menu():
    """Display the program menu."""

    print("\n===== WORLD WEATHER STATION =====")
    print("1. Display all cities")
    print("2. Search for a city")
    print("3. Exit")


def main():
    # Step 1: Connect to the server and retrieve the weather information.
    weather_data = connect_to_server()

    # Step 2: Organize the weather information into a list.
    cities = process_weather_data(weather_data)

    # Step 3: Keep showing the menu until the user chooses to exit.
    choice = ""

    while choice != "3":
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_all_cities(cities)

        elif choice == "2":
            search_city(cities)

        elif choice == "3":
            print("Thanks for using the World Weather Station!")

        else:
            print("Please enter a number from 1 to 3.")


# Start the program.
main()
