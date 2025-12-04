#!/usr/bin/env python3

# OPS435 Assignment 1
# check_apache_log_aabel3 .py
# Author: Avraham Abel

# Allowing the sys.argv to allow it to be done on the terminal/cmd
import sys


def load_logs(file_list):
    """Prints each filename that would be loaded."""
    for filename in file_list:
        print(f"Loading {filename}")

# Displaying the title to be displayed
def display_title(title):
    """Displays a formatted title with the appropate matching equal signs."""
    print(title)
    print("=" * len(title))

# Menu naviation script to ensure that it's properly looped
def main_menu():
    """Displays the main menu and proper navigation."""
    while True:
        display_title("Apache Log Analyser - Main Menu")
        print("1) Successful Requests")
        print("2) Failed Requests")
        print("q) Quit")
        choice = input("What would you like to do? ").strip().lower()
        if choice == '1':
            successful_requests_menu()
        elif choice == '2':
            failed_requests_menu()
        elif choice == 'q':
            break
        else:
            print("Invalid option. Try again.")

# Sub menu nativation script beyond the main menu script to ensure it's proper
def successful_requests_menu():
    """The successful requests submenu. And unsuccesful ones get filtered"""
    while True:
        display_title("Apache Log Analyser - Successful Requests Menu")
        print("1) How many total requests (Code 200)")
        print("2) How many requests from Seneca (IPs starting with 142.204)")
        print("3) How many requests for OPS435_Lab")
        print("q) Return to Main Menu")
        choice = input("What would you like to do? ").strip().lower()
        if choice == '1':
            total_requests_200()
        elif choice == '2':
            requests_from_seneca()
        elif choice == '3':
            requests_for_ops435_lab()
        elif choice == 'q':
            break
        else:
            print("Invalid option. Try again.")

# Currently we got placeholder functions that haven't been implemented til assignment 1 part 2
def failed_requests_menu():
    """Handles failed requests submenu."""
    while True:
        display_title("Apache Log Analyser - Failed Requests Menu")
        print("1) How many total \"Not Found\" requests (Code 404)")
        print("2) How many 404 requests contained \"hidebots\" in the URL")
        print("3) Print all IP addresses that caused a 404 response")
        print("q) Return to Main Menu")
        choice = input("What would you like to do? ").strip().lower()
        if choice == '1':
            total_requests_404()
        elif choice == '2':
            requests_with_hidebots()
        elif choice == '3':
            ip_addresses_404()
        elif choice == 'q':
            break
        else:
            print("Invalid option. Try again.")

# Placeholder texts of the correct choices display "Not implemented yet" to the user
def total_requests_200():
    """Placeholder for counting total 200 responses."""
    print("Not implemented yet")

def requests_from_seneca():
    """Placeholder for counting requests from Seneca IPs."""
    print("Not implemented yet")

def requests_for_ops435_lab():
    """Placeholder for counting requests for OPS435_Lab."""
    print("Not implemented yet")

def total_requests_404():
    """Placeholder for counting total 404 responses."""
    print("Not implemented yet")

def requests_with_hidebots():
    """Placeholder for counting 404s with 'hidebots' in URL."""
    print("Not implemented yet")

def ip_addresses_404():
    """Placeholder for listing IPs causing 404s."""
    print("Not implemented yet")

# Main script to ensure it executes correctly
if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Error: No arguments provided.")
        sys.exit(1)

    if args[0] in ['--default', '-d']:
        if len(args) < 2:
            print("Error: No filenames provided with --default.")
            sys.exit(1)
        load_logs(args[1:])
        total_requests_200()
    else:
        load_logs(args)
        main_menu()
