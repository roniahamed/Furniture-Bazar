# 🪑 Furniture Bazar - Furniture Selling Platform

[![Django Version](https://img.shields.io/badge/Django-4.0-green.svg)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Bootstrap Version](https://img.shields.io/badge/Bootstrap-5-purple.svg)](https://getbootstrap.com/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-orange.svg)](https://www.mysql.com/)

A comprehensive e-commerce platform for furniture retail built with Django. This full-featured online store provides a seamless shopping experience with modern design and robust functionality.
## 🖼️ Preview

![Furniture Bazar Main Screenshot](https://github.com/roniahamed/img/blob/master/furniture%20bazar%20main.png?raw=true)

*Screenshot of the Furniture Bazar homepage. Explore the live site below!*
## 🌐 Live Demo

**[🔗 Visit Furniture Bazar](https://furniturebazar2.pythonanywhere.com/)**

*Experience the live application with all features including user registration, product browsing, shopping cart, and checkout process.*

## 📋 Project Overview

Furniture Bazar is a complete e-commerce solution designed specifically for furniture retailers. Built with Django and modern web technologies, it offers a professional shopping experience with comprehensive administrative tools for business management.

The platform serves both customers looking for quality furniture and business owners who need a reliable e-commerce solution with powerful backend management capabilities.

## ✨ Features

### 🔐 User Management
- **Secure Authentication**: Secure registration, login, and logout functionality for a personalized experience.
- **User Profiles**: Personal account management with order history
- **Session-Based Security**: Secure user sessions and data protection

### 🛍️ Shopping Experience
- **Product Catalog**: Comprehensive display of furniture organized by categories
- **Dynamic Product Pages**: Detailed view for each product with high-quality images, descriptions, pricing, and stock status.
- **Advanced Search & Filtering**: Users can easily search for specific products or filter the entire catalog by category.
- **Shopping Cart**: A fully functional session-based shopping cart where users can add, update quantities, and remove products.
- **Wishlist Functionality**: Allows users to save their favorite products to a personal wishlist for later purchase.
- **Multi-Step Checkout**: A multi-step checkout process to collect shipping information and place an order efficiently.

### 📱 User Interface
- **Responsive Design**: Bootstrap 5 powered interface optimized for all devices
- **Mobile-First Approach**: Seamless experience on desktops, tablets, and smartphones
- **Modern UI/UX**: Clean, professional design with intuitive navigation

### 🔧 Administrative Tools
- **Django Admin Panel**: Comprehensive backend management system
- **Product Management**: Easy addition, editing, and removal of products
- **Category Management**: Organize products with flexible category system
- **Order Management**: Track and manage customer orders
- **User Management**: Administrative control over user accounts

### 📊 Business Features
- **Order History**: Complete order tracking for registered users
- **Inventory Management**: Track product availability and stock levels
- **Category Organization**: Hierarchical product categorization


## 🛠️ Technologies Used

### Backend
- **Python 3.9**: Core programming language
- **Django 4.0**: Web framework for rapid development
- **Gunicorn**: WSGI HTTP Server for deployment
- **Django ORM**: Database abstraction layer

### Frontend
- **HTML5**: Modern markup language
- **CSS3**: Advanced styling and animations
- **Bootstrap 5**: Responsive UI framework
- **JavaScript**: Dynamic client-side functionality

### Database
- **MySQL**: Reliable relational database management system

### Deployment
- **PythonAnywhere**: Cloud hosting platform
- **Static Files Management**: Optimized asset delivery

## ⚙️ Setup and Installation (Local)
Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.9 or higher
- MySQL database server (Make sure the service is running)
- Git (for cloning the repository)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/roniahamed/Furniture-Bazar.git
   cd Furniture-Bazar
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv furniture_env
   source furniture_env/bin/activate  # On Windows: furniture_env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the MySQL Database:**
    -   Log in to your MySQL server and create a new database for the project.
        ```sql
        CREATE DATABASE furniture_bazar_db;
        ```
    -   It is also recommended to create a dedicated user for this database.
   
   **Configure Database Settings:**
    -   Open the `FurnitureBazar/settings.py` file.
    -   Locate the `DATABASES` setting and update it with your MySQL credentials. **Do not commit your credentials to a public repository.**

    ```python []
    # In FurnitureBazar/settings.py

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'furniture_bazar_db', # Your database name
            'USER': 'your_mysql_user',     # Your MySQL username
            'PASSWORD': 'your_mysql_password', # Your MySQL password
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

5. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   -   **Main Site:** Open your web browser and go to `http://127.0.0.1:8000/`
   -   **Admin Panel:** Go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.

## 📁 Project Structure

Here is a brief overview of the project's directory structure:

```
├── FurnitureBazar/    # Main Django project configuration (settings.py, urls.py)
├── accounts/          # App for user authentication (login, register, dashboard)
├── cart/              # App for shopping cart logic
├── core/              # App for core views (home, about, contact)
├── orders/            # App for order creation and management
├── store/             # App for products, categories, and main store logic
├── wishlist/          # App for wishlist functionality
├── templates/         # HTML templates for the entire project
├── static/            # Static files (CSS, JavaScript, Images)
├── media/             # User-uploaded files (product images)
├── manage.py          # Django's command-line utility
└── requirements.txt   # Project dependencies
```
## 📄 Documentation

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=furniture_bazar
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
```

### Production Settings
For production deployment, ensure:
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Set up proper static files serving
- Configure email backend for order confirmations
- Set up SSL certificates

## 🎯 Usage Examples

### Adding Products (Admin)
1. Access admin panel at `/admin/`
2. Navigate to Products → Add Product
3. Fill in product details, upload images
4. Set category and pricing
5. Save and publish

### Customer Shopping Flow
1. Browse products by category
2. Use search and filters to find items
3. View detailed product information
4. Add items to shopping cart
5. Proceed through checkout process
6. Complete order with shipping details

## 🔮 Future Improvements

### Planned Features
- **Payment Integration**: Stripe, PayPal, and local payment gateways
- **Product Reviews**: Customer rating and review system
- **Advanced Analytics**: Sales reports and customer insights
- **Email Notifications**: Order confirmations and status updates
- **Inventory Alerts**: Low stock notifications for administrators
- **Multi-vendor Support**: Allow multiple sellers on the platform
- **Social Media Integration**: Share products on social platforms

### Technical Enhancements
- **API Development**: RESTful API using Django REST Framework
- **Caching**: Redis integration for improved performance
- **CDN Integration**: Faster static file delivery
- **Docker Support**: Containerized deployment
- **Automated Testing**: Comprehensive test suite
- **CI/CD Pipeline**: Automated deployment workflow

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Guidelines
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author & Contact

**Roni Ahamed**
- **GitHub**: [@roniahamed](https://github.com/roniahamed)
- **Profile**: Backend Developer | Python | Django | REST API | MySQL | PostgreSQL | Trainer | Competitive Programmer
- **LinkedIn**: [Connect with me](https://linkedin.com/in/roniahamed)
- **Email**: [Contact me](mailto:roniahamed@email.com)

## 🙏 Acknowledgments

- Django community for the excellent web framework
- Bootstrap team for the responsive UI components
- PythonAnywhere for reliable hosting services
- All contributors and users who have supported this project

## 📈 Project Stats

- **Created**: 2023 (2 years ago)
- **Language**: Python (Django)
- **Status**: Active and maintained
- **Deployment**: Live on PythonAnywhere

---

**⭐ If you found this project helpful, please give it a star on GitHub!**

*Built with ❤️ using Django and modern web technologies*