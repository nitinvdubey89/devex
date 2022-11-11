import click


@click.command()
@click.option("--name", required=True, help="Your name.")
@click.option("--devp", "--p", is_flag=True, help="Add if you are DevNet Professional")
@click.option("--deve/--no-deve", is_flag=True, help="Add if you are DevNet Expert")
@click.option("--api", type=click.Choice(["netconf","restconf"]), default="netconf", show_default=True)
def demo():
    print("hi")


if __name__ == "__main__":
    demo()
