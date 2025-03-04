# Crochet Inventory System

Welcome to the Crochet Inventory System! This application provides an efficient way to manage crochet items, inventory, and orders, offering a robust backend with flexible API endpoints for seamless integration.

## Features

- **Item Management**: Add, edit, and delete crochet items with relevant details (e.g., name, type, quantity, price, and description).
- **Inventory Tracking**: Monitor stock levels and get alerts for low inventory.
- **Order Management**: Manage customer orders with statuses like pending, completed, and canceled.
- **Authentication**: Secure user authentication using JWT for admin and staff roles.
- **Categories and Tags**: Organize crochet items with categories and tags for better management.
- **Search and Filtering**: Search inventory and orders by name, category, or status.
- **Reports**: Generate sales and inventory reports.

## Tech Stack

- **Backend**: Django, Django REST Framework (DRF)
- **Database**: MySQL

## Installation

### Prerequisites

- Python (v3.8 or higher)
- MySQL
- Virtual Environment (optional but recommended)

### Setup Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/crochet-inventory.git
   cd crochet-inventory
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database in `settings.py`:**

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',  # Use 'django.db.backends.mysql' for MySQL
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',
           'PORT': '5432',  # Use '3306' for MySQL
       }
   }
   ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser for admin access:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

## Authentication

The project uses JWT for secure authentication. Install and configure Djoser for user management.

1. **Install required packages:**

   ```bash
   pip install djangorestframework-simplejwt
   ```

2. **Update `INSTALLED_APPS` in `settings.py`:**

   ```python
   INSTALLED_APPS = [
       ...,  
       'rest_framework',
       'rest_framework_simplejwt',
   ]
   ```

3. **Configure REST framework and JWT settings in `settings.py`:**

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       ),
   }

   SIMPLE_JWT = {
       'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
       'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
   }
   ```


## Usage

- **Admin Panel**: Accessible at `/admin/` for managing inventory and orders.
- **API Endpoints**: Use tools like Postman or curl to interact with the API.

## Contributing

1. **Fork the repository:**

   ```bash
   git clone https://github.com/yourusername/crochet-inventory.git
   cd crochet-inventory
   ```

2. **Create a new branch:**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit your changes:**

   ```bash
   git commit -m 'Add new feature'
   ```

4. **Push to the branch:**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request on GitHub.**

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For questions or feedback, email me at stharabi9862187405@gmail.com.
