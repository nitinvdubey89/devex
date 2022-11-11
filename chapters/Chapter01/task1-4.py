import click

@click.command()
@click.pass_context
def function1(ctx):
    ctx.ensure_object(dict)
    function2()
    function3()

@click.pass_context
def function2(ctx):
    ctx.obj['hello'] = 'world'

@click.pass_context
def function3(ctx):
    print(ctx.obj['hello'])


if __name__ == "__main__":
    function1()