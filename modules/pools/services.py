from sqlalchemy.orm import Session
from fastapi import HTTPException
from modules.pools.models import Pool
from modules.pools.error_codes import PoolErrorCodes
from modules.pools.validators import PoolValidator
from modules.pools.utils import get_current_utc_time

# Add a new pool
def add_pool(db: Session, pool_name: str, blockchain: str) -> Pool:
    if db.query(Pool).filter(Pool.pool_name == pool_name, Pool.blockchain == blockchain).first():
        raise HTTPException(status_code=400, detail=PoolErrorCodes.POOL_ALREADY_EXISTS)

    validated_data = PoolValidator(pool_name=pool_name, blockchain=blockchain).dict()

    new_pool = Pool(
        pool_name=validated_data["pool_name"],
        blockchain=validated_data["blockchain"],
        created_at=get_current_utc_time(),
        updated_at=get_current_utc_time()
    )
    
    db.add(new_pool)
    db.commit()
    db.refresh(new_pool)
    return new_pool

# Get all pools
def get_all_pools(db: Session):
    return db.query(Pool).all()

# Remove a pool by ID
def remove_pool(db: Session, pool_id: int) -> bool:
    pool = db.query(Pool).filter(Pool.id == pool_id).first()
    if not pool:
        raise HTTPException(status_code=404, detail=PoolErrorCodes.POOL_NOT_FOUND)

    db.delete(pool)
    db.commit()
    return True
