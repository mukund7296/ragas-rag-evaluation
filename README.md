
# RAGAS – RAG Evaluation Framework

Building a Retrieval-Augmented Generation (RAG) application is not enough. We also need to measure whether generated answers are accurate, relevant, and grounded in retrieved documents.

This project explores automated evaluation of RAG applications using **RAGAS**.

## Why RAGAS?

RAGAS helps evaluate the quality of RAG pipelines by measuring how well the system retrieves relevant context and generates reliable answers.

Key evaluation concepts include:

- **Faithfulness:** Is the answer supported by the retrieved context?
- **Answer Relevancy:** Does the answer address the user's question?
- **Context Precision:** Are the retrieved documents relevant?
- **Context Recall:** Does the retrieved context contain the information needed?

Note: The current quickstart configuration uses a custom `DiscreteMetric`. The metrics above are evaluation concepts and are not necessarily all enabled in this project yet.

## Project Structure

```text
rag_eval/
├── README.md
├── pyproject.toml
├── rag.py
├── evals.py
├── __init__.py
└── evals/
    ├── datasets/
    ├── experiments/
    └── logs/
```

## Quick Start

### 1. Configure your API key

Choose the provider configured in your evaluation code.

For example, Google Gemini:

```bash
export GOOGLE_API_KEY="your-google-api-key"
```

Never commit your actual API key.

### 2. Install dependencies

Using uv:

```bash
uv sync
```

Or using pip:

```bash
pip install -e .
```

### 3. Run the evaluation

Using uv:

```bash
uv run python evals.py
```

Or using pip:

```bash
python evals.py
```

## Experiments

RAGAS experiments help compare evaluation runs and understand how changes to a RAG pipeline affect answer quality.

Experiment outputs and execution logs are stored under:

```text
evals/experiments/
evals/logs/
```

## Customization

You can customize:

- Test questions and expected evaluation criteria.
- The LLM provider and model.
- The evaluation metric and grading instructions.
- The RAG retrieval and answer-generation workflow.

See `evals.py` and `rag.py` for the implementation.

## Learning Goals

- Understand RAG evaluation.
- Explore RAGAS metrics and experiments.
- Evaluate generated answers against retrieved context.
- Compare evaluation runs.
- Build a foundation for continuous RAG quality monitoring.

## Documentation

[RAGAS Documentation](https://docs.ragas.io/)
