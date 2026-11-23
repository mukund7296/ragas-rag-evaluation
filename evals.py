
import os
import sys
import asyncio
from pathlib import Path

from openai import OpenAI

from ragas import Dataset, experiment
from ragas.llms import llm_factory
from ragas.metrics import DiscreteMetric

# Import your RAG application
sys.path.insert(0, str(Path(__file__).parent))
from rag import default_rag_client


# --------------------------------------------------
# 1. API CONFIGURATION
# --------------------------------------------------

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY is missing. "
        "Please configure it in your terminal."
    )


# --------------------------------------------------
# 2. GEMINI CLIENT
# --------------------------------------------------

# This OpenAI SDK client connects to Google's API.
# It does NOT use the OpenAI service or require an OpenAI key.

gemini_client = OpenAI(
    api_key=GOOGLE_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


# --------------------------------------------------
# 3. RAGAS EVALUATION LLM
# --------------------------------------------------

llm = llm_factory(
    "gemini-2.0-flash",
    provider="openai",
    client=gemini_client,
)


# --------------------------------------------------
# 4. RAG APPLICATION CLIENT
# --------------------------------------------------

# Assumes default_rag_client accepts an OpenAI-compatible
# client through its llm_client argument, as in your
# original commented-out code.

rag_client = default_rag_client(
    llm_client=gemini_client,
    logdir="evals/logs",
)


# --------------------------------------------------
# 5. LOAD DATASET
# --------------------------------------------------

def load_dataset():

    dataset = Dataset(
        name="test_dataset",
        backend="local/csv",
        root_dir="evals",
    )

    data_samples = [
        {
            "question": "What is Ragas 0.3?",
            "grading_notes": (
                "- Experimentation as the central pillar\n"
                "- Provides abstractions for datasets, experiments "
                "and metrics\n"
                "- Supports evaluations for RAG, LLM workflows "
                "and agents"
            ),
        },
        {
            "question": "How are experiment results stored in Ragas 0.3?",
            "grading_notes": (
                "- Configured using different backends like local "
                "and Google Drive\n"
                "- Stored under experiments/ folder in backend storage"
            ),
        },
        {
            "question": "What metrics are supported in Ragas 0.3?",
            "grading_notes": (
                "- Discrete metrics\n"
                "- Numerical metrics\n"
                "- Ranking metrics"
            ),
        },
    ]

    for sample in data_samples:
        dataset.append(sample)

    dataset.save()

    return dataset


# --------------------------------------------------
# 6. DEFINE EVALUATION METRIC
# --------------------------------------------------

my_metric = DiscreteMetric(
    name="correctness",
    prompt=(
        "Check whether the response contains the important "
        "points mentioned in the grading notes. "
        "Return only 'pass' or 'fail'.\n\n"
        "Response: {response}\n"
        "Grading Notes: {grading_notes}"
    ),
    allowed_values=["pass", "fail"],
)


# --------------------------------------------------
# 7. RUN EXPERIMENT
# --------------------------------------------------

@experiment()
async def run_experiment(row):

    # Get the answer from your RAG application
    response = rag_client.query(row["question"])

    answer = response.get("answer", "")

    # Evaluate the answer using Gemini
    score = my_metric.score(
        llm=llm,
        response=answer,
        grading_notes=row["grading_notes"],
    )

    experiment_view = {
        **row,
        "response": answer,
        "score": score.value,
        "log_file": response.get("logs", ""),
    }

    return experiment_view


# --------------------------------------------------
# 8. MAIN FUNCTION
# --------------------------------------------------

async def main():

    print("\nLoading dataset...")

    dataset = load_dataset()

    print("Dataset loaded successfully!")
    print("Number of test cases:", len(dataset))

    print("\nStarting RAG evaluation using Gemini...")

    experiment_results = await run_experiment.arun(dataset)

    print("\nExperiment completed!")
    print("Experiment results:", experiment_results)

    # Save results
    experiment_results.save()

    print("\nExperiment results saved successfully!")


# --------------------------------------------------
# 9. EXECUTION
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())
