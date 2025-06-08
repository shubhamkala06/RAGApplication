from enum import Enum

class LogFields(str,Enum):
    QUERY_TEXT = "query_text"
    RETRIEVED_DOCS_COUNT = "retrieved_docs_count"
    RETRIEVED_SOURCES = "retrieved_sources"
    RETRIEVAL_LATENCY_MS = "retrieval_latency_ms"
    GENERATION_LATENCY_MS = "generation_latency_ms"
    TOTAL_LATENCY_MS = "total_latency_ms"
    GENERATED_TEXT_LENGTH = "generated_text_length"
    PIPELINE_STAGE = "pipeline_stage"
    SUCCESS = "success"

    # Evaluation metrics
    RELEVANCE_SCORE = "relevance_score"
    ACCURACY_SCORE = "accuracy_score"
    CONTEXTUAL_AWARENESS_SCORE = "contextual_awareness_score"
    RESPONSE_QUALITY_SCORE = "response_quality_score"
    