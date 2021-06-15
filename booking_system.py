# ----------------------------------------------------------------------------------- #
# Title: Booking System
# Description: Take information inputted by user to find the best route for a package
#               Intended for developer to make front end, basics for user.
# ChangeLog (Jack Kennedy,06/13/2020,Reread to not overcomplicate things):
# JJack,6.13.2021,Created started script
# Jack Kennedy, 06/13/2021, Worked on script
# ----------------------------------------------------------------------------------- #
# GOALS
# Set up Data Structure to save PACKAGE INFO AND OUTCOME to CSV file = Not finished
# Create process to book ONE PACKAGE, DON"T NEED TO DO SEVERAL!!! = Not Finished
#           Note: ACTUAL DELIVERY DATE DOES NOT MATTER!!! Either it's below or over 3 days
# Create a Menus including: 1. Book Quote Package, 2. Display History of Packages, 3. Exit
#           Note: Project does not call for editing data. Do not need to create script to
#           extract data to edit booking information. Could be added, not required.
#           Script only serves one purpose, doesn't need big menu.
#           Honestly, the history part is only for testing. Don't even need that.
# Create a set of variables to compare all booking options, then display THE CHEAPEST ONE(S)!!! to user
#           Note: User might be curious to know what the other options are. Not required, but could
#           add an option at the end to display what all options look like.
#           ONLY NEED THE CHEAPEST OPTION TO SAVE TO CSV FILE

# Imports
import csv
import datetime
from csv import writer

# Data
    # Storage
masterList = []
dicRow = {}
    # Global Variables to create Dictionaries
name = ""
packageD = ""
dangerous = ""
weight = None
volume = None
delDate = None
length = None
height = None
width = None
price = None


# Processing
class Processor:
    # Reads the CSV file and captures it into "masterList", a list that stores dictionaries.
    @staticmethod
    def read_data_from_file_master_list():
        global masterList
        global dicRow
        with open('booking_data.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print("Loading in booking_data.csv File...")
                line_count += 1
                dicRow = {"Name": row["Name"],
                          "Package Description": row["Package Description"],
                          "Dangerous": row["Dangerous"],
                          "Weight": row["Weight"],
                          "Volume": row["Volume"],
                          "Days Until Delivery": row["Days Until Delivery"],
                          "Price": row["Price"]}
                masterList.append(dicRow)
                line_count += 1

    @staticmethod
    def append_to_master_file():
        global name
        global packageD
        global dangerous
        global weight
        global volume
        global delDate
        dicRow = {"Name": name,
                  "Package Description": packageD,
                  "Dangerous": dangerous,
                  "Weight": weight,
                  "Volume": volume,
                  "Day Until Delivery": delDate,
                  "Price": price}
        masterList.append(dicRow)

    # Takes data currently captured in the script and saves it to the CSV file.
    @staticmethod
    def save_data_to_csv_file():
        List_saving = [name, packageD, dangerous, weight, volume, delDate, price]
        with open("booking_data.csv", mode="a") as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List_saving)
            f_object.close()
            print("The file had been updated")

    # Captures name of package sender
    @staticmethod
    def capture_name():
        global name
        name = input("Name of Sender: ")

    # Captures package description in a string
    @staticmethod
    def capture_description():
        global packageD
        packageD = input("Description of Package: ")

    # Has user choose one of only two choices for dangerous
    @staticmethod
    def determine_danger():
        global dangerous
        while True:
            dangerous = str(input("Are the contents of this package dangerous (yes or no): ")).lower().strip()
            if dangerous == "yes":
                break
            if dangerous == "no":
                break
            else:
                print("Please enter yes or no.")

    # Gets the weight as a float to allow decimals
    @staticmethod
    def capture_weight():
        global weight
        weight = input("Weight in Kilograms (Kg): ")
        weight = float(weight)

    # Uses a formula to get the total volume and check each side
    @staticmethod
    def capture_volume():
        global volume
        global height
        global width
        global length
        while type(volume).__name__ != "float":
            try:
                height = float(input("Enter the height: "))
                length = float(input("Enter the length: "))
                width = float(input("Enter the width: "))
                volume = height * length * width
                print("The volume of your package is", volume," cubic meters")
            except ValueError:
                print("Please only enter numbers.")
            if type(volume).__name__ == 'float':
                break

    @staticmethod
    def days_for_delivery():
        global delDate
        while type(delDate).__name__ != "int":
            try:
                delDate = int(input("In how many days will this package be sent?: "))
            except ValueError:
                print("Please only enter whole numbers.")
            if type(delDate).__name__ == 'int':
                break

    @staticmethod
    def calculate_best_bookings():
        global price
        air_op1 = 10.0 * weight
        air_op2 = 20.0 * volume
        air_options = [air_op1, air_op2]
        air = max(air_options)
        if dangerous == "yes" and delDate < 3:
            print("Booking quote is flat rate $45 by Truck")
            price = 45
        if dangerous == "yes" and delDate >= 3:
            print("Booking quote is flat rate $25 by Truck")
            price = 25
        if dangerous == "no" and delDate < 3:
            words = "Booking quote is ${} by Air"
            print(words.format(air))
            price = air
        if dangerous == "no" and delDate >= 3:
            choice_list = [air, 25, 30]
            best_choice = min(choice_list)
            if best_choice == 25:
                print("Booking quote is flat rate $25 by Truck")
                price = 25.0
            if best_choice == 30:
                print("Booking quote is flat rate $30 by Boat")
                price = 30.0
            if best_choice < 25:
                words_1 = "Booking quote is ${} by Air"
                print(words_1.format(air))
                price = air


    @staticmethod
    def reset():
        global name
        global packageD
        global dangerous
        global weight
        global volume
        global delDate
        global length
        global height
        global width
        global price
        name = ""
        packageD = ""
        dangerous = ""
        weight = None
        volume = None
        delDate = None
        length = None
        height = None
        width = None
        price = None

