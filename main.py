import click


@click.command()
@click.option('-c', '--count', type=int, default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)


if __name__ == '__main__':
    hello()
