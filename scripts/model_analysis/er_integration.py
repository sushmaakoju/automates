import requests


def main():
    webservice = "http://localhost:8000"

    eqn_pic_path = "8.png"
    res = requests.post(
        f"{webservice}/decode_equation/",
        # headers={"Content-type": "multipart/form-data"},
        files={"file": (eqn_pic_path, open(eqn_pic_path, "rb"), "image/png")},
    )

    data = res.json()
    print(data)
    print(type(data))


if __name__ == "__main__":
    main()
