# CS340-Final

Kate Wheeler

CS 340: Client/Server Development

Final Project

This scenario is fictional for educational purposes.

Grazioso Salvare, an innovative international rescue animal training company, has contracted Global Rain to create a web interface which will help them as they interact with their database of animals that are associated with shelters. Their purpose in interacting with this database will be identifying dogs which are fit to perform various kinds of rescues: water, mountain or wilderness, or human tracking. The web app includes the database, as well as an interactive dropdown allowing the user to pick one or more type of rescue and view only results relevant to their interests. Below the database display is a pie chart displaying breeds (in the visible dataset) and a map which automatically pins the location of the selected animal in the database.

The code of the app exists in two main files, one Python and one Python Notebook (.ipynb). The Python file creates the database instance for interaction using some hard-coded values, then defines the four main CRUD functions: Create, Read, Update, and Delete. The Python Notebook file implements the dashboard: first importing the necessary libraries, then defining the page’s layout using HTML divs, then calling the aspects of the dashboard one-by-one. This starts with the dropdown and its check-boxes, followed by the table itself, then the pie chart, and finally the map. 

Module 8 Journal:

I try to maintain readability and adaptability in my apps my commenting extensively: it helps that at this point the only one trying to adapt my apps is me. The CRUD module which I interacted with using a different file each week is a great example: by commenting well and using value but still meaningful variable names, I've ensured that I can come back to this functionality again and again. An interesting quirk of this term for me was two classes with final projects that relied on CRUD modules to interact with/creatively display the contents of a dababase table (the other was an Android app for a book collection: see the CS 360-Final if you're interested!) so I've gained a real appreciation for how necessary this logic will be for interacting with data in future projects. 

The real guiding goal in my choice of major/concentration was not based around a passion for computer science but a desire for data accessibility. The volume of data we have, in all fields, is such that we may never truly analyze even a small portion of it. Yet, concise and accurate answers to nearly any question someone may have is at our fingertips if we can figure out how to access it (AI is swell as an administrative tool, but it's simply aggregating existing analysis unless explicitly told otherwise). A project such as this, aggregating the population of several animal shelters, can have dozens of applications from research to adoption event planning to lost pet sites and more. 
