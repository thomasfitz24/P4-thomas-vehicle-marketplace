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

### Images


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

##Images
<img width="1284" height="1312" alt="Screenshot 2026-01-04 at 22 36 07" src="https://github.com/user-attachments/assets/b4d14b75-21a0-4541-a7d4-3ec85b2448f2" />
<img width="1296" height="1290" alt="Screenshot 2026-01-04 at 22 33 13" src="https://github.com/user-attachments/assets/ab84e7e7-b13b-40bd-8797-c37903b40d44" />


---

## Testing

### Manual Testing

* Navigation, filtering, authentication
* Stripe checkout flow

### Responsiveness Testing

* Desktop, tablet, and mobile layouts

### Validation Testing

* Required fields enforced

### Images
<img width="1373" height="1034" alt="Screenshot 2026-01-04 at 22 11 32" src="https://github.com/user-attachments/assets/332f5824-9fbe-406a-90ee-9d61ab7e9fd3" />
<img width="543" height="931" alt="Screenshot 2026-01-04 at 22 23 21" src="https://github.com/user-attachments/assets/137da3a3-806a-425d-859d-c9767a551a09" />
<img width="1187" height="820" alt="Screenshot 2026-01-04 at 22 23 11" src="https://github.com/user-attachments/assets/4b24c0ba-26fb-4c94-8287-a3f5bd3322b8" />
<img width="1249" height="787" alt="Screenshot 2026-01-04 at 22 12 22" src="https://github.com/user-attachments/assets/ed8caa11-dda5-41c5-a940-5c903f2311cb" />
<img width="1235" height="743" alt="Screenshot 2026-01-04 at 22 12 16" src="https://github.com/user-attachments/assets/8b499fa2-3220-42c9-ae61-a064207884a4" />
<img width="349" height="536" alt="Screenshot 2026-01-04 at 22 12 06" src="https://github.com/user-attachments/assets/d9969e3a-5104-4627-bf8f-f20d0388c312" />
<img width="362" height="647" alt="Screenshot 2026-01-04 at 22 11 59" src="https://github.com/user-attachments/assets/a51cb447-4b8f-47db-b7ed-f9f5faea95d7" />
<img width="364" height="629" alt="Screenshot 2026-01-04 at 22 11 51" src="https://github.com/user-attachments/assets/dd664e44-a671-4ce6-8c7c-d573d31fb7ca" />

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

Screenshots for commit history can be found below.

