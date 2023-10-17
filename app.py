from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Clase modelo Pydantic para un dinosaurio
class Dinosaurio(BaseModel):
    id: int
    nombre: str
    imagen: str

# Lista de dinosaurios
dinosaurios = [
    Dinosaurio(id=1, nombre="Tyrannosaurus Rex", imagen="https://th.bing.com/th/id/OIP.AcumA5Rr8jYidcmec3mSGgHaF0?w=220&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"),
    Dinosaurio(id=2, nombre="Velociraptor", imagen="https://th.bing.com/th/id/OIP.GCiYNzZDrb5mMn-_CONghgHaDS?w=289&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"),
    Dinosaurio(id=3, nombre="Triceratops", imagen="https://th.bing.com/th/id/OIP.m6qR9fgJgiBNwegeBec7rQHaC3?w=315&h=135&c=7&r=0&o=5&dpr=1.5&pid=1.7"),
    Dinosaurio(id=4, nombre="Brachiosaurus", imagen="https://www.wildrepublic.com/wp-content/uploads/2018/07/Brachiosaurus-3025-xl.jpg"),
    Dinosaurio(id=5, nombre="Stegosaurus", imagen="https://vignette1.wikia.nocookie.net/dino/images/4/4c/Stegosaurus-detail-header.png/revision/latest?cb=20150407211604"),
    Dinosaurio(id=6, nombre="Pteranodon", imagen="https://th.bing.com/th/id/OIP.efV4QTNt6H6VURvLFJ1y_QHaEA?w=294&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"),
    Dinosaurio(id=7, nombre="Allosaurus", imagen="https://th.bing.com/th/id/OIP.TKaUr9E_PweRrgje08inGgHaDZ?w=320&h=160&c=7&r=0&o=5&dpr=1.5&pid=1.7"),
    Dinosaurio(id=8, nombre="Spinosaurus", imagen="https://th.bing.com/th/id/OIP.YK2kLs776LKoDczbnX9FnQHaEF?w=272&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"),
    Dinosaurio(id=9, nombre="Ankylosaurus", imagen="https://th.bing.com/th/id/OIP.0wcZ7-7qEo0d8KOGEB4vDwHaFj?w=212&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"),
    Dinosaurio(id=10, nombre="Parasaurolophus", imagen="https://th.bing.com/th/id/OIP._o4KnILXd9VZlkcqGchF1wHaFM?w=234&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7"),
]

# Obtener todos los dinosaurios
@app.get("/dinosaurios/", response_model=List[Dinosaurio])
async def read_dinosaurios():
    return dinosaurios

# Obtener un dinosaurio por su ID
@app.get("/dinosaurios/{dinosaurio_id}", response_model=Dinosaurio)
async def read_dinosaurio(dinosaurio_id: int):
    dinosaurio = next((d for d in dinosaurios if d.id == dinosaurio_id), None)
    if dinosaurio is None:
        raise HTTPException(status_code=404, detail="Dinosaurio no encontrado")
    return dinosaurio

# Agregar un nuevo dinosaurio
@app.post("/dinosaurios/", response_model=Dinosaurio)
async def create_dinosaurio(dinosaurio: Dinosaurio):
    dinosaurios.append(dinosaurio)
    return dinosaurio

# Actualizar un dinosaurio por su ID
@app.put("/dinosaurios/{dinosaurio_id}", response_model=Dinosaurio)
async def update_dinosaurio(dinosaurio_id: int, dinosaurio: Dinosaurio):
    index = next((i for i, d in enumerate(dinosaurios) if d.id == dinosaurio_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Dinosaurio no encontrado")
    dinosaurios[index] = dinosaurio
    return dinosaurio

# Eliminar un dinosaurio por su ID
@app.delete("/dinosaurios/{dinosaurio_id}", response_model=Dinosaurio)
async def delete_dinosaurio(dinosaurio_id: int):
    index = next((i for i, d in enumerate(dinosaurios) if d.id == dinosaurio_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Dinosaurio no encontrado")
    deleted_dinosaurio = dinosaurios.pop(index)
    return deleted_dinosaurio

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=22)
