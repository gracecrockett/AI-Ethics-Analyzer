import openai
import os

def run_gpt_analysis(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    messages = [
        {"role": "system", "content": "You are an AI Ethics Analyst. Evaluate the given AI use case for potential ethical concerns in five categories: Fairness, Transparency, Privacy, Bias Risk, and Accountability. Provide brief feedback for each."},
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.5,
    )

    return response.choices[0].message["content"]
