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

# def export_all_to_json():
#     all_data = {}
# # for title in completed_titles:
#     for user_id in range(1, 11):  # Assuming there are users with IDs from 1 to 10
#         user = get_user_name(user_id)
#         if user is not None:
#             employee_name = user['name']
#             todos = get_user_todos(user_id)
#             if todos is not None:
#                 user_data = []
#                 for todo in todos:
#                     user_data.append({
#                         "username": employee_name,
#                         "task": todo['title'],
#                         "completed": todo['completed']
#                     })
#                 all_data[user_id] = user_data
    
#     file_name = "todo_all_employees.json"
#     with open(file_name, 'w') as file:
#         json.dump(all_data, file, indent=2)
    
#     print(f"JSON exported successfully to {file_name}")

# if __name__ == "__main__":
#     export_all_to_json()

def export_all_to_json():
    all_data = {}
    user_id = 1

    while True:
        user = get_user_name(user_id)
        if user is None:
            break  # No more users found, exit the loop

        employee_name = user['username']
        todos = get_user_todos(user_id)
        if todos is not None:
            user_data = []
            for todo in todos:
                user_data.append({
                    "username": employee_name,
                    "task": todo['title'],
                    "completed": todo['completed']
                })
            all_data[user_id] = user_data
        
        user_id += 1
    
    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as file:
        json.dump(all_data, file, indent=2)
    
    print(f"JSON exported successfully to {file_name}")

if __name__ == "__main__":
    export_all_to_json()
