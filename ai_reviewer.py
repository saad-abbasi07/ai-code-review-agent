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
You are a professional software engineer performing a defensive
code-quality review.

Analyze the following source code only to help the developer
improve the safety, reliability, maintainability, and performance
of their application.

Do NOT provide instructions for exploiting vulnerabilities.
Only identify potential weaknesses and recommend defensive fixes.

FILE:
{filename}

SOURCE CODE:
{code}

Review the code for:

1. Bugs and potential runtime errors
2. Security weaknesses and insecure coding practices
3. Performance problems
4. Reliability and error-handling problems
5. Code quality and maintainability issues
6. Input validation problems
7. API design problems

For every important issue, provide:

- Severity: Critical / High / Medium / Low
- Category
- Problem
- Explanation
- Defensive suggested fix

Focus on practical improvements that a developer can implement.

If the code has no important issues, respond exactly:

"No major issues found."
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text