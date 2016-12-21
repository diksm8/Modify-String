import click
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('text')
@click.option('-m', '--modify', required=True, help='How the string should be modified.', type=click.Choice(['upper', 'lower', 'fupper']))
def main(text, modify):
	"""Simple script to modify a string.

	Made this because a friend needed help with his programming homework."""
	if modify == 'upper':
		print text.upper()
	if modify == 'lower':
		print text.lower()
	if modify == 'fupper':
		print text[0].upper() + text[1:]

if __name__ == '__main__':
	main()