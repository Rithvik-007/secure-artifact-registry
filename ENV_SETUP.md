# Environment Variables Setup

This project uses environment variables for configuration. Create a `.env` file in the appropriate directory to customize settings.

## Backend Setup

Create a `.env` file in the `backend/` directory with the following variables:

```env
# Database Configuration
DATABASE_URL=sqlite:///./artifact.db

# JWT Authentication
# REQUIRED: Generate a secure secret key: python -c "import secrets; print(secrets.token_hex(32))"
SECRET_KEY=<your-generated-secret-key-here>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS Configuration (comma-separated for multiple origins)
CORS_ORIGINS=http://localhost:5173,http://localhost:3000

# File Storage
STORAGE_BASE_PATH=storage
```

### Notes:
- `SECRET_KEY`: **REQUIRED** - The application will fail to start without this. Generate a secure key using:
  ```bash
  python -c "import secrets; print(secrets.token_hex(32))"
  ```
  The `.env` file is automatically loaded from the `backend/` directory regardless of where you run the app from.
- `CORS_ORIGINS`: Comma-separated list of allowed origins for CORS
- `DATABASE_URL`: SQLite by default, but can be changed to PostgreSQL, MySQL, etc.
- `STORAGE_BASE_PATH`: Base directory for storing uploaded files

## Frontend Setup

Create a `.env` file in the `frontend/` directory with:

```env
# Backend API URL
VITE_API_URL=http://127.0.0.1:8000
```

### Notes:
- `VITE_API_URL`: The base URL of your backend API
- Vite requires the `VITE_` prefix for environment variables to be exposed to the client
- Defaults to `http://127.0.0.1:8000` if not set

## Default Values

If you don't create a `.env` file:
- **Backend**: `SECRET_KEY` is **REQUIRED** - the application will fail to start without it. Other values have sensible defaults.
- **Frontend**: Uses `http://127.0.0.1:8000` as the API URL if `VITE_API_URL` is not set.

## Production Considerations

1. **Never commit `.env` files** - they should be in `.gitignore`
2. **Use strong SECRET_KEY** in production
3. **Set appropriate CORS_ORIGINS** for your domain
4. **Use a production database** (PostgreSQL, MySQL, etc.)
5. **Configure proper file storage** (S3, Azure Blob, etc.)

