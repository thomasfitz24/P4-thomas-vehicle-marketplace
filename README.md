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

The primary goal of the Vehicle Marketplace is to deliver a full-stack, database-driven web application that allows users to browse, search, and purchase vehicles through a clear, intuitive interface. Unlike a purely informational site or an internal management tool, this project focuses on the complete user journey: discovering products, viewing detailed information, authenticating where necessary, and completing a transactional purchase. This aligns directly with the requirements of Project 4 by demonstrating a real-world Django application that integrates a relational database, multiple reusable apps, user authentication, and e-commerce functionality.

The motivation for this project is closely tied to my ongoing professional work in Search Engine Optimisation (SEO) and web development. A significant proportion of my working hours is spent delivering SEO-focused development for a range of companies, which requires a strong understanding of how users discover content and how technical decisions influence visibility, performance, and usability. Search Engine Optimisation in this context refers to improving a website’s structure, content, and technical foundations to increase its visibility in search engine results. This includes semantic HTML, clean URL structures, fast load times, mobile responsiveness, accessible layouts, and well-organised, database-driven content.

Working in this way allows me to continually expand my skills across both front-end and back-end development, as SEO often exposes weaknesses in poorly structured applications. As a result, many of my design and implementation choices are informed by real-world requirements rather than purely academic exercises. This project provided an opportunity to apply those principles within a controlled full-stack build, ensuring that navigation, search functionality, template structure, and data modelling were aligned with both user experience and technical SEO best practices.

The idea for the Vehicle Marketplace was also strongly influenced by my work with Shoreline Vehicles, where I spend approximately 40% of my working hours. As a business that relies heavily on online visibility and lead generation, Shoreline Vehicles requires systems that not only present vehicles attractively but are also structured in a way that supports discoverability, scalability, and long-term maintainability. Through this work, it became clear that a dedicated, database-driven marketplace would provide far more control and flexibility than static listings or third-party platforms.

From a full-stack development perspective, this created a clear opportunity to combine structured relational data with interactive front-end features. Core entities such as Product and Category form the foundation of the data model, while Django views, templates, and forms provide controlled access to that data. Authentication and authorisation separate public users from staff and administrators, and Stripe integration extends the application beyond basic CRUD by introducing real payment processing and user feedback flows.

The specific problem the project addresses is the lack of a cohesive, end-to-end system for showcasing vehicles and handling transactions within a single platform. Without such a system, businesses must rely on disconnected tools for browsing, enquiries, and payments, which increases friction for users and complexity for administrators. The Vehicle Marketplace resolves this by providing a centralised solution where users can browse vehicles, filter by category, view detailed specifications and descriptions, and complete a purchase within the same application.

The scope of the project is intentionally focused on demonstrating core full-stack principles rather than advanced commercial features. While the application includes authentication and secure payment processing, it does not yet implement features such as user dashboards, order history, or inventory analytics. These constraints ensure that the fundamental requirements of Project 4—relational data modelling, CRUD functionality, user interaction, e-commerce integration, testing, version control, and deployment—are implemented clearly and to a strong standard.

In summary, the Vehicle Marketplace exists to solve a clear real-world problem: providing a structured, professional, and transactional platform for showcasing and selling vehicles online. By combining Django’s back-end capabilities with a responsive front end, SEO-aware structure, and secure payment integration, the project delivers a practical full-stack solution while directly meeting the learning outcomes and assessment criteria of Project 4.

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

### Images


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

### Key Commit Text

* Initial repository setup
* Create Django project and verify initial run
* Clean project structure and confirm Django setup
* Add product and category models and register in admin
* Add product views and connect product URLs
* Display products on public marketplace with working templates
* Add category filtering to product listings
* Add basic global styling and static files
* Fix auth template path for Django login view
* Fix base template structure and add staff admin link
* Display product images on product list and detail pages
* Add product search functionality
* Add checkout app with success and cancel pages
* Implement Stripe checkout with payment success and cancel feedback
* Refactor base template with structured header, search bar and auth buttons
* Remove duplicate search form from main content and rely on header search
* Enhance vehicle detail page with structured layout and purchase action
* Restructure vehicle detail page with image-first layout and separated purchase and details sections
* Add product description field and display detailed vehicle information
* Improve product detail layout with structured sections and description content
* Improve responsive product grid layout across screen sizes
* Improve UI styling for category filters and back to vehicles navigation
* Add centred cancel page with return to marketplace button
* Create initial README with project overview
* Add project purpose and target audience to README
* Add UX and accessibility documentation to README
* Add project overview and purpose to README
* Add user stories defining application interactions
* Add features overview to README
* Add data model description to README
* Document CRUD functionality in README
* Add authentication and authorisation section to README
* Document Stripe e-commerce payment functionality
* Add testing documentation to README
* Add security considerations to README
* Add technologies used section to README

Screenshots of commit history can be found below.
