import click

import square


@click.command()
@click.argument("value", type = int )
def main(value):
    print(f"The square of {value} is {square.square(value)}")


main()
