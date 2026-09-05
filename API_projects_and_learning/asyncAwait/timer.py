import time


# this is a syncrones function
def countTime():
    print("count timer started")
    time.sleep(5)
    print("timer ended")
def callash():
    print("calling ash started")
    time.sleep(3)
    print("timer ended")


def  main():
    countTime()
    callash()

if __name__ == "__main__":
    main()
