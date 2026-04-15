from fastapi import FastAPI,status,HTTPException
from scalar_fastapi import get_scalar_api_reference
from typing import Any
from pydantic import BaseModel

class Shipment(BaseModel):
    content:str
    weight:float
    destination:int

app = FastAPI()

shipments={
    2203:{
        "weight":123.12,
        "content": "wooden_box",
        "status": "in transit",
    },
    2204:{
        "weight":63.12,
        "content": "glassware",
        "status": "placed",
    },
    2205:{
        "weight":213.56,
        "content":"frame",
        "status":"delivered",
    },
    2206:{
        "weight":582.5,
        "content":"televisiom",
        "status":"delivered",
    }
}
@app.get("/shipment/latest")
def get_latest_shipment():
    id=max(shipments.keys()) #Returning the id of the latest shipment
    return shipments[id]

@app.get("/shipment/{id}")
def get_shipment(id: int) -> dict[str,str | int | float]: #Type hinting so that the the function takes int as an input and also hinting that the output should be dict which have the key and value of datatype string or integer.
    if not id:
        id=max(shipments.keys())
        return shipments[id]#giving back the latest request if no id is given
    #without exception
    # if id not in shipments:
    #     return {"error": "shipment not found"}
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,#can also go like status_code=404
            detail="shipment not found"
        )
    return shipments[id]
#Using Path and Query parameters together
@app.get("/shipment/{field}")
def get_shipment_field(field:str,id:int)-> dict[str,Any]:
    return{
        field:shipments[id][field]
    }

@app.get("/shipment/{id}")
def get_shipment(id: int) -> dict[str,str | int | float]: #Type hinting so that the the function takes int as an input and also hinting that the output should be dict which have the key and value of datatype string or integer.
    if not id:
        id=max(shipments.keys())
        return shipments[id]#giving back the latest request if no id is given
    #without exception
    # if id not in shipments:
    #     return {"error": "shipment not found"}
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,#can also go like status_code=404
            detail="shipment not found"
        )
    return shipments[id]

@app.get("/scalar",include_in_schema=False)#Making a custom documentation using openapi specification #include in schema to false will not show it in the documentation of scalar
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )

#Request Body Pameter
# @app.post("/shipment")
# def submit_shipment(data: dict[str,Any])-> dict[str,Any]:
#     content=data["content"]
#     weight=data["weight"]
#     if weight>25:
#         raise HTTPException(
#             status_code=406,
#             detail="Maximum  weight limit is 25kg"
#         )
#     new_id=max(shipments.keys())+1
#     shipments[new_id]={
#         "content": content,
#         "weight": weight,
#         "status": "placed",
#     }
#     return {"id": new_id}



# Post method 
@app.post("/shipment")
def sumbit_shipment(shipment:Shipment) -> dict[str,int]:
    if shipment.weight>25:
        raise HTTPException(
            status_code=406,
            detail="Maximum  weight limit is 25kg"
        )
    new_id=max(shipments.keys())+1
    shipments[new_id]={
        "content": shipment.content,
        "weight": shipment.weight,
        "status": "placed",
    }

    return {"id": new_id}
#Update the existing data,get new data from the client and replace the existing data from the dataframe
@app.put("/shipment")
def shipment_update(id:int,content:str,weight:float,status:str) -> dict[str,Any]:
    shipments[id]={
        "content": content,
        "weight": weight,
        "status": status,
    }
    return shipments[id]
#Patch using request body
@app.patch("/shipment")
def patch_shipment(id:int,body:dict[str,Any]):
    shipment=shipments[id]
    #Update the provided fields that are not None
    shipment.update(body)
    shipments[id]=shipment
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
def delete_shipment(id:int)-> dict[str,str]:
    shipments.pop(id)
    return{"detail": f"Shipment with the id #{id} has been deleted"}