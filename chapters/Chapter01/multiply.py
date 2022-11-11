import click

@click.group()
def demo():
    pass

@demo.command()
@click.option("--a", type=int)
@click.option("--b", type=int)
def step1(a, b):
  print(f"{a} x {b} = {a*b}")

# @demo.command()
# def output():
#     print("You")

if __name__ == "__main__":
    step1()