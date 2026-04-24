# CS340-Final

Kate Wheeler
CS 340: Client/Server Development
Final Project

This scenario is fictional for educational purposes.

Grazioso Salvare, an innovative international rescue animal training company, has contracted Global Rain to create a web interface which will help them as they interact with their database of animals that are associated with shelters. Their purpose in interacting with this database will be identifying dogs which are fit to perform various kinds of rescues: water, mountain or wilderness, or human tracking. The web app includes the database, as well as an interactive dropdown allowing the user to pick one or more type of rescue and view only results relevant to their interests. Below the database display is a pie chart displaying breeds (in the visible dataset) and a map which automatically pins the location of the selected animal in the database.
The code of the app exists in two main files, one Python and one Python Notebook (.ipynb). The Python file creates the database instance for interaction using some hard-coded values, then defines the four main CRUD functions: Create, Read, Update, and Delete. The Python Notebook file implements the dashboard: first importing the necessary libraries, then defining the page’s layout using HTML divs, then calling the aspects of the dashboard one-by-one. This starts with the dropdown and its check-boxes, followed by the table itself, then the pie chart, and finally the map. 
