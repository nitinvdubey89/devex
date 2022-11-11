import click

@click.command()
@click.option('-s', '--safety', 'safe')
@click.option('--enabled', is_flag=True, default=False, show_default=True)
@click.option('--nargs', nargs=3, type=int)
@click.option('--item', '-i', 'mytuple', type=(int, str))
def test(safe, enabled, nargs, mytuple):
    print(safe, enabled, nargs, mytuple)

if __name__ == "__main__":
    test()