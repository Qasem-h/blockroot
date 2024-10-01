from fastapi import FastAPI
from core.settings import settings
from core.logging import init_logging
from core.middleware import RequestLoggerMiddleware
import uvicorn
from modules.accounts.router import router as accounts_router
from modules.wallets.router import router as wallets_router
from modules.alerts.router import router as alerts_router
from modules.subscription.router import router as subscription_router

# Initialize logging
init_logging(settings.log_level)

app = FastAPI()

# Add middleware
app.add_middleware(RequestLoggerMiddleware)

# Include routers
app.include_router(accounts_router, prefix="/accounts")
app.include_router(wallets_router, prefix="/wallets")
app.include_router(alerts_router, prefix="/alerts")
app.include_router(subscription_router, prefix="/subscription")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
