from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from typing import Any


from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from .database.models import ShipmentStatus
from .database.session import SessionDep
from .database_sql import Database
from FastAPI_with_SQLmodel.schemas import ShipmentCreate, ShipmentRead, ShipmentUpdate
from FastAPI_with_SQLmodel.database.session import create_db_and_tables


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan_handler)

db=Database()


@app.on_event("startup")
def startup() -> None:
    db.connect_to_db()
    db.create_table()


@app.on_event("shutdown")
def shutdown() -> None:
    db.close()


# shipments={
#     2203:{
#         "weight":14,
#         "content": "wooden_box",
#         "status": "in transit",
#         "destination": 11020
#     },
#     2204:{
#         "weight":6,
#         "content": "glassware",
#         "status": "placed",
#         "destination": 11021
#     },
#     2205:{
#         "weight":2,
#         "content":"frame",
#         "status":"delivered",
#         "destination": 11022
#         },
#     2206:{
#         "weight":5,
#         "content":"televisiom",
#         "status":"delivered",
#         "destination": 11023
#          }
# # }
# @app.get("/shipment/latest")
# def get_latest_shipment():
#     id=max(shipments.keys()) #Returning the id of the latest shipment
#     return shipments[id]

@app.get("/shipment",response_model=ShipmentRead)
def get_shipment(id: int,session: SessionDep) :#Not type hinting as it's already specified in the response_model parameter #->dict[str,str | int | float] #Type hinting so that the the function takes int as an input and also hinting that the output should be dict which have the key and value of datatype string or integer.
    session
    shipment=session.get(ShipmentRead,id)
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist"
        )
        
    return shipment
#Using Path and Query parameters together
# @app.get("/shipment/{field}")
# def get_shipment_field(field:str,id:int)-> dict[str,Any]:
#     return{
#         field:shipments[id][field]
#     }

# @app.get("/shipment/{id}")
# def get_shipment(id: int) -> dict[str,str | int | float]: #Type hinting so that the the function takes int as an input and also hinting that the output should be dict which have the key and value of datatype string or integer.
#     if not id:
#         id=max(shipments.keys())
#         return shipments[id]#giving back the latest request if no id is given
#     #without exception
#     # if id not in shipments:
#     #     return {"error": "shipment not found"}
#     if id not in shipments:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,#can also go like status_code=404
#             detail="shipment not found"
#         )
#     return shipments[id]

@app.get("/scalar",include_in_schema=False)#Making a custom documentation using openapi specification #include in schema to false will not show it in the documentation of scalar
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )

#Request Body Pameter
@app.post("/shipment")
def submit_shipment(shipment: ShipmentCreate, session: SessionDep)-> dict[str,Any]:
   new_shipment=ShipmentRead(
       **shipment.model_dump(),
       status=ShipmentStatus.placed,
       estimated_delivery=datetime.now() + timedelta(days=3)
   )
   session.add(new_shipment)#adding the new data into the db
   session.commit()#commiting the changes
   session.refresh(new_shipment)#need to refresh the db to get the id
   return {"id": new_shipment.id}







# Post method 
# @app.post("/shipment")
# def sumbit_shipment(shipment:ShipmentRead) -> dict[str,int]:
#     #Commented out cause we already have applied the condition using the Field in the schemas.py
#     # if shipment.weight>25:
#     #     raise HTTPException(
#     #         status_code=406,
#     #         detail="Maximum  weight limit is 25kg"
#     #     )
#     new_id=max(shipments.keys())+1
#     shipments[new_id]={
#         "content": shipment.content,
#         "weight": shipment.weight,
#         "status": "placed",
#     }

#Update the existing data,get new data from the client and replace the existing data from the dataframe
# @app.put("/shipment")
# def shipment_update(id:int,content:str,weight:float,status:str) -> dict[str,int]:
#     shipments[id]={
#         "content": content,
#         "weight": weight,
#         "status": status,
#     }
#     return shipments[id]
#Patch using request body
@app.patch("/shipment",response_model=ShipmentRead)
def patch_shipment(id: int, shipment_update:ShipmentUpdate,session: SessionDep):
    update=shipment_update.model_dump(exclude_unset=True)#the data for which we have to update our shipment
    if not update:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No data to update"
        )
    shipment=session.get(ShipmentRead,id)
    shipment.sqlmodel_update(update)#we can use this as it's already a sqlmodel
    session.add(shipment)#adding the updated values
    session.commit()#commiting the changes
    session.refresh(shipment)#refreshing to the updated values
    return shipment



#Normal patch code
# @app.patch("/shipment")
# def patch_shipment(id:int,content:str | None=None,weight:float | None=None,status:str | None=None):
#     shipment=shipments[id]
#     #Update the provided fields that are not None
#     if content:
#         shipment["content"]=content
#     if weight:
#         shipment["weight"]=weight
#     if status:
#         shipment["status"]=status
#     shipments[id]=shipment
#     return shipment

#Delelting a shipment
@app.delete("/shipment")
def delete_shipment(id:int , session: SessionDep)-> dict[str,str]:
    session.delete(
        session.get(ShipmentRead,id)
    )
    session.commit()
    return{"detail": f"ShipmentRead with the id {id} has been deleted"}

