
# Vehicle Marketplace – Django Full Stack Application

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Rationale]()
3. [Project Purpose]()
4. [Target Audience]()
5. [User Experience (UX)]()
6. [Accessibility]()
7. [Wireframes](#wireframes)
8. [User Stories](#user-stories)
9. [Features](#features)
10. [Data Model](#data-model)
11. [CRUD Functionality]()
12. [Authentication &amp; Authorisation]()
13. [E-commerce &amp; Payments]()
14. [Testing](#testing)
15. [Security]()
16. [Technologies Used](#technologies-used)
17. [Version Control &amp; Git Commit History]()

---

## Project Overview

This project is a full-stack vehicle marketplace web application built using the Django framework. The application allows users to browse available vehicles, filter by category, view detailed vehicle information, and purchase vehicles through an integrated Stripe payment system.

The project demonstrates the use of Django’s Model-View-Template (MVT) architecture, relational databases, user authentication, and third-party payment integration. It has been designed to meet accessibility, usability, and responsive design principles across desktop and mobile devices.

This application was developed as **Project 4** for the  **Level 5 Diploma in Web Application Development** .

---

## Project Rationale

The rationale behind this project was to design and build a realistic, production-style full stack web application that reflects real-world e-commerce requirements.

A vehicle marketplace was chosen as the domain because it naturally requires:

* Relational data modelling
* Search and filtering functionality
* Authentication and authorisation
* Secure online payments
* Clear separation between user and admin roles

This project demonstrates the ability to plan, design, build, test, and document a complete Django-based application using industry-standard practices.

---

## Project Purpose

The purpose of the Vehicle Marketplace application is to provide users with a clear and intuitive platform for browsing vehicles, viewing detailed information, and completing a secure online purchase.

The application demonstrates a real-world full stack e-commerce workflow, including product listing, search and filtering, authentication, and online payments. It is designed to reflect how a modern vehicle marketplace might function at a small-to-medium business scale.

---

## Target Audience

The target audience for this application includes:

* Users looking to browse and purchase vehicles online
* Administrators managing vehicle listings and categories
* Businesses requiring a simple, secure vehicle sales platform

The interface is designed to be easy to navigate for first-time users while still providing full control and management capabilities for administrators.

---

## User Experience (UX)

The application is designed with a clear and consistent layout to ensure users can easily navigate and understand the purpose of the site immediately.

Key UX features include:

* A persistent header with navigation, search functionality, and authentication controls
* A responsive grid layout that adapts to different screen sizes
* Card-based vehicle listings for clear visual separation
* Dedicated vehicle detail pages with structured information and clear calls to action
* Feedback pages for successful and cancelled purchases

Users have full control of their interaction with the application, including browsing, searching, filtering by category, viewing detailed information, and completing purchases.

---

## Accessibility

Accessibility considerations were included throughout development, including:

* High colour contrast between text and background for readability
* Semantic HTML structure using headings, navigation elements, and sections
* Clear button styling and consistent interactive elements
* Responsive design supporting mobile, tablet, and desktop screen sizes
* Alt text for vehicle images where applicable

---

## Wireframes

Wireframes were created during the planning stage to establish layout structure, navigation flow, and content hierarchy before development began.

### Desktop Wireframes

### Mobile Wireframes

*(Wireframe images to be added to the `docs/wireframes/` directory.)*

---

## User Stories

### Visitor (Unauthenticated User)

* Browse vehicles without logging in
* Search and filter vehicles by category
* View detailed vehicle information
* Register or log in to make a purchase

### Registered User

* Log in securely
* Complete payments using Stripe
* Receive feedback after successful or cancelled payments

### Admin User

* Create, edit, and delete vehicles
* Manage vehicle categories

---

## Features

### General Features

* Responsive design across all devices
* Card-based vehicle listings
* Search and category filtering

### Product Management

* Vehicle detail pages
* Admin-only CRUD functionality

### Authentication & Authorisation

* Login/logout system
* Admin permissions enforced

### E-commerce Functionality

* Stripe Checkout integration
* Payment success and cancellation feedback

---

## Data Model

### Category Model

* name
* slug

### Product Model

* name
* slug
* price
* year
* mileage
* description
* image
* is_available
* category (ForeignKey)

---

## CRUD Functionality

* **Create:** Admin creates vehicles and categories
* **Read:** Users browse and view vehicles
* **Update:** Admin edits listings
* **Delete:** Admin removes listings

---

## Authentication & Authorisation

* Django authentication system
* Admin-only access to admin panel
* Non-admin users restricted from data modification

---

## E-commerce & Payments

* Stripe Checkout integration
* Secure environment variable key storage
* Success and cancellation pages

---

## Testing

### Manual Testing

* Navigation, filtering, authentication
* Stripe checkout flow

### Responsiveness Testing

* Desktop, tablet, and mobile layouts

### Validation Testing

* Required fields enforced
* Invalid inputs rejected

---

## Security

* Environment variables for secrets
* Django ORM for database protection
* Restricted admin access
* Input validation

---

## Technologies Used

* Python 3
* Django
* SQLite
* HTML5
* CSS3
* Stripe API
* Git & GitHub

---

## Version Control & Git Commit History

Git was used throughout the project to document the development process and track incremental changes.

### Key Commit Examples

* Initial Django project setup
* Core app and product models added
* Authentication and admin configuration
* Product listing and detail templates
* Stripe checkout integration
* UI styling and responsive layout
* README documentation updates

Screenshots of commit history can be found below:
