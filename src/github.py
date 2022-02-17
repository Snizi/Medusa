from github import Github, UnknownObjectException
from github.GithubException import GithubException

def auth():

    token = "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"
    g = Github(token)
    user = g.get_user()
    return user



user = auth()


def upload_files(recon_folder):
    user.get_repo('recon')


