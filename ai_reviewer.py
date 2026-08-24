import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=api_key)


def review_code(code, filename):

    prompt = f"""
You are an expert software code reviewer.

Review this source code.

FILE:
{filename}

CODE:
{code}

Find:
1. Bugs
2. Security vulnerabilities
3. Performance problems
4. Code quality problems

For each problem provide:
- Severity
- Category
- Problem
- Explanation
- Suggested fix

If there are no important problems, say:
"No major issues found."
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text