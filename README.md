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
