from prefect import flow, task

@task
def say_hello(name):
    print(f"hello {name}")

@task
def say_goodbye(name):
    print(f"goodbye {name}")

@flow
def greetings(names):
    for name in names:
        say_hello.submit(name)
        say_goodbye.submit(name)

if __name__ == "__main__":
    greetings(["arthur", "trillian", "ford", "marvin"])

