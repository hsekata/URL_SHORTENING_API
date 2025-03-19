# URL Shortener API

## Overview
This is a simple Django-based URL shortener API that allows users to:
- Shorten a given URL
- Retrieve the original URL using the shortened code
- Update or delete a shortened URL entry
- Retrieve statistics about a shortened URL

## Technologies Used
- **Django** (Backend framework)
- **Django REST Framework (DRF)** (API development)


---

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/URL_SHORTENING_API.git
cd url-shortener
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
python manage.py migrate
```

### 5. Run the Server
```sh
python manage.py runserver
```

The API will be accessible at: **http://127.0.0.1:8000/**

---

## API Endpoints

### 1. Shorten a URL
**Endpoint:**
```http
POST /shorten
```
**Request Body:**
```json
{
    "url": "https://example.com"
}
```
**Response:**
```json
{
    "url": "https://example.com",
    "shortcode": "aB12xZ",
    "createdAt": "2025-03-19T12:00:00Z",
    "updatedAt": "2025-03-19T12:00:00Z"
}
```

### 2. Retrieve, Update, or Delete a Shortened URL
**Endpoint:**
```http
GET /shorten/{shortcode}
PUT /shorten/{shortcode}
DELETE /shorten/{shortcode}
```
**GET Response:**
```json
{
    "url": "https://example.com",
    "shortcode": "aB12xZ",
    "createdAt": "2025-03-19T12:00:00Z",
    "updatedAt": "2025-03-19T12:00:00Z"
}
```

**PUT Request Body (to update URL):**
```json
{
    "url": "https://new-example.com"
}
```
**PUT Response:**
```json
{
    "url": "https://new-example.com",
    "shortcode": "aB12xZ",
    "createdAt": "2025-03-19T12:00:00Z",
    "updatedAt": "2025-03-19T13:00:00Z"
}
```

### 3. Retrieve Short URL Statistics
**Endpoint:**
```http
GET /shorten/{shortcode}/stat
```
**Response:**
```json
{
    "url": "https://example.com",
    "shortcode": "aB12xZ",
    "createdAt": "2025-03-19T12:00:00Z",
    "updatedAt": "2025-03-19T12:00:00Z",
    "accessCount": 10
}
```

---

## Database Model
### `URL` Model Fields:
| Field         | Type         | Description |
|--------------|-------------|-------------|
| `url`        | CharField   | The original long URL |
| `shortcode`  | CharField   | Unique short code for the URL |
| `createdAt`  | TimeField   | Timestamp when the short URL was created |
| `updatedAt`  | TimeField   | Timestamp when the short URL was last updated |
| `accessCount`| IntegerField| Number of times the short URL was accessed |

