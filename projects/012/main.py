import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_boot_menu():
    clear_screen()
    print("=== FAKE BOOT MENU ===")
    print("1. Boot Windows 11")
    print("2. Boot Linux (Ubuntu)")
    print("3. Boot in Safe Mode")
    print("4. Enter BIOS Setup")
    print("5. Exit")
    print("======================")

def boot_sequence(os_name):
    print(f"\nLoading {os_name}...")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    print(f"\n{os_name} booted successfully!\n")

while True:
    show_boot_menu()
    choice = input("Select an option (1-5): ")

    if choice == '1':
        boot_sequence("Windows 11")
    elif choice == '2':
        boot_sequence("Linux (Ubuntu)")
    elif choice == '3':
        boot_sequence("Safe Mode")
    elif choice == '4':
        print("\nOpening BIOS Settings...")
        time.sleep(2)
        print("You are now in the BIOS setup. (Just kidding 😄)\n")
    elif choice == '5':
        print("\nExiting Boot Menu. Goodbye!")
        break
    else:
        print("\nInvalid choice! Please try again.\n")
    
    input("Press Enter to return to menu...")
