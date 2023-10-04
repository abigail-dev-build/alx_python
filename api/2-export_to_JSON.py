"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
import json
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

# function to export as json
def export_to_json(user_id, username, todos):
    file_name = f"{user_id}.json"
    data = {user_id: []}
    
    for todo in todos:
        data[user_id].append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        })
    
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)
    
    print(f"JSON exported successfully to {file_name}")

if __name__ == "__main__":
    todos = get_user_todos(id)
    user = get_user_name(id)
    USERNAME = user['username']

    export_to_json(id, USERNAME, todos)
