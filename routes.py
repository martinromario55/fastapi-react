from fastapi import APIRouter, status, HTTPException


from models import (supplier_pydantic, supplier_pydanticIn, Supplier)



router = APIRouter()

# Create Supplier
@router.post("/supplier", status_code=status.HTTP_201_CREATED)
async def create_supplier(supplier_info: supplier_pydanticIn):
    try:
        supplier_obj = await Supplier.create(**supplier_info.dict(exclude_unset=True))
        response = await supplier_pydantic.from_tortoise_orm(supplier_obj)
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        