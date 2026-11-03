# Generative AI Agents, knowledge, tools, and sessions

Reviewed: 2026-11-03

## Choose the product boundary

Use Generative AI Agents when its supported knowledge and tool orchestration fit. Direct Generative AI inference, AIDP agent features and custom application orchestration have different APIs and resource contracts. Identify the exact product before selecting SQL, retrieval or function-calling behavior.

## Resource and identity map

Separate agent configuration, tools, knowledge bases/data sources, ingestion jobs, deployment endpoints and conversational sessions. Human administration, endpoint invocation, source access and tool execution may use different principals. A knowledge base created by an administrator does not automatically enforce every end user's source permissions.

## Working sequence

1. Define the user task, allowed data, required tools, session ownership and response contract.
2. Select currently supported tools, models and regions. Inspect the specific tool's execution and authorization semantics.
3. Configure source connectivity/credentials and scoped access. Ingest a bounded source and inspect failed or skipped documents separately from overall job state.
4. Configure the agent and endpoint. Treat session identifiers as user-scoped application state; never share conversational context across unrelated users.
5. Invoke with a bounded question and inspect retrieved sources, citations and actual tool effects separately.
6. For tools that write, enforce authorization in the tool/API itself and preserve any required application approval flow. Prompt instructions are not access control.

## Change and recovery

Record agent/tool configuration, source version and endpoint consumers. Changes to a SQL tool or API schema can change behavior even when the endpoint ID stays constant. Reconcile failed ingestion and document removal through the supported source/knowledge lifecycle; don't assume deleting a source object immediately revokes an indexed copy.

Budget inference, ingestion and retained supporting resources with current service terms. Clean up sessions/endpoints and application-owned knowledge artifacts within scope while preserving source systems. Use the [RAG recipe](recipe-rag-application.md) when the application owns retrieval or needs explicit permission filtering.

## Sources

- [Agents overview](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/overview.htm)
- [Agents access](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/iam-policies.htm)
