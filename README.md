# Frameworks Assignment - Anna Keil

## Project Description
I developed this web application because in my current role at the company I am working for, the need for an application to effectively track employees' training hours arose. We need to have records on who is giving and receiving trainings and exactly how many hours were spent giving or receiving training per employee.


## Project Details
My web application uses the Django framework integrated with a PostgreSQL database for data management. I am storing employees, inter-user messages and the training records for employees. I used modern HTML, CSS powered by Bootstrap, and dynamic JavaScript functionality throughout the development.

Application Structure:
- Backend Framework: Django
- Database: PostgreSQL
- Frontend: HTML, CSS, JavaScript

## Database Description
The application uses Django models to manage `Employees`, `Training` records, and internal `Messages`.

The Training model stores information about employee training courses and sessions.

As for Training Types, Training can be categorised as either: 1 - internal, 2 - external. As for Training Status, 4 disctint categories have been used: 1 - Ongoing, 2 - Planned, 3 - Completed, 4 -Failed. 

These all contain and carry crucial data, central to the application. I used Django migrations to create the database and manage the tables. I am using a combination of built in Django admin panels and custom registration forms to handle user creation. 

I built custom forms for such as login, password reset, registration, creating registration, creating training, and logout.


## Deployed site

This site has been deployed to GitHub Pages at the URL below:

[https://github.com/annakeil2/frameworksassignment_trainingtracker](https://github.com/annakeil2/frameworksassignment_trainingtracker)

Link to render.com deployment below:

[https://frameworksassignment-trainingtracker.onrender.com/](https://frameworksassignment-trainingtracker.onrender.com/)

Admin user access supplied in submission. 