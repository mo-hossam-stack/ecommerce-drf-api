# Django E-commerce API

## Project Overview
This Django project is a backend API for an e-commerce application. It provides endpoints for managing products, categories, cart items, reviews, user authentication, orders, and payment integration using Stripe.

## Features
- User authentication and management
- Product and category listing
- Cart functionality (add, update, delete items)
- Wishlist functionality (add, delete, check existence)
- Product search
- Order processing with Stripe checkout

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd project_directory
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables in `.env`:
   ```sh
   STRIPE_SECRET_KEY=your_stripe_secret_key
   WEBHOOK_SECRET=your_webhook_secret
   ```
5. Apply migrations and run the development server:
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

## API Endpoints

### Product Endpoints

#### Get all products
**Endpoint:** `GET /product_list`

- **Response:**
  - Returns a list of all products.

---

#### Get Product Details
**Endpoint:** `GET /products/<slug:slug>`

- **Parameters:**
  - `slug`: The unique identifier for a product.
- **Response:**
  - JSON object containing product details.

---

#### Get All Categories
**Endpoint:** `GET /category_list`

- **Response:**
  - Returns a list of all product categories.

---

#### Get Category Details
**Endpoint:** `GET /category/<slug:slug>`

- **Response:**
  - JSON object containing category details.