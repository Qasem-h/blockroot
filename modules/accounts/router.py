from fastapi import APIRouter

router = APIRouter()

@router.get("/account_info")
async def get_account_info():
    return {"message": "This is account info."}
