
# WeatherServer.py
# Run this program before running WeatherClient.py.

import socket

HOST = "127.0.0.1"
PORT = 12345

# Each city is stored as:
# City|Country|TemperatureC

weather_data = [
    "Toronto|Canada|12",
    "London|United Kingdom|15",
    "Tokyo|Japan|21",
    "Sydney|Australia|24",
    "Paris|France|16",
    "Calgary|Canada|9",
    "Miami|United States|29",
    "Rome|Italy|22",
    "Auckland|New Zealand|17",
    "Cairo|Egypt|32"
]


def send_weather_data(client):
    """Send the weather information to the client."""

    for city in weather_data:
        client.sendall((city + "\n").encode("utf-8"))

    # Tell the client that all records have been sent.
    client.sendall("END\n".encode("utf-8"))


def handle_client(client, address):
    """Handle a request from a client."""

    print("Connected to:", address)

    try:
        with client.makefile("r", encoding="utf-8") as request_file:
            request = request_file.readline().strip()

        if request == "GET_WEATHER":
            print("Sending weather information...")
            send_weather_data(client)
        else:
            client.sendall("INVALID_REQUEST\n".encode("utf-8"))
            print("Invalid request received.")

    except OSError as error:
        print("Connection error:", error)

    finally:
        client.close()
        print("Connection closed.")


def main():
    """Start the weather server."""

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    print("Weather server is running.")
    print("Waiting for clients...")

    while True:
        client, address = server.accept()
        handle_client(client, address)


main()
