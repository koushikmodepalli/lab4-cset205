class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightDatabase:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights_by_city(self, city):
        result = []
        for flight in self.flights:
            if city.lower() in (flight.source.lower(), flight.destination.lower()):
                result.append(flight)
        return result

    def search_flights_from_city(self, city):
        result = []
        for flight in self.flights:
            if city.lower() == flight.source.lower():
                result.append(flight)
        return result

    def search_flights_between_cities(self, source, destination):
        result = []
        for flight in self.flights:
            if source.lower() == flight.source.lower() and destination.lower() == flight.destination.lower():
                result.append(flight)
        return result

def main():
    database = FlightDatabase()

    # Adding flights to the database
    database.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    database.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    database.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    database.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    database.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    database.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    while True:
        print("Search Options:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            city = input("Enter the city name: ")
            result = database.search_flights_by_city(city)
            if result:
                for flight in result:
                    print(f"Flight ID: {flight.flight_id}, Source: {flight.source}, Destination: {flight.destination}, Price: {flight.price}")
            else:
                print("No flights found for the specified city.")
        
        elif choice == 2:
            city = input("Enter the source city name: ")
            result = database.search_flights_from_city(city)
            if result:
                for flight in result:
                    print(f"Flight ID: {flight.flight_id}, Source: {flight.source}, Destination: {flight.destination}, Price: {flight.price}")
            else:
                print("No flights found from the specified city.")
        
        elif choice == 3:
            source = input("Enter the source city name: ")
            destination = input("Enter the destination city name: ")
            result = database.search_flights_between_cities(source, destination)
            if result:
                for flight in result:
                    print(f"Flight ID: {flight.flight_id}, Source: {flight.source}, Destination: {flight.destination}, Price: {flight.price}")
            else:
                print("No flights found between the specified cities.")
        
        elif choice == 4:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
