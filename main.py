from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from github_reader import clone_repo
from code_reader import read_code
from ai_reviewer import review_code
from static_analyzer import analyze_python


app = FastAPI(title="AI Code Review Agent")


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://ai-code-review-frontend.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "AI Code Review Agent API is running"}


@app.post("/review")
def review(repo_url: str):

    folder = clone_repo(repo_url)
    files = read_code(folder)

    reviews = []

    for file in files:

        analysis = []

        if file["file"].endswith(".py"):
            analysis = analyze_python(file["file"])

        result = review_code(
            file["code"],
            file["file"]
        )

        reviews.append({
            "file": file["file"],
            "static_analysis": analysis,
            "ai_review": result
        })

    return {
        "message": "AI code review completed",
        "total_files": len(reviews),
        "reviews": reviews
    }