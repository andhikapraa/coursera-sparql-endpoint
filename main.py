from fastapi import FastAPI
from rdflib import ConjunctiveGraph
from rdflib_endpoint import SparqlRouter

g = ConjunctiveGraph()
g.parse("coursera_csv.ttl", format="turtle")

sparql_router = SparqlRouter(
    graph=g,
    path="/sparql",
    title="Coursera Free Courses",
    description="A simple SPARQL endpoint for Coursera Free Courses",
    version="0.0.1",
)

app = FastAPI()
app.include_router(sparql_router)

# to run the server
# uvicorn main:app --reload