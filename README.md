# Vehicle Marketplace – Django Full Stack Application

## Project Overview

This project is a full-stack vehicle marketplace web application built using the Django framework. The application allows users to browse available vehicles, filter by category, view detailed vehicle information, and purchase vehicles through an integrated Stripe payment system.

The project demonstrates the use of Django’s Model-View-Template (MVT) architecture, relational databases, user authentication, and third-party payment integration. It has been designed to meet accessibility, usability, and responsive design principles across desktop and mobile devices.

This application was developed as **Project 4** for the **Level 5 Diploma in Web Application Development**.

# Vehicle Marketplace

A full stack Django web application that allows users to browse, search, and purchase vehicles online.

This project was developed using the Django framework with a relational database and multiple reusable apps. It includes user authentication, an admin interface, and Stripe-based checkout functionality.

This application was created as Project 4 for the Level 5 Diploma in Web Application Development.

## Project Purpose

The purpose of the Vehicle Marketplace application is to provide users with a clear and intuitive platform for browsing vehicles, viewing detailed information, and completing a secure online purchase.

The application demonstrates a real-world full stack e-commerce workflow, including product listing, search and filtering, authentication, and online payments. It is designed to reflect how a modern vehicle marketplace might function at a small-to-medium business scale.

## Target Audience

The target audience for this application includes:

- Users looking to browse and purchase vehicles online
- Administrators managing vehicle listings and categories
- Businesses requiring a simple, secure vehicle sales platform

The interface is designed to be easy to navigate for first-time users while still providing full control and management capabilities for administrators.


## User Experience (UX)

The application is designed with a clear and consistent layout to ensure users can easily navigate and understand the purpose of the site immediately.

Key UX features include:

- A persistent header with navigation, search functionality, and authentication controls
- A responsive grid layout that adapts to different screen sizes
- Card-based vehicle listings for clear visual separation
- Dedicated vehicle detail pages with structured information and clear calls to action
- Feedback pages for successful and cancelled purchases

Users have full control of their interaction with the application, including browsing, searching, filtering by category, viewing detailed information, and completing purchases.

## Accessibility

Accessibility considerations were included throughout development, including:

- High colour contrast between text and background for readability
- Semantic HTML structure using headings, navigation elements, and sections
- Clear button styling and consistent interactive elements
- Responsive design supporting mobile, tablet, and desktop screen sizes
- Alt text for vehicle images where applicable

These considerations ensure the application is usable by a wide range of users and aligns with modern accessibility best practices.


## User Stories

### Visitor (Unauthenticated User)

- As a visitor, I want to browse available vehicles so that I can view what is for sale without creating an account.
- As a visitor, I want to search and filter vehicles by category so that I can quickly find relevant listings.
- As a visitor, I want to view detailed information about a vehicle so that I can decide whether I want to purchase it.
- As a visitor, I want to register or log in so that I can make a purchase.

### Registered User

- As a registered user, I want to log in securely so that I can access purchase functionality.
- As a registered user, I want to complete a payment using Stripe so that I can safely buy a vehicle.
- As a registered user, I want to see feedback after a successful or cancelled payment so that I understand the outcome of my transaction.

### Admin User

- As an admin user, I want to create, edit, and delete vehicles so that I can manage marketplace listings.
- As an admin user, I want to manage categories so that vehicles are organised logically.

## Features

### General Features

- Responsive layout that works on desktop, tablet, and mobile devices.
- Clear navigation with a fixed header and footer.
- Clean, card-based vehicle listing layout for easy browsing.
- Search functionality allowing users to find vehicles by name.
- Category filtering to help users narrow down vehicle listings.

### Product Management

- Vehicle listings displayed as cards with image, price, year, and mileage.
- Dedicated vehicle detail pages with full information and description.
- Admin-only access to create, update, and delete vehicles and categories via the Django admin panel.

### Authentication & Authorisation

- User authentication using Django’s built-in authentication system.
- Login and logout functionality.
- Admin users have additional permissions to manage marketplace content.
- Non-admin users are prevented from accessing the database directly.

### E-commerce Functionality

- Secure vehicle purchases using Stripe Checkout.
- Payment success page confirming completed transactions.
- Payment cancellation page providing user feedback and return navigation.

### Accessibility & UX

- High-contrast header and footer for readability.
- Buttons styled consistently across the site.
- Forms use clear labels and placeholders.
- Layout designed to be intuitive and easy to navigate for first-time users.


## Data Model

The application uses a relational database implemented with Django’s ORM.
The data model is designed to reflect a real-world vehicle marketplace and consists of the following core entities:

### Category Model

The Category model is used to group vehicles into logical categories.

**Fields:**

- `name` – Name of the category
- `slug` – URL-friendly identifier

**Purpose:**

- Allows vehicles to be filtered and organised
- Improves navigation and user experience

### Product Model

The Product model represents an individual vehicle listing.

**Fields:**

- `name` – Vehicle name
- `slug` – URL-friendly identifier
- `price` – Vehicle price
- `year` – Year of manufacture
- `mileage` – Vehicle mileage
- `description` – Detailed vehicle description
- `image` – Vehicle image
- `is_available` – Availability status
- `category` – Foreign key relationship to Category

**Relationships:**

- One Category can be associated with many Products (one-to-many relationship)

This relational structure allows efficient querying, filtering, and management of vehicle listings while maintaining data integrity.


## CRUD Functionality

The application implements full CRUD (Create, Read, Update, Delete) functionality using Django’s models, views, templates, and admin interface.

### Create

- Administrators can create new vehicle categories and vehicle listings via the Django admin panel.
- Vehicle creation includes validation for required fields such as name, price, year, and mileage.

### Read

- All users (including anonymous users) can browse available vehicles.
- Users can view a list of vehicles displayed in a card-based layout.
- Each vehicle has a dedicated detail page displaying full information, including images and descriptions.

### Update

- Administrators can edit existing vehicle listings and categories through the Django admin interface.
- Changes made to vehicle details are immediately reflected in the user interface.

### Delete

- Administrators can remove vehicles and categories from the system using the Django admin panel.
- Deleted records are permanently removed from the database and no longer visible to users.

This approach ensures that all database operations are securely handled through the application logic, preventing unauthorised access to the data store.


## Authentication & Authorisation

The application uses Django’s built-in authentication system to manage user access and permissions.

### Authentication

- Users can log in and log out using Django’s authentication views.
- Login pages are only accessible to unauthenticated users.
- Authenticated users can access additional functionality such as purchasing vehicles.

### Authorisation

- Administrator (staff) users have full access to the Django admin panel.
- Only admin users can create, edit, or delete vehicle listings and categories.
- Non-admin users are prevented from accessing or modifying the data store directly.
- All sensitive operations are handled securely through Django’s permission system.

This ensures that user data and marketplace content are protected while allowing appropriate access based on user roles.



## E-commerce & Payments

The application includes e-commerce functionality implemented using Stripe Checkout to allow users to securely purchase vehicles online.

### Stripe Integration

- Stripe is used as the online payment processing system.
- Secure Checkout Sessions are created using Stripe’s Python API.
- Sensitive Stripe keys are stored as environment variables and are not committed to the repository.

### Payment Flow

1. Users select a vehicle and click the “Buy Vehicle” button.
2. A Stripe Checkout session is created server-side.
3. Users are redirected to Stripe’s secure checkout page.
4. Upon successful payment, users are redirected to a payment success page.
5. If a payment is cancelled, users are redirected to a cancellation page with the option to return to the marketplace.

### User Feedback

- A clear success message is displayed after a completed purchase.
- A cancellation message is displayed if the user exits the payment process.
- Navigation options are provided to return users back to the marketplace.

This implementation ensures a secure, user-friendly checkout experience while following best practices for handling payments.
