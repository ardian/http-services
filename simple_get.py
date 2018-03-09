import requests


def main():
    url = "http://ardian.me"
    resp = requests.get(url)

    if resp.status_code != 200:
        print("Error reqeusting URL, {}").format(resp.status_code)
        return
    print(resp.text[:500])


if __name__ == '__main__':
    main()
