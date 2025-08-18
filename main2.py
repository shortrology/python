from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

#Create FastAPI app instance
app = FastAPI()

#Define the data model for a Todo item

class Todo(BaseModel):      # Object representing a To-Do item
    id: int                 # Unique identifier for the todo item
    task: str               # Description of the task
    done: bool = False      # Status of the task (default: not done)


# In-memory list to store todos
# In a real app, you would use a database

todos: List[Todo] = []

# Create a new todo item
# This endpoint adds a new todo item to the list

@app.post("/todo/add-item")
def add_item_in_todo(item: Todo):
    todos.append(item)
    return {
        "message": "Item added successfully",
        "item": item,
        "success": True
    }
    
# Get all todo items
# This endpoint retrieves all todo items from the list

@app.get("/todo/get-items")
def get_items_from_todo():
    return {
        "message": "Items retrieved successfully",
        "items": todos,
        "total_items": len(todos),
        "success": True
    }
    
# Get a todo item by id
# This endpoint retrieves a todo item by its unique id

@app.get("/todo/get-item/{item_id}")
def get_item_by_id(item_id: int):
    for todo in todos:
        if todo.id == item_id:
            return {
                "message": "Item found",
                "item": todo,
                "success": True
            }
    return {
        "message": f"No item found with id {item_id}",
        "success": False
    }

# Update an existing todo item
# This endpoint updates a todo item by replacing it with the provided updated item

@app.put("/todo/update-item")
def update_item(updated_item: Todo):
    for index, todo in enumerate(todos):
        if todo.id == updated_item.id:
            todos[index] = updated_item
            return {
                "message": "Item updated successfully",
                "item": updated_item,
                "success": True
            }
    return {
        "message": f"No item found with id {updated_item.id}",
        "success": False
    }
        
# Delete a todo item by id
# This endpoint deletes a todo item by its unique id

@app.delete("/todo/delete-item")
def delete_item_from_todo(item_id: int):
    if len(todos) > 0:
        for todo_item in todos:
            print(todo_item, item_id)
            if todo_item.id == item_id:
                todos.remove(todo_item)
                return {
                    "message": "Item deleted successfully",
                    "item": todo_item,
                    "success": True
                }
            else:
                return {
                    "message": "Item not found / matched",
                    "success": False
                }
    else:
        return {
            "message": "No items found in the To-Do list",
            "success": False
        }
    

# To run this app:
# 1. Install FastAPI and Uvicorn: pip install fastapi uvicorn
# 2. Run: uvicorn main:app --reload
# 3. Open http://127.0.0.1:8000/docs for interactive API documentation
# create an update endpoint to update a todo item
# create a get by id endpoint to get a specific todo item