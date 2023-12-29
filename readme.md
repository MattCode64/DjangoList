# DjangoList

---

## Description

This is a simple Django project (DRF) that allows you to create a list of items. You can add, edit, and delete items from the list. You can also mark items as complete.

---

## Models

### Collection
- title: CharField
- slug: SlugField


### Task
- title: CharField
- slug: SlugField
- description : TextField
- complete: BooleanField
- created: DateTimeField
- collection: ForeignKey
- updated: DateTimeField (later)
- due_date: DateTimeField (later)

---

### Features

- [x] Create a new collection
- [x] Delete an existing collection
- [x] Create a new task (in a collection)
- [x] Edit an existing task
- [x] Delete an existing task
- [x] Mark a task as complete

---

### Installation

1. Clone this repository: `git clone https://github.com/MattCode64/todolist`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install the requirements: `pip install -r requirements.txt`