# MVC system for sales control

Small system for sales control using simple files to save data.

Archaic system created with the aim of showing architecture using model for modelling data, dao for persistence, controller for business logic, and view for the ui.

No database was used, the system uses simple files to save and retrieve data.

The pickle library could have been used to serialize the data into a file, but it was decided to use files
simple with separation by pipes.

The aim is to show that the view can be switched to any other type of interface easily, for example,
web, desktop, mobile, etc. without having to change anything in the business rules or system logic.
