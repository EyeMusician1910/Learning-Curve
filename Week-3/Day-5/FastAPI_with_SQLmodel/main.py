from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, status

try:
    from scalar_fastapi import get_scalar_api_reference
except ModuleNotFoundError:
    get_scalar_api_reference = None

from .api.route import master_router
from .database.session import create_db_and_tables


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan_handler)
app.include_router(master_router)


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    if get_scalar_api_reference is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Scalar docs support is not installed. Install it with: pip install scalar-fastapi",
        )

    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
