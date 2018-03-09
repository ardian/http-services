import requests

#import json


def main():

    #get user input for github user and repo
    user, repo = get_repo_info()

    # github API URL
    url = 'https://api.github.com/repos/{}/{}'.format(user, repo)
    # save respond from request
    resp = requests.get(url)

    #check if response is 200, if not the case respond error message
    if resp.status_code != 200:
        print("Error accessing repos: {}".format(resp.status_code))
        return
    #json_data = json.loads(resp.text) # convert to dict using json lib
    # convert json into dict using requests
    json_data = resp.json()

    # get clone url from dict
    clone = json_data.get("clone_url", "ERROR: NO DATA")

    #print repo name and user
    print("To clone {}'s repo named {}".format(user, repo))

    print("The command is: ")

    #print clone url
    print("git clone {}".format(clone))


# define function to get user input for username and reponame
def get_repo_info():
    user = input("What is the username? ")
    repo = input("What is the repo name? ")

    return user, repo


if __name__ == '__main__':
    main()