<img width="1047" height="870" alt="Screenshot 2026-01-03 at 23 31 21" src="https://github.com/user-attachments/assets/1b3ba787-9db8-48f5-af81-50691e2def10" />
<img width="918" height="1233" alt="Screenshot 2026-01-03 at 23 18 18" src="https://github.com/user-attachments/assets/4850a06c-90e8-4f61-a7c3-600a2c41f6f0" />
<img width="813" height="1179" alt="Screenshot 2026-01-03 at 23 14 07" src="https://github.com/user-attachments/assets/398edf09-5d32-4b7c-b8fe-5d7922790011" />
<img width="807" height="1144" alt="Screenshot 2026-01-03 at 23 07 08" src="https://github.com/user-attachments/assets/3bb6ec27-2c56-4b0c-8cf9-0d70349b5a5b" />
<img width="376" height="529" alt="Screenshot 2026-01-03 at 22 54 08" src="https://github.com/user-attachments/assets/75c7a16d-db85-4ced-9dce-bd3414310b2e" />
<img width="1200" height="471" alt="Screenshot 2026-01-03 at 22 09 42" src="https://github.com/user-attachments/assets/80054984-df6f-4a76-a4d7-b8953f6c2921" />
<img width="460" height="554" alt="Screenshot 2026-01-03 at 21 55 42" src="https://github.com/user-attachments/assets/ecefced7-474a-4daf-b39b-2fa5ff54790d" />
<img width="2192" height="772" alt="Screenshot 2026-01-03 at 21 50 48" src="https://github.com/user-attachments/assets/07fbf5d3-a538-4d4c-8516-0993f5cbce37" />
<img width="4" height="1" alt="Screenshot 2026-01-03 at 21 50 39" src="https://github.com/user-attachments/assets/3bd177ab-5320-43ab-8644-05d5c401aaaf" />
<img width="2558" height="537" alt="Screenshot 2026-01-03 at 21 13 35" src="https://github.com/user-attachments/assets/8f3793eb-1431-4044-a1d1-95876c598e09" />
<img width="2557" height="512" alt="Screenshot 2026-01-03 at 21 07 17" src="https://github.com/user-attachments/assets/0eebf470-a81d-49bc-a61d-de2c0aca41ce" />
<img width="465" height="509" alt="Screenshot 2026-01-03 at 21 03 03" src="https://github.com/user-attachments/assets/58c4de4b-eae5-41ef-8386-92058a9b4b02" />
<img width="2545" height="455" alt="Screenshot 2026-01-03 at 20 55 10" src="https://github.com/user-attachments/assets/8e7a9195-c532-493e-bacd-a36d5b8967e4" />
<img width="2553" height="482" alt="Screenshot 2026-01-03 at 20 54 56" src="https://github.com/user-attachments/assets/c534e83e-8ebd-49ff-b284-5a222d711b8b" />
<img width="643" height="489" alt="Screenshot 2026-01-03 at 20 47 01" src="https://github.com/user-attachments/assets/3e1151bc-430f-41b7-8df7-6a05f988287c" />
<img width="894" height="573" alt="Screenshot 2026-01-03 at 20 38 15" src="https://github.com/user-attachments/assets/26d51bc9-4ff6-439f-83bf-128348494f42" />
<img width="653" height="303" alt="Screenshot 2026-01-03 at 20 38 10" src="https://github.com/user-attachments/assets/24896645-229a-4b5e-879e-66ca08dfcc87" />
<img width="1112" height="584" alt="Screenshot 2026-01-03 at 20 28 43" src="https://github.com/user-attachments/assets/1616728b-4eb4-42db-b80d-852835685fe1" />
<img width="1160" height="451" alt="Screenshot 2026-01-03 at 19 49 35" src="https://github.com/user-attachments/assets/84582df8-4738-4943-b46e-48c4fbaf5191" />
<img width="119" height="250" alt="Screenshot 2026-01-03 at 19 41 21" src="https://github.com/user-attachments/assets/ca802bdd-35ae-40d7-a65b-a69fc582c5d9" />
<img width="222" height="381" alt="Screenshot 2026-01-03 at 19 37 42" src="https://github.com/user-attachments/assets/ed0dc6b4-1604-4603-9734-c2bdec4d852f" />
<img width="242" height="564" alt="Screenshot 2026-01-03 at 19 37 09" src="https://github.com/user-attachments/assets/61bf946f-0bf7-4042-82c6-b4fcef01c457" />
<img width="646" height="71" alt="Screenshot 2026-01-03 at 19 35 11" src="https://github.com/user-attachments/assets/51dcf51f-6914-4b88-bee6-bb7a11b3e9f7" />
<img width="2375" height="1339" alt="Screenshot 2026-01-03 at 19 32 31" src="https://github.com/user-attachments/assets/b5b80784-401f-4b38-b28c-03af8d71d68b" />
<img width="602" height="241" alt="Screenshot 2026-01-03 at 19 24 32" src="https://github.com/user-attachments/assets/75b486c4-5583-4456-a462-6a2eff58c4fb" />
<img width="785" height="75" alt="Screenshot 2026-01-03 at 19 22 03" src="https://github.com/user-attachments/assets/03bc080d-02c4-4d63-8339-e208bf769774" />
<img width="2535" height="1324" alt="Screenshot 2026-01-03 at 19 21 32" src="https://github.com/user-attachments/assets/5044c528-6e3d-45ae-a0b2-52b3641d9bb4" />
<img width="264" height="320" alt="Screenshot 2026-01-04 at 21 57 36" src="https://github.com/user-attachments/assets/a855b60e-9b40-4d93-9be2-fcfbab437d53" />
<img width="915" height="1213" alt="Screenshot 2026-01-04 at 00 08 18" src="https://github.com/user-attachments/assets/139b8537-5f32-4ec3-91da-323dbf984ffc" />
<img width="311" height="90" alt="Screenshot 2026-01-04 at 00 02 07" src="https://github.com/user-attachments/assets/d09f0f12-f62a-44a5-8a2c-2237a89f68b1" />
<img width="261" height="164" alt="Screenshot 2026-01-04 at 00 01 55" src="https://github.com/user-attachments/assets/22296682-8354-40b2-b921-17ebc6c2665e" />



