import requests
localhostURL= "http://localhost:81"

def test1() -> bool:
    response = requests.get(f"{localhostURL}/?items=100.200.300.400,127.0.0.1")
    if response.status_code != 200:
        return False
    json = response.json()
    if json.get("totalValid") ==2:
        return True
    return False
def test2() -> bool:
    response = requests.get(f"{localhostURL}/")
    if response.status_code != 200:
        return False
    json = response.json()
    if json.get("totalValid") ==0:
        return True
    return False
def main():
    success = test1() and test2()
    if success:
        exit(0)
    else:
        exit(1)
if __name__ == "__main__":
    main()
