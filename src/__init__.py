"""Top-level package for milky2onebot."""

from gateway import app
import uvicorn


if __name__ == "__main__":
    uvicorn.run(app)
