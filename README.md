

# Vehicle Marketplace – Django Full Stack Application

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Rationale](#project-rationale)
3. [Project Purpose](#project-purpose)
4. [Target Audience](#target-audience)
5. [User Experience (UX)](#user-experience-ux)
6. [Accessibility](#accessibility)
7. [Wireframes](#wireframes)
8. [User Stories](#user-stories)
9. [Features](#features)
10. [Data Model](#data-model)
11. [CRUD Functionality](#crud-functionality)
12. [Authentication & Authorisation](#authentication--authorisation)
13. [E-commerce & Payments](#e-commerce--payments)
14. [Testing](#testing)
15. [Security](#security)
16. [Critical Development Issues & Debugging](#critical-development-issues--debugging)
17. [Technologies Used](#technologies-used)
18. [Version Control & Git Commit History](#version-control--git-commit-history)
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
<img width="1536" height="1024" alt="wireframe " src="https://github.com/user-attachments/assets/401c47f5-90a4-4911-b483-48bfb496950d" />


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

### Assessor Access

For assessment and testing purposes, a pre-registered user account is available:

* **Username:** `user`
* **Password:** `user`

---

## E-commerce & Payments

* Stripe Checkout integration
* Secure environment variable key storage
* Success and cancellation pages

## Images
<img width="507" height="766" alt="Screenshot 2026-01-06 at 22 46 34" src="https://github.com/user-attachments/assets/353bdc4a-87e3-4eb1-94e6-30731e1c8f06" />
<img width="502" height="775" alt="Screenshot 2026-01-06 at 22 45 20" src="https://github.com/user-attachments/assets/2b1661cc-1cb9-48fe-b624-09af994d96d3" />
<img width="519" height="775" alt="Screenshot 2026-01-06 at 22 45 14" src="https://github.com/user-attachments/assets/b8d3fea7-d562-4fd8-bc44-6b7fb1ff8e67" />

---

## Testing!


### Manual Testing

* Navigation, filtering, authentication
* Stripe checkout flow

### Responsiveness Testing

* Desktop, tablet, and mobile layouts
<img width="366" height="448" alt="Screenshot 2026-01-06 at 22 46 41" src="https://github.com/user-attachments/assets/37176089-8962-4b94-8d95-b7077df563ed" />
<img width="507" height="766" alt="Screenshot 2026-01-06 at 22 46 34" src="https://github.com/user-attachments/assets/aff961ff-dd5f-4c3d-94f5-dd8eae831fa8" />
<img width="502" height="775" alt="Screenshot 2026-01-06 at 22 45 20" src="https://github.com/user-attachments/assets/5727d2d8-f550-48a8-8958-fcec0d17dc80" />
<img width="519" height="775" alt="Screenshot 2026-01-06 at 22 45 14" src="https://github.com/user-attachments/assets/ebda8ac5-db21-4399-a598-a39ba5f6c197" />
<img width="701" height="810" alt="Screenshot 2026-01-06 at 22 45 05" src="https://github.com/user-attachments/assets/a35d83f7-1ea0-4cb4-9b67-036adbb3cf2b" />
<img width="787" height="823" alt="Screenshot 2026-01-06 at 22 44 56" src="https://github.com/user-attachments/assets/a27a65c7-bb6e-4a37-bdad-03663b587870" />
<img width="1465" height="816" alt="Screenshot 2026-01-06 at 22 44 31" src="https://github.com/user-attachments/assets/bba8ef2a-7c66-4d5b-b277-f4d6d6cfa05e" />
<img width="1464" height="835" alt="Screenshot 2026-01-06 at 22 44 18" src="https://github.com/user-attachments/assets/81e1a1d9-456d-445d-82be-4011eec8c730" />


### Validation Testing

* Required fields enforced
<img width="1077" height="725" alt="Screenshot 2026-01-06 at 22 36 09" src="https://github.com/user-attachments/assets/a0569b84-175e-4796-98cf-785a6d558f99" />
<img width="1207" height="501" alt="Screenshot 2026-01-06 at 22 34 28" src="https://github.com/user-attachments/assets/db190235-08d4-493c-80e4-462aad49984a" />
<img width="1067" height="633" alt="Screenshot 2026-01-06 at 22 33 58" src="https://github.com/user-attachments/assets/9d71d10a-b1a4-42ec-97a1-c37c29abe5f8" />
<img width="1135" height="469" alt="Screenshot 2026-01-06 at 22 33 36" src="https://github.com/user-attachments/assets/ed911976-d368-4971-b897-9b8c1d3f7cae" />
<img width="1146" height="586" alt="Screenshot 2026-01-06 at 22 32 55" src="https://github.com/user-attachments/assets/a02f748a-abf9-4394-bcea-19e1a5240b05" />
<img width="1264" height="625" alt="Screenshot 2026-01-06 at 22 32 36" src="https://github.com/user-attachments/assets/be27f0bd-a496-4a48-a1be-cbf3f010a8bf" />
<img width="1218" height="584" alt="Screenshot 2026-01-06 at 22 31 53" src="https://github.com/user-attachments/assets/27d4101d-51a5-4dac-9d1a-6bef4483352a" />


## Security

* Environment variables for secrets
* Django ORM for database protection
* Restricted admin access
* Input validation

---

## Critical Development Issues & Debugging

During the development and deployment of this project, a significant challenge was encountered regarding static file handling and media storage on Heroku. This section documents the debugging process, root causes, and solutions.

### Static Files & Media Upload Issue – Debugging Summary

**Overview**
During deployment of this Django application to Heroku, a critical production issue occurred where:

* CSS stopped loading entirely.
* `collectstatic` reported 0 files collected.
* Media uploads (product images) failed to persist or display.
* 500 errors appeared only when `DEBUG=False`.

The issue took approximately 3 days (~15 hours) to fully diagnose. Although the final fix involved changing only one line, the difficulty came from silent failures caused by conflicting storage backends.

**Initial Symptoms**
The issue began after the following sequence:

1. The app deployed successfully to Heroku.
2. Cloudinary was added for image uploads.
3. CSS changes were made post-deployment.
4. CSS stopped loading in production.
5. `collectstatic` began returning: `0 static files copied`.

Despite this, `findstatic css/style.css` succeeded, templates used `{% load static %}` correctly, and the app worked locally with `DEBUG=True`. This strongly suggested Django could see the static files but was refusing to collect or serve them.

### Root Cause #1 – Cloudinary / Static Files Conflict

**Actual Cause**
The core issue was `cloudinary_storage` being present in `INSTALLED_APPS` while also using WhiteNoise for static files. This caused Django’s staticfiles pipeline to silently short-circuit, resulting in:

* `collectstatic` collecting 0 files.
* No error messages.
* Static files appearing to exist but never being served.

**The Fix**
Static and media responsibilities were separated: WhiteNoise for static files and Cloudinary for media uploads only.
The fix was simply to remove `cloudinary_storage` from `INSTALLED_APPS`.
Once removed, `collectstatic` immediately began copying files, CSS loaded correctly, and production no longer returned 500 errors.

### Root Cause #2 – ImageField on Heroku

**Media Upload Issue**
After static files were fixed, a second issue surfaced where images uploaded via `/admin` disappeared after refresh or dyno restarts.

**Actual Cause**
The Product model originally used:

**Python**

```
models.ImageField(upload_to="products/")
```

This stores files on the local filesystem, which is ephemeral on Heroku and does not persist.

**The Fix – Use CloudinaryField**
The Product model was updated to use Cloudinary directly:

**Python**

```
from cloudinary.models import CloudinaryField

image = CloudinaryField("image", blank=True, null=True)
```

This ensured admin uploads go directly to Cloudinary and media URLs remain valid in production.

### Configuration

**Environment Variable Configuration**
A `ValueError` initially occurred because the Cloudinary URL was not set in the environment. This was resolved by exporting the variable:

**Bash**

```
export CLOUDINARY_URL=cloudinary://API_KEY:API_SECRET@CLOUD_NAME
```

This was added to the Heroku Config Vars.

**Final Working Setup**

* **Static Files:** Handled by WhiteNoise, served from `/staticfiles`. `cloudinary_storage` is **not** in `INSTALLED_APPS`.
* **Media Files:** Handled by Cloudinary using `CloudinaryField`.

**Why This Is Documented**
This section exists to demonstrate real-world debugging and problem-solving, show an understanding of Django deployment internals, and prevent future regressions.

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

<img width="1122" height="277" alt="Screenshot 2026-01-04 at 22 38 28" src="https://github.com/user-attachments/assets/bba6c602-21b6-49a3-82b2-f7b0344ea5df" />
<img width="1287" height="1236" alt="Screenshot 2026-01-04 at 22 38 12" src="https://github.com/user-attachments/assets/47ad23cf-7e28-4340-9948-e87c8d05295c" />
<img width="1296" height="1290" alt="Screenshot 2026-01-04 at 22 33 13" src="https://github.com/user-attachments/assets/54201e4c-2bc6-417b-97e7-232a7cf79b86" />
<img width="1249" height="787" alt="Screenshot 2026-01-04 at 22 12 22" src="https://github.com/user-attachments/assets/065b01c1-6a1c-4550-ae9f-3c2be91bcfac" />
<img width="1235" height="743" alt="Screenshot 2026-01-04 at 22 12 16" src="https://github.com/user-attachments/assets/07333216-0d49-4c82-b387-b5fe28d30730" />
<img width="349" height="536" alt="Screenshot 2026-01-04 at 22 12 06" src="https://github.com/user-attachments/assets/ac82fceb-f7bf-4a92-a209-f13e2b8ab243" />
<img width="362" height="647" alt="Screenshot 2026-01-04 at 22 11 59" src="https://github.com/user-attachments/assets/1abf1283-4eb3-4d81-ac50-e49594af25fc" />
<img width="364" height="629" alt="Screenshot 2026-01-04 at 22 11 51" src="https://github.com/user-attachments/assets/ba348816-169b-411c-abde-83f0ebf7eab6" />
<img width="1373" height="1034" alt="Screenshot 2026-01-04 at 22 11 32" src="https://github.com/user-attachments/assets/7b871187-5e0e-4d96-b3ce-d9a440583653" />
<img width="915" height="1213" alt="Screenshot 2026-01-04 at 00 08 18" src="https://github.com/user-attachments/assets/658cad93-2c27-45fd-b8d1-713b7beb6a14" />
<img width="311" height="90" alt="Screenshot 2026-01-04 at 00 02 07" src="https://github.com/user-attachments/assets/f29a3c61-2e5b-4dd2-bde3-8781541cdb85" />
<img width="261" height="164" alt="Screenshot 2026-01-04 at 00 01 55" src="https://github.com/user-attachments/assets/17581a90-4603-4583-acb3-0ca6c4ce7088" />
<img width="1047" height="870" alt="Screenshot 2026-01-03 at 23 31 21" src="https://github.com/user-attachments/assets/c3492937-ec3d-474f-bf8d-a38f4b97b262" />
<img width="918" height="1233" alt="Screenshot 2026-01-03 at 23 18 18" src="https://github.com/user-attachments/assets/203c22f8-a0b6-4036-9378-2f0643191c2a" />
<img width="813" height="1179" alt="Screenshot 2026-01-03 at 23 14 07" src="https://github.com/user-attachments/assets/0d1acc8c-f271-43ea-adde-77f5e0bd0e8f" />
<img width="807" height="1144" alt="Screenshot 2026-01-03 at 23 07 08" src="https://github.com/user-attachments/assets/46d9e58c-04b9-4f4b-8e44-942f6e8f1e82" />
<img width="376" height="529" alt="Screenshot 2026-01-03 at 22 54 08" src="https://github.com/user-attachments/assets/9bf1806b-6560-4f1d-ab80-d18fb8ae68a0" />
<img width="1200" height="471" alt="Screenshot 2026-01-03 at 22 09 42" src="https://github.com/user-attachments/assets/8f5d0547-8a7e-4f42-a28b-273305982dbd" />
<img width="460" height="554" alt="Screenshot 2026-01-03 at 21 55 42" src="https://github.com/user-attachments/assets/3223dec9-9d6e-4501-93d3-de14a12e8e66" />
<img width="2192" height="772" alt="Screenshot 2026-01-03 at 21 50 48" src="https://github.com/user-attachments/assets/765c9142-7955-43a4-baa3-9d9a3673971b" />
<img width="4" height="1" alt="Screenshot 2026-01-03 at 21 50 39" src="https://github.com/user-attachments/assets/b604ae3b-0ca0-410b-bf53-7c4303613c1c" />
<img width="2558" height="537" alt="Screenshot 2026-01-03 at 21 13 35" src="https://github.com/user-attachments/assets/b8302222-17c4-4ddf-acf0-7a5c6e96aa61" />
<img width="2557" height="512" alt="Screenshot 2026-01-03 at 21 07 17" src="https://github.com/user-attachments/assets/b8b327ed-b104-43f4-9f92-69417822efc1" />
<img width="465" height="509" alt="Screenshot 2026-01-03 at 21 03 03" src="https://github.com/user-attachments/assets/b1b5831e-8aa9-40a3-898e-78057fe13650" />
<img width="2545" height="455" alt="Screenshot 2026-01-03 at 20 55 10" src="https://github.com/user-attachments/assets/452de418-747e-4c4f-9348-4721b3dd0559" />
<img width="2553" height="482" alt="Screenshot 2026-01-03 at 20 54 56" src="https://github.com/user-attachments/assets/88d7eeb9-3631-47c3-a260-8d449c2167d4" />
<img width="643" height="489" alt="Screenshot 2026-01-03 at 20 47 01" src="https://github.com/user-attachments/assets/96b70a62-b210-432f-8126-d2b00241fe01" />
<img width="894" height="573" alt="Screenshot 2026-01-03 at 20 38 15" src="https://github.com/user-attachments/assets/3ce6d532-d63e-4175-b8fd-f83728e82ef0" />
<img width="653" height="303" alt="Screenshot 2026-01-03 at 20 38 10" src="https://github.com/user-attachments/assets/dd6fa87c-a465-4c9a-8781-b1830c58fdc1" />
<img width="1112" height="584" alt="Screenshot 2026-01-03 at 20 28 43" src="https://github.com/user-attachments/assets/9d2b1a06-aa97-471f-a089-afdfd1426790" />
<img width="1160" height="451" alt="Screenshot 2026-01-03 at 19 49 35" src="https://github.com/user-attachments/assets/d50b4cb2-a925-466d-8f6a-021f6ccb5334" />
<img width="119" height="250" alt="Screenshot 2026-01-03 at 19 41 21" src="https://github.com/user-attachments/assets/4e24431c-a2fd-470c-ab51-56f0ad68da90" />
<img width="222" height="381" alt="Screenshot 2026-01-03 at 19 37 42" src="https://github.com/user-attachments/assets/6c49c08d-af07-4927-8fa0-2cba586d5522" />
<img width="242" height="564" alt="Screenshot 2026-01-03 at 19 37 09" src="https://github.com/user-attachments/assets/830e896e-5bbb-43b3-9b87-506041d8943e" />
<img width="646" height="71" alt="Screenshot 2026-01-03 at 19 35 11" src="https://github.com/user-attachments/assets/39b4a7de-9bf3-49b7-a91d-d6ff5759c6a2" />
<img width="2375" height="1339" alt="Screenshot 2026-01-03 at 19 32 31" src="https://github.com/user-attachments/assets/929508d4-1d8e-4e6c-aabc-8091f820a116" />
<img width="602" height="241" alt="Screenshot 2026-01-03 at 19 24 32" src="https://github.com/user-attachments/assets/168a357b-7724-429d-8f47-9ccb4e0164c7" />
<img width="785" height="75" alt="Screenshot 2026-01-03 at 19 22 03" src="https://github.com/user-attachments/assets/7150cea3-3027-47b1-a9f7-2f535b2cd2fb" />
<img width="2535" height="1324" alt="Screenshot 2026-01-03 at 19 21 32" src="https://github.com/user-attachments/assets/1b73df38-37ad-41c4-92f0-1127c1a54c84" />
<img width="554" height="382" alt="Screenshot 2025-12-31 at 15 41 05" src="https://github.com/user-attachments/assets/0ea99231-e273-43b4-8edd-4c9356485eea" />
<img width="1184" height="759" alt="Screenshot 2025-12-31 at 12 40 25" src="https://github.com/user-attachments/assets/bd2f1877-04bb-4b1e-83ef-f22fa2f5e02d" />
<img width="432" height="573" alt="Screenshot 2026-01-05 at 21 41 03" src="https://github.com/user-attachments/assets/39aabc99-69e9-4f57-bb88-8ef7f96a2337" />
<img width="299" height="555" alt="Screenshot 2026-01-05 at 20 39 47" src="https://github.com/user-attachments/assets/12839a4b-a06d-46cf-a086-c2593e7f2f8c" />
<img width="230" height="118" alt="Screenshot 2026-01-05 at 20 38 58" src="https://github.com/user-attachments/assets/0d7107ef-51af-478a-8d13-1abfad72f3ce" />
<img width="231" height="208" alt="Screenshot 2026-01-05 at 20 30 56" src="https://github.com/user-attachments/assets/d43f512d-81e8-4a66-bf1a-6ca1802fcc7c" />
<img width="223" height="153" alt="Screenshot 2026-01-05 at 19 10 39" src="https://github.com/user-attachments/assets/c3799088-bb59-4466-bcf6-f9708300f5f4" />
<img width="1333" height="1341" alt="Screenshot 2026-01-06 at 21 35 48" src="https://github.com/user-attachments/assets/cdc97922-382b-4f52-b6ef-171458690975" />
<img width="519" height="129" alt="Screenshot 2026-01-06 at 19 50 55" src="https://github.com/user-attachments/assets/f1bf2986-7aa3-4cc5-8cca-4bdd5ad1dfd0" />
<img width="287" height="447" alt="Screenshot 2026-01-06 at 18 57 56" src="https://github.com/user-attachments/assets/5d6d31d9-eae7-4c22-8c11-04ee13ab71b8" />
<img width="748" height="1382" alt="Screenshot 2026-01-06 at 12 22 53" src="https://github.com/user-attachments/assets/bfe8e5f5-d492-493c-838b-91ae33bf4114" />

