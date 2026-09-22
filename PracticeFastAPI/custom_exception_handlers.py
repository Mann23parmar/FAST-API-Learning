from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


class OutOfStockError(Exception):
    def __init__(self, product_name: str):
        self.product_name = product_name


@app.exception_handler(OutOfStockError)
async def out_of_stock_handler(
    request: Request,
    exception: OutOfStockError,
):
    return JSONResponse(
        status_code=400,
        content={
            "message": f"{exception.product_name} is out of stock",
        },
    )


@app.get("/products/{product_name}")
def get_product(product_name: str):
    if product_name.lower() == "laptop":
        raise OutOfStockError(product_name)
    return {"product": product_name, "available": True}
