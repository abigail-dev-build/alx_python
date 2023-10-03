"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

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

todos = get_user_todos(id)
user = get_user_name(id)
EMPLOYEE_NAME = user['name']
TOTAL_NUMBER_OF_TASKS = len(todos)
completed_titles = [todo['title'] for todo in todos if todo['completed']]
NUMBER_OF_DONE_TASKS = len(completed_titles)



if todos is not None:
    print(f"Employee {EMPLOYEE_NAME} is done with tasks ({NUMBER_OF_DONE_TASKS} / {TOTAL_NUMBER_OF_TASKS}): ")
for title in completed_titles:
    print("\t " + title)
