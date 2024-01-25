import json

if __name__ == '__main__':
    try:
        with open("meteo.json", "r") as init:
            d = json.load(init)
    except FileNotFoundError as e:
        print(f"{type(e).__name__} was raised: {e}")
    except Exception as e:
        print(f"{type(e).__name__} was raised: {e}")
    else:
        for key in d:
            print(d[key]['server'])
            print(d[key]['user'])
            print(d[key]['pass'])
            print(d[key]['localPath'])
            print(d[key]['remotePath'])
            print("\n")

        # keys method useful for this:
        print(list(d.keys()))
    # finally:
    #     print("finally executes always")


