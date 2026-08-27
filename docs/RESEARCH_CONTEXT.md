# Research context behind the benchmark

The benchmark tasks were chosen to reflect active LLM-system directions rather than arbitrary coding exercises.

## GraphRAG

Microsoft's GraphRAG work combines LLM-derived knowledge graphs, graph/community analysis, and retrieval for both local and global questions. DRIFT Search extends local search with community context and iterative follow-up questions.

References:
- Microsoft Research — Project GraphRAG: https://www.microsoft.com/en-us/research/project/graphrag/
- From Local to Global: A Graph RAG Approach to Query-Focused Summarization: https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/
- DRIFT Search: https://www.microsoft.com/en-us/research/blog/introducing-drift-search-combining-global-and-local-search-methods-to-improve-quality-and-efficiency/

## Agentic RAG and Agentic GraphRAG

Current Agentic RAG work emphasizes planning, iterative evidence gathering, tool use, stopping decisions, and trajectory quality rather than a fixed retrieve-once/generate-once pipeline.

References:
- ACL Findings 2026 — Data-Centric Perspectives on Agentic Retrieval-Augmented Generation: https://aclanthology.org/2026.findings-acl.78/
- 2026 survey — A Survey of Agentic GraphRAG: From Retrieval-augmented Generation to Graph-native Agents: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6713979

## Ontology + Knowledge Graph constraints

The benchmark treats an ontology as an explicit semantic constraint layer rather than asking an LLM to decide all class/relation validity implicitly. This motivates:
- class and relation validation
- domain/range checking
- alias alignment
- open-world entity resolution
- reviewable ontology induction rather than automatic mutation

## Structured outputs, tool routing, and bounded processing

Modern LLM application guidance increasingly separates semantic judgment from deterministic validation/processing. Structured outputs improve schema reliability, while bounded programmatic processing is useful for predictable stages such as filtering, ranking, deduplication, aggregation, and validation.

References:
- OpenAI model guidance: https://developers.openai.com/api/docs/guides/latest-model
- OpenAI function calling / Structured Outputs overview: https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api

## Why these ideas are useful for an agent-routing benchmark

The tasks naturally differ in reasoning demand:

- repository discovery can often be delegated cheaply
- deterministic schema/ontology checks should not require the strongest model
- multi-step planning and ambiguous alignment may require deeper reasoning
- provenance and evaluation need correctness checks even when code executes successfully

That variation makes the domain suitable for testing whether Luna/Terra/Sol routing reduces expensive-model exposure without degrading correctness.
