import platform
import subprocess
import psutil

def get_system_information():
    system_info = {}
    system_info['System'] = platform.system()
    system_info['Node Name'] = platform.node()
    system_info['Release'] = platform.release()
    system_info['Version'] = platform.version()
    system_info['Machine'] = platform.machine()
    system_info['Processor'] = platform.processor()
    return system_info

def get_ipconfig():
    ipconfig_output = subprocess.check_output(['ipconfig', '/all'], universal_newlines=True)
    return ipconfig_output

def ctrl_i_command():
    # Add functionality for Ctrl+I command
    print("Ctrl+I command executed.")

def ctrl_e_command():
    # Add functionality for Ctrl+E command
    print("Ctrl+E command executed.")

def display_services():
    # Display information about services
    services = [service.as_dict() for service in psutil.win_service_iter()]
    for service in services:
        print(service)

def display_task_manager():
    # Display information about running processes (similar to Task Manager)
    for process in psutil.process_iter(['pid', 'name', 'username']):
        print(process.info)

def main():
    while True:
        print("\nSwitch Selection Menu:")
        print("1. Get System Information")
        print("2. Run ipconfig /all command")
        print("3. Execute Ctrl+I command")
        print("4. Execute Ctrl+E command")
        print("5. Display information about services")
        print("6. Display information like Task Manager")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            print(get_system_information())
        elif choice == '2':
            print(get_ipconfig())
        elif choice == '3':
            ctrl_i_command()
        elif choice == '4':
            ctrl_e_command()
        elif choice == '5':
            display_services()
        elif choice == '6':
            display_task_manager()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
