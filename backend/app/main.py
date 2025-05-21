import os
import datetime
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from apis.llm import router as llm_router
from core.logging import setup_logging
from config import API_PREFIX, API_VERSION

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\raman\AI-code-reviewer\\backend\zbala-owner.json"

# Set up logging
logger = setup_logging()

# Initialize the FastAPI app
app = FastAPI(
    title="AI Code reviewer",
    description="AI Code reviewer API",
    version=API_VERSION,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routers
app.include_router(llm_router, prefix=API_PREFIX)

@app.get("/")
async def root():
    """API root endpoint - redirects to documentation"""
    return {"message": "AI Code reviewer", "docs_url": "/docs"}

@app.get("/health")
async def health_check():
    """API health check endpoint"""
    logger.debug("Health check endpoint called")
    
    health_status = {
        "status": "healthy",
        "version": API_VERSION,
        "timestamp": datetime.datetime.now().isoformat(),
        "services": {
            "gemini": "available"
        }
    }
    
    logger.info(f"Health check: {health_status['status']}")
    return health_status