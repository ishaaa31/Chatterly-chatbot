from neo4j import GraphDatabase

uri = "neo4j+s://a773e76a.databases.neo4j.io"  
username = "neo4j"
password = "aouXi2KOAtWlqgAQKcS7nrGmyWh_MEbgtcvTqLnbWcY"  

driver = GraphDatabase.driver(uri, auth=(username, password))

def store_fact(subject, relation, obj):
    with driver.session() as session:
        session.run("""
            MERGE (s:Entity {name: $subject})
            MERGE (o:Entity {name: $object})
            MERGE (s)-[:RELATION {type: $relation}]->(o)
        """, subject=subject, relation=relation, object=obj)

def query_facts(limit=10):
    with driver.session() as session:
        result = session.run("""
            MATCH (s)-[r]->(o)
            RETURN s.name AS subject, r.type AS relation, o.name AS object
            LIMIT $limit
        """, limit=limit)
        return [(record["subject"], record["relation"], record["object"]) for record in result]
