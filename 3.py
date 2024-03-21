import random
import time

def generate_sensor_values():
    """Generate random sensor values for temperature, humidity, and CO2."""
    temperature = random.uniform(-50, 50)  # Generate a random temperature between -50 and 50 Celsius
    humidity = random.uniform(0, 100)  # Generate a random humidity value between 0% and 100%
    co2 = random.uniform(300, 2000)  # Generate a random CO2 level between 300ppm and 2000ppm
    return temperature, humidity, co2

def main():
    while True:
        # Generate random sensor values
        temperature, humidity, co2 = generate_sensor_values()
        
        # Print the sensor values with two decimal places for temperature and CO2, and one decimal place for humidity
        print(f"Temperature: {temperature:.2f} °C, Humidity: {humidity:.1f}%, CO2: {co2:.2f} ppm")
        
        # Wait for a specified interval (e.g., 5 seconds) before generating the next set of values
        time.sleep(5)

if __name__ == "__main__":
    main()
