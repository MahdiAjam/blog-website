# Blog Website - Django Project

## Overview
This is my second Django project that is a feature-rich blogging platform that allows users to **register**, **log in**, **create** and **manage articles**, **comment**, and **reply to comments**. The platform is built using Django, providing a secure and scalable foundation for the application.

## Features
- **User Authentication**: The project implements Django's built-in authentication system, allowing users to securely register, log in, and log out.
- **OTP Registration**: A custom registration system using one-time password (OTP) verification sent to users' phone numbers for added security.

- **Password Recovery**: If users forget their password, they can reset it via an email containing a secure reset link. 
- **Profile Management**: Users can update their personal information and upload profile pictures via a dedicated profile management page.
- **Article Management**: Authenticated users can create, update, and delete articles. The articles have dedicated detail views to showcase content.
- **Commenting System**: Users can comment on articles, and the system supports nested replies for discussions.
- **Pagination**: Articles, comments, and other lists are paginated for a seamless browsing experience, even with large datasets.
- **Admin Panel**: Django's admin interface is customized to manage users, articles, and comments efficiently.

## Installation

### Prerequisites
- Python 3.8+
- Django 4.0+
- pip (Python package manager)
- A database system (e.g., SQLite, PostgreSQL, MySQL)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/mahdiajam-blog-website.git
   ```
2. Navigate to the project directory:
   ```bash
   cd mahdiajam-blog-website
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```bash
   python manage.py runserver
   ```
8. Access the application in your browser:
   - Default: `http://127.0.0.1:8000`
   - Admin: `http://127.0.0.1:8000/admin`


## Project Structure
```
mahdiajam-blog-website/
├── manage.py
├── utils.py
├── account/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── managers.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_otpcode.py
│   │   ├── 0003_user_description_user_image.py
│   │   ├── 0004_relation.py
│   │   └── __init__.py
│   └── templates/
│       └── account/
│           ├── edit_profile.html
│           ├── login.html
│           ├── password_reset_complete.html
│           ├── password_reset_confirm.html
│           ├── password_reset_done.html
│           ├── password_reset_email.html
│           ├── password_reset_form.html
│           ├── profile.html
│           ├── register.html
│           └── verify.html
├── article/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_comment.py
│   │   ├── 0003_alter_comment_reply.py
│   │   └── __init__.py
│   └── templates/
│       └── article/
│           ├── article.html
│           ├── create.html
│           ├── detail.html
│           └── update.html
├── blog/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   └── templates/
│       └── home/
│           ├── about.html
│           ├── contact.html
│           └── home.html
├── static/
│   ├── css/
│   │   ├── flex-slider.css
│   │   ├── fontawesome.css
│   │   ├── owl.css
│   │   └── templatemo-stand-blog.css
│   ├── fonts/
│   │   ├── Flaticon.woff
│   │   ├── FontAwesome.otf
│   │   ├── flexslider-icon.eot
│   │   ├── flexslider-icon.ttf
│   │   ├── flexslider-icon.woff
│   │   ├── fontawesome-webfont.eot
│   │   ├── fontawesome-webfont.ttf
│   │   ├── fontawesome-webfont.woff
│   │   ├── fontawesome-webfont.woff2
│   │   ├── slick.eot
│   │   ├── slick.ttf
│   │   └── slick.woff
│   ├── images/
│   ├── js/
│   │   ├── accordions.js
│   │   ├── custom.js
│   │   ├── isotope.js
│   │   ├── owl.js
│   │   └── slick.js
│   └── vendor/
│       ├── bootstrap/
│       │   ├── css/
│       │   └── js/
│       └── jquery/
└── templates/
    ├── base.html
    └── includes/
        ├── Adbaner.html
        ├── footer.html
        ├── head.html
        ├── header.html
        ├── messages.html
        ├── script.html
        └── sidebar.html
```

## Technologies Used
- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default, but can be replaced with PostgreSQL, MySQL, etc.)
- **OTP Handling**: Phone-based OTP verification
- **Libraries**: FontAwesome, Bootstrap, Owl Carousel

## License
This project is licensed under the [MIT License](LICENSE).

## Contribution
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.

## Contact
For questions or support, contact **Mahdi Ajam** at **mahdiajam8754@gmail.com**.

