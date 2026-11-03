CREATE TABLE atlas_rag_collections (
  collection_id VARCHAR2(64) PRIMARY KEY,
  model_id VARCHAR2(255) NOT NULL,
  embed_endpoint VARCHAR2(512) NOT NULL,
  dimensions NUMBER NOT NULL,
  chunk_version VARCHAR2(64) NOT NULL
);
CREATE TABLE atlas_rag_documents (
  collection_id VARCHAR2(64) NOT NULL,
  doc_id VARCHAR2(64) NOT NULL,
  source_ref VARCHAR2(4000) NOT NULL,
  source_version VARCHAR2(255) NOT NULL,
  PRIMARY KEY (collection_id, doc_id),
  FOREIGN KEY (collection_id) REFERENCES atlas_rag_collections(collection_id) ON DELETE CASCADE
);
CREATE TABLE atlas_rag_chunks (
  collection_id VARCHAR2(64) NOT NULL,
  doc_id VARCHAR2(64) NOT NULL,
  chunk_no NUMBER NOT NULL,
  content CLOB NOT NULL,
  embedding VECTOR(*, FLOAT32) NOT NULL,
  PRIMARY KEY (collection_id, doc_id, chunk_no),
  FOREIGN KEY (collection_id, doc_id) REFERENCES atlas_rag_documents(collection_id, doc_id) ON DELETE CASCADE
);
