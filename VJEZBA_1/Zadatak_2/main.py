import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from kmeans import kmeans

MIN_CLUSTERS = 2
MAX_CLUSTERS = 10
MAX_POINTS = 1000

app = FastAPI(title="K-means API")

origins = [os.environ["FRONTEND_ORIGIN"]]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class Point(BaseModel):
    x: float = Field(ge=0, le=800)
    y: float = Field(ge=0, le=500)


class ClusterRequest(BaseModel):
    k: int = Field(ge=MIN_CLUSTERS, le=MAX_CLUSTERS)
    points: list[Point] = Field(min_length=MIN_CLUSTERS, max_length=MAX_POINTS)


@app.get("/")
def health():
    return {"status": "ok"}


@app.get("/api/config")
def get_config():
    return {
        "min_clusters": MIN_CLUSTERS,
        "max_clusters": MAX_CLUSTERS,
        "max_points": MAX_POINTS,
    }


@app.post("/api/cluster")
def cluster_points(request: ClusterRequest):
    points = []
    for point in request.points:
        points.append((point.x, point.y))

    if len(set(points)) < request.k:
        raise HTTPException(
            status_code=422,
            detail="Broj različitih točaka mora biti barem jednak broju grupa.",
        )

    labels, centers = kmeans(points, request.k)

    return {
        "labels": labels,
        "centers": [{"x": x, "y": y} for x, y in centers],
    }