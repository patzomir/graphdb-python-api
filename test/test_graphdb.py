jsonld_string1 = '{ \
  "@context" : { \
    "@base" : "http://ontology.roche.com/", \
    "@vocab" : "http://ontology.roche.com/model/rts/core/", \
    "id" : "@id", \
    "type" : "@type", \
    "literalForm" : "http://www.w3.org/2008/05/skos-xl#literalForm", \
    "modified" : { \
      "@id" : "http://purl.org/dc/terms/modified", \
      "@type" : "http://www.w3.org/2001/XMLSchema#dateTime" \
    }, \
    "broader" : { \
      "@id" : "http://www.w3.org/2004/02/skos/core#broader", \
      "@type" : "@id", \
      "@container" : "@set" \
    }, \
    "prefLabelXl" : "http://www.w3.org/2008/05/skos-xl#prefLabel", \
    "prefLabel" : "http://www.w3.org/2004/02/skos/core#prefLabel", \
    "altLabelXl" : { \
      "@id" : "http://www.w3.org/2008/05/skos-xl#altLabel", \
      "@container" : "@set" \
    }, \
    "hiddenLabelXl" : { \
      "@id" : "http://www.w3.org/2008/05/skos-xl#hiddenLabel", \
      "@container" : "@set" \
    }, \
    "labelTypeConcept" : { \
      "@id" : "http://ontology.roche.com/model/rts/core/labelTypeConcept", \
      "@container" : "@set" \
    }, \
    "sourceConcept" : { \
      "@id" : "http://ontology.roche.com/model/rts/core/sourceConcept", \
      "@container" : "@set" \
    }, \
    "definition" : "http://www.w3.org/2004/02/skos/core#definition", \
    "comment" : "http://www.w3.org/2004/02/skos/core#editorialNote", \
    "topConceptOf" : { \
      "@id" : "http://www.w3.org/2004/02/skos/core#topConceptOf", \
      "@type" : "@id" \
    }, \
    "Concept" : "http://www.w3.org/2004/02/skos/core#Concept" \
  }, \
  "@graph" : [ { \
    "id" : "ROX1308059566478", \
    "type" : "Concept", \
    "prefLabelXl" : { \
      "literalForm" : "Astrocyte" \
    } \
  }, { \
    "id" : "ROX37924416443868120", \
    "type" : "Concept", \
    "prefLabelXl" : { \
      "literalForm" : "Amacrine cell" \
    } \
  }, { \
    "id" : "ROX38018592443943878", \
    "type" : "Concept", \
    "prefLabelXl" : { \
      "literalForm" : "Basket cell" \
    } \
  }, { \
    "id" : "ROX38019456443943988", \
    "type" : "Concept", \
    "prefLabelXl" : { \
      "literalForm" : "Acinar cell" \
    } \
  }, { \
    "id" : "ROX38019456443944008", \
    "type" : "Concept", \
    "prefLabelXl" : { \
      "literalForm" : "Basal cell" \
    } \
  } ] \
}'

jsonld_string2 = '{ \
  "@context" : { \
    "@base" : "http://ontology.roche.com/", \
    "@vocab" : "http://ontology.roche.com/model/rts/core/", \
    "id" : "@id", \
    "type" : "@type", \
    "literalForm" : "http://www.w3.org/2008/05/skos-xl#literalForm", \
    "modified" : { \
      "@id" : "http://purl.org/dc/terms/modified", \
      "@type" : "http://www.w3.org/2001/XMLSchema#dateTime" \
    }, \
    "broader" : { \
      "@id" : "http://www.w3.org/2004/02/skos/core#broader", \
      "@type" : "@id", \
      "@container" : "@set" \
    }, \
    "prefLabelXl" : "http://www.w3.org/2008/05/skos-xl#prefLabel", \
    "prefLabel" : "http://www.w3.org/2004/02/skos/core#prefLabel", \
    "altLabelXl" : { \
      "@id" : "http://www.w3.org/2008/05/skos-xl#altLabel", \
      "@container" : "@set" \
    }, \
    "hiddenLabelXl" : { \
      "@id" : "http://www.w3.org/2008/05/skos-xl#hiddenLabel", \
      "@container" : "@set" \
    }, \
    "labelTypeConcept" : { \
      "@id" : "http://ontology.roche.com/model/rts/core/labelTypeConcept", \
      "@container" : "@set" \
    }, \
    "sourceConcept" : { \
      "@id" : "http://ontology.roche.com/model/rts/core/sourceConcept", \
      "@container" : "@set" \
    }, \
    "definition" : "http://www.w3.org/2004/02/skos/core#definition", \
    "comment" : "http://www.w3.org/2004/02/skos/core#editorialNote", \
    "topConceptOf" : { \
      "@id" : "http://www.w3.org/2004/02/skos/core#topConceptOf", \
      "@type" : "@id" \
    }, \
    "Concept" : "http://www.w3.org/2004/02/skos/core#Concept" \
  }, \
  "@graph" : [ { \
    "id" : "ROX1308059566227", \
    "type" : "Concept", \
    "prefLabelXl" : { \
      "literalForm" : "Basophil" \
    } \
  }, { \
    "id" : "ROX1308488055155", \
    "type" : "Concept", \
    "prefLabelXl" : { \
      "literalForm" : "Bone cell" \
    } \
  }, { \
    "id" : "ROX37511424443804145", \
    "type" : "Concept", \
    "prefLabelXl" : { \
      "literalForm" : "Bladder urothelial cell" \
    } \
  }, { \
    "id" : "ROX37934784443869806", \
    "type" : "Concept", \
    "prefLabelXl" : { \
      "literalForm" : "Bipolar neuron" \
    } \
  }, { \
    "id" : "ROX38019456443944004", \
    "type" : "Concept", \
    "prefLabelXl" : { \
      "literalForm" : "Bergmann glial cell" \
    } \
  } ] \
}'


bnode_test1 = "<http://example.com> <http://example.com> [ <http://example.com> '1' ;]."
bnode_test2 = "<http://example.com> <http://example.com> [ <http://example.com> '2' ;]."


if __name__ == "__main__":
    graphdb = "http://localhost:7200/repositories/bnode"
    graph = "http://example-transaction"
    triples1 = [
        '<http://example1> <http://example1>  "keep" <{}> .'.format(graph),
        '<http://example1> <http://example1>  "delete" <{}> .'.format(graph)
    ]
    triples2 = [
        '<http://example1> <http://example1>  "keep" <{}> .'.format(graph),
        '<http://example1> <http://example1>  "add" <{}> .'.format(graph)
    ]
    jsonld1 = json.loads(jsonld_string1)
    jsonld1["@id"] = graph
    jsonld2 = json.loads(jsonld_string2)
    jsonld2["@id"] = graph

    jsonlds1 = [
        json.dumps(jsonld1),
        json.dumps(jsonld2)
    ]
    jsonlds2 = [json.dumps(jsonld1)]
    #overwrite_graph_example(graphdb, graph, triples1, "text/x-nquads")
    #overwrite_graph_example(graphdb, graph, triples2, "text/x-nquads")
    with open("/home/patzo/Downloads/example1.jsonld") as f:
    	t1 = f.read()
    with open("/home/patzo/Downloads/example2.jsonld") as f:
    	t2 = f.read()
    # BNODE TEST
    # overwrite_graph_example(graphdb, graph, [t1, t2], "application/ld+json")
    overwrite_graph_example(graphdb, graph, [bnode_test1, bnode_test2], "text/turtle")


    #overwrite_graph_example(graphdb, graph, jsonlds1, "application/ld+json")
    #overwrite_graph_example(graphdb, graph, jsonlds2, "application/ld+json")