# DjangoList

---

## Description

This is a simple Django project (DRF) that allows you to create a list of items.
You can add, edit, and delete items from the list. You can also mark items as complete.

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

---

### Frontend

The frontend is built with Vue.js and is located in the `frontend` directory.
To run the frontend, you must have Node.js installed, Vue CLI, and axios.

1. Install Node.js: `sudo apt install nodejs`
2. Install Vue CLI: `npm install -g @vue/cli`
3. Create a new Vue project: `vue create .` or `vue create frontend`
4. Install axios: `npm install axios` (in the `frontend` directory)

Install also the following package:

`pip install django-cors-headers` (in requirements.txt)

---

### Run the project

1. Run the backend: `python manage.py runserver`
2. Run the frontend: `npm run serve` (in the `frontend` directory)

---

### Conclusion

This is a simple project that I made to learn Django and DRF.
I really not get in deep with the frontend, but I will do it in the future, maybe.
I just coded the links between the frontend and the backend and display the data of collections.