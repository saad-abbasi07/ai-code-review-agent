import os

ALLOWED_EXTENSIONS = {
    ".py", ".js", ".ts", ".jsx", ".tsx",
    ".java", ".cpp", ".c", ".cs", ".go"
}

IGNORE_DIRS = {
    ".git", "node_modules", "venv",
    "__pycache__", "dist", "build"
}


def read_code(repo_folder):
    files = []

    for root, dirs, filenames in os.walk(repo_folder):

        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for filename in filenames:
            extension = os.path.splitext(filename)[1]

            if extension in ALLOWED_EXTENSIONS:
                path = os.path.join(root, filename)

                try:
                    with open(path, "r", encoding="utf-8") as file:
                        code = file.read()

                    files.append({
                        "file": path,
                        "code": code
                    })

                except UnicodeDecodeError:
                    pass

    return files