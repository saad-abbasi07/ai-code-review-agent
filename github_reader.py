import os
from git import Repo

def clone_repo(repo_url):
    folder = "temp_repo"

    if os.path.exists(folder):
        return folder

    Repo.clone_from(repo_url, folder)

    return folder