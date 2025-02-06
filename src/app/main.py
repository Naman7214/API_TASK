import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings
from config.database import get_database
from controllers import (
    auth_controller,
    user_controller,
    admin_controller,
    product_controller,
    cart_controller,
    order_controller,
    complaint_controller,
    file_controller,
)

# Initialize FastAPI app
app = FastAPI(
    title="E-Commerce API",
    description="FastAPI-based E-Commerce Application with MongoDB, GCP, and JWT Auth",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Connection
@app.on_event("startup")
async def startup_db():
    """Connect to MongoDB on app startup"""
    app.mongodb_client = AsyncIOMotorClient(settings.MONGO_URI)
    app.mongodb = app.mongodb_client[settings.MONGO_DB]

@app.on_event("shutdown")
async def shutdown_db():
    """Close MongoDB connection on app shutdown"""
    app.mongodb_client.close()

# Include Controllers (Routes)
app.include_router(auth_controller.router,tags=["Auth"])
app.include_router(user_controller.router, tags=["Users"])
app.include_router(admin_controller.router,tags=["Admin"])
app.include_router(product_controller.router,  tags=["Products"])
app.include_router(cart_controller.router, tags=["Cart"])
app.include_router(order_controller.router, tags=["Orders"])
app.include_router(complaint_controller.router, tags=["Complaints"])
app.include_router(file_controller.router, tags=["File Uploads"])

# Run FastAPI Server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
