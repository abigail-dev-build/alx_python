"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

import csv
import requests

def get_user_name(employee_id):
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        employee = response.json()
        return employee
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    
def get_user_todos(id):
    url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        todos = response.json()
        return todos
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# function to export as csv
def export_to_csv(user_id, username, todos):
    file_name = f"{user_id}.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        # Write each task
        for todo in todos:
            writer.writerow([user_id, username, todo['completed'], todo['title']])
    print(f"CSV exported successfully to {file_name}")

if __name__ == "__main__":
    todos = get_user_todos(id)
    user = get_user_name(id)
    USERNAME = user['username']
        
    export_to_csv(id, USERNAME, todos)
