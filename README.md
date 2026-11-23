
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
<img width="355" height="518" alt="image" src="https://github.com/user-attachments/assets/5e131f5c-a0a1-4c5b-a238-cbfdc2527771" />


## Real-World Use Case: Financial Services RAG Evaluation

### Scenario: Banking and Loan Assistant

Financial institutions maintain large collections of documents, including:

- Personal loan policies
- Interest rate documentation
- Transaction fee schedules
- Credit card terms and conditions
- Account management policies
- Compliance and regulatory guidelines

A RAG-based banking assistant can retrieve information from these documents and answer customer questions.

### Example: Early Loan Repayment

**Sample financial policy (fictional):**

- Loan amount: €10,000
- Annual interest rate: 6%
- Maximum repayment period: 5 years
- Early repayment fee: 1% of the outstanding balance

**Customer Question:**

"Can I repay my personal loan early, and what is the fee?"

**Retrieved Context:**

"Customers can repay their personal loans before the maturity date. An early repayment fee of 1% of the outstanding balance applies."

**Generated Answer:**

"Yes, you can repay your personal loan early. An early repayment fee of 1% of the outstanding balance applies."

**Reference Answer:**

"Early repayment is allowed, and a fee of 1% of the outstanding balance applies."

### How RAGAS Evaluates This Answer

| Metric | Evaluation Purpose |
|---|---|
| Faithfulness | Checks whether the answer is supported by the retrieved policy |
| Answer Relevancy | Checks whether the answer addresses the customer's question |
| Context Precision | Checks whether the retrieved document is relevant |
| Context Recall | Checks whether the required policy information was retrieved |
| Answer Correctness | Compares the generated answer with the reference answer |

### Example of an Incorrect Answer

Suppose the AI responds:

"You can repay your loan early without any additional fee."

Although this answer addresses the customer's question, it contradicts the retrieved policy.

RAGAS evaluation can help identify the issue and provide insights into the quality of the RAG pipeline.

**Important:** This is an illustrative example using fictional financial policy data, not actual bank data or financial advice.

