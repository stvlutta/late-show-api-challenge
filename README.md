# 🌙 Flask Code Challenge — Late Show API

A Flask REST API for a Late Night TV show system built with PostgreSQL, JWT authentication, and MVC architecture.

## 🚀 Features

- ✅ **MVC Architecture** - Clean separation of concerns
- ✅ **PostgreSQL Database** - Robust data persistence
- ✅ **JWT Authentication** - Token-based security
- ✅ **RESTful API** - Standard HTTP methods and status codes
- ✅ **Data Validation** - Input validation and error handling
- ✅ **Cascade Deletes** - Automatic cleanup of related data

## 📁 Project Structure

```
.
├── server/
│   ├── app.py                 # Flask application factory
│   ├── config.py              # Configuration settings
│   ├── seed.py                # Database seeding script
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py            # User model with auth
│   │   ├── guest.py           # Guest model
│   │   ├── episode.py         # Episode model
│   │   └── appearance.py      # Appearance model with validation
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── auth_controller.py # Registration & login
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   └── appearance_controller.py
├── migrations/                # Database migration files
├── challenge-4-lateshow.postman_collection.json
├── .gitignore
└── README.md
```

## 🛠 Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL 12+

### 1. Clone Repository
```bash
git clone https://github.com/<username>/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. Install Dependencies
```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```

### 3. PostgreSQL Setup
Create your database in PostgreSQL:
```sql
CREATE DATABASE late_show_db;
```

### 4. Environment Variables
Set your database connection in `server/config.py` or use environment variables:
```bash
export DATABASE_URL="postgresql://username:password@localhost:5432/late_show_db"
export JWT_SECRET_KEY="your-secret-key-here"
```

### 5. Database Migration & Seeding
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

### 6. Run the Application
```bash
python server/app.py
```

The API will be available at `http://localhost:5000`

## 🔐 Authentication Flow

### 1. Register a User
```http
POST /register
Content-Type: application/json

{
  "username": "testuser",
  "password": "password123"
}
```

### 2. Login to Get JWT Token
```http
POST /login
Content-Type: application/json

{
  "username": "testuser",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "user": {
    "id": 1,
    "username": "testuser"
  }
}
```

### 3. Use Token in Protected Requests
```http
Authorization: Bearer <your-jwt-token>
```

## 🛠 API Routes

| Route | Method | Auth Required? | Description |
|-------|--------|----------------|-------------|
| `/register` | POST | ❌ | Register a new user |
| `/login` | POST | ❌ | Login and get JWT token |
| `/episodes` | GET | ❌ | List all episodes |
| `/episodes/<int:id>` | GET | ❌ | Get episode with appearances |
| `/episodes/<int:id>` | DELETE | ✅ | Delete episode + appearances |
| `/guests` | GET | ❌ | List all guests |
| `/appearances` | POST | ✅ | Create new appearance |

## 📖 API Examples

### Get All Episodes
```http
GET /episodes
```

**Response:**
```json
[
  {
    "id": 1,
    "date": "2024-01-15",
    "number": 101
  },
  {
    "id": 2,
    "date": "2024-01-16",
    "number": 102
  }
]
```

### Get Episode with Appearances
```http
GET /episodes/1
```

**Response:**
```json
{
  "id": 1,
  "date": "2024-01-15",
  "number": 101,
  "appearances": [
    {
      "id": 1,
      "rating": 5,
      "guest_id": 1,
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Jennifer Lawrence",
        "occupation": "Actress"
      }
    }
  ]
}
```

### Create Appearance (Protected)
```http
POST /appearances
Authorization: Bearer <token>
Content-Type: application/json

{
  "rating": 4,
  "guest_id": 1,
  "episode_id": 2
}
```

**Response:**
```json
{
  "id": 7,
  "rating": 4,
  "guest_id": 1,
  "episode_id": 2,
  "guest": {
    "id": 1,
    "name": "Jennifer Lawrence",
    "occupation": "Actress"
  },
  "episode": {
    "id": 2,
    "date": "2024-01-16",
    "number": 102
  }
}
```

## 🧪 Testing with Postman

1. **Import Collection**: Import `challenge-4-lateshow.postman_collection.json` into Postman
2. **Set Base URL**: The collection uses `{{base_url}}` variable set to `http://localhost:5000`
3. **Authentication Flow**:
   - Run "Register User" to create an account
   - Run "Login User" to get JWT token (automatically saved to collection variable)
   - The token is automatically used in protected routes

### Collection Features
- **Auto-token management**: Login automatically saves JWT token
- **Environment variables**: Base URL configured as collection variable
- **Protected routes**: Automatically include Bearer token
- **Sample data**: Pre-filled request bodies

## 📊 Database Models

### User
- `id` (Primary Key)
- `username` (Unique)
- `password_hash` (Encrypted)

### Guest
- `id` (Primary Key)
- `name`
- `occupation`

### Episode
- `id` (Primary Key)
- `date`
- `number` (Unique)

### Appearance
- `id` (Primary Key)
- `rating` (1-5 validation)
- `guest_id` (Foreign Key)
- `episode_id` (Foreign Key)

## 🔒 Security Features

- **Password Hashing**: Uses Werkzeug's secure password hashing
- **JWT Tokens**: Stateless authentication with Flask-JWT-Extended
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection
- **Error Handling**: Secure error messages without sensitive data exposure

## 🚨 Error Handling

The API returns appropriate HTTP status codes and JSON error messages:

```json
{
  "error": "Username already exists"
}
```

Common status codes:
- `200` - Success
- `201` - Created
- `400` - Bad Request (validation errors)
- `401` - Unauthorized (invalid credentials/token)
- `404` - Not Found
- `500` - Internal Server Error

## 🌐 GitHub Repository

[https://github.com/<username>/late-show-api-challenge](https://github.com/<username>/late-show-api-challenge)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.