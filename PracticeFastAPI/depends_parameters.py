from fastapi import Depends, FastAPI

app = FastAPI()


def require_role(role: str):
    def check_role():
        return {"role": role, "message": f"User has the {role} role"}

    return check_role


@app.get("/admin")
def admin_page(user=Depends(require_role("admin"))):
    return {"page": "Admin page", "user": user}