# Presentation


class Presentation:

    # Allows the user to choose options.
    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 4] - "))
        print()
        return choice

    # Brings up the menu
    @staticmethod
    def print_menu_tasks():
        print("""
                   HR System
                *** Menu of Options ***
                1) Booking Quote for Package
                2) Display Shipping Rules and Prices
                3) Display Booking Quote History
                4) Exit

                *Reminder*:
                If needed data may be changed
                in the "booking_data.csv file       
                """)

    @staticmethod
    def today_date():
        print("Today's Date Is:", datetime.date.today())

    @staticmethod
    def display_rules_and_prices():
        print("""
                    The rules for shipping are:
                Packages have to be below 10Kg
                Packages Have to be smaller than 5x5x5 meters
                    - If any side exceeds 5 meters it can't be shipped
                If the package contains dangerous goods air will be unavailable
                If the package is Urgent(Under 3 Days), air will be the only choice
                
                    Prices for Shipping are:
                Truck = Flat Rate $25 ($45 if Urgent)
                Ocean = Flat Rate $30 (No Urgent Option)
                Air   = $10 per Kilogram OR $20 per Cubic Meter, The Higher of the Two
                """)

    @staticmethod
    def overweight_allowance():
        print("The weight entered is over the allowed amount (10kg).\n"
              "You will be returned to the menu as this package\n"
              "won't be able to be sent.")

    # If package dimensions go over user will go back to menu
    @staticmethod
    def over_volume_allowance():
        if length > 5.0:
            over_length = """
                            The length {} meters is over the allowed measurement.
                            You will be returned to the menu as this package
                            won't be able to be sent."""
            print(over_length.format(length))
        if width > 5.0:
            over_width = """
                            The width {} meters is over the allowed measurement.
                            You will be returned to the menu as this package
                            won't be able to be sent."""
            print(over_width.format(width))
        if height > 5.0:
            over_height = """
                             The height {} meters is over the allowed measurement.
                             You will be returned to the menu as this package
                             won't be able to be sent."""
            print(over_height.format(height))
        if volume > 125.0:
            over_volume = """
                            The volume total {} is over the allowed volume.
                            You will be returned to the menu as this package
                            won't be able to be sent."""
            print(over_volume.format(volume))
        else:
            pass

    @staticmethod
    def display_master_list(big_list):
        print("\tThis is a history of all booking quotes.\n"
              "===================================================")
        print("{:^18}".format("Name"), "{:^18}".format("Package Description"), "{:^18}".format("Dangerous"),
              "{:^18}".format("Weight"), "{:^18}".format("Volume"), "{:^18}".format("Days Until Delivery"),
              "{:^18}".format("Price"))
        counter = 0
        for row in big_list:
            print("{:^18}".format(row["Name"]), "{:^18}".format(row["Package Description"]),
                  "{:^18}".format(row["Dangerous"]), "{:^18}".format(row["Weight"]),
                  "{:^18}".format(row["Volume"]), "{:^18}".format(row["Days Until Delivery"]),
                  "{:^18}".format(row["Price"]))
            counter += 1

# Main Body of Script
Processor.read_data_from_file_master_list()
Presentation.today_date()
while True:
    Presentation.print_menu_tasks()
    strChoice = Presentation.input_menu_choice()

    if strChoice.strip() == "1":
        Processor.capture_name()
        Processor.capture_description()
        Processor.determine_danger()
        Processor.capture_weight()
        if weight >= 10:
            Presentation.overweight_allowance()
            Processor.reset()
        else:
            Processor.capture_volume()
            if width > 5 or height > 5 or length > 5 or volume > 125:
                Presentation.over_volume_allowance()
                Processor.reset()
            else:
                Processor.days_for_delivery()
                Processor.calculate_best_bookings()
                Processor.append_to_master_file()
                Processor.save_data_to_csv_file()
                Processor.reset()

    if strChoice.strip() == "2":
        Presentation.display_rules_and_prices()

    if strChoice.strip() == "3":
        Presentation.display_master_list(masterList)

    if strChoice.strip() == "4":
        print("Goodbye!")
        break
