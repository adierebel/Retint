from os import path, getcwd
from PIL import Image
import click

def echo_click(*args, Color=None):
	Text = []
	for i in args:
		Text.append(str(i))
	Text = " ".join(Text)
	if Color:
		click.echo(click.style(Text, fg=Color))
	else:
		click.echo(Text)

def process(Filename):
	# Path
	ResourcePath	= getcwd()
	ResourceFolder	= [
		"drawable-mdpi",
		"drawable-hdpi",
		"drawable-xhdpi",
		"drawable-xxhdpi",
		"drawable-xxxhdpi"
	]

	# Loop for Folder
	for Folder in ResourceFolder:

		# Build path
		Filepath = path.join(ResourcePath, Folder, Filename + ".png")

		# Check file
		if path.isfile(Filepath):
			# Print info
			echo_click(" * Processing " + Filepath + " done", Color="green")

			# Open image
			IMGOriginal	= Image.open(Filepath)
			Width		= IMGOriginal.width
			Height		= IMGOriginal.height
			
			# Save
			IMGBase	= Image.new('RGBA', (Width, Height), (255, 0, 0, 0))
			IMGBase = Image.alpha_composite(IMGOriginal, IMGOriginal)
			IMGBase = Image.alpha_composite(IMGBase, IMGOriginal)
			IMGBase.save(Filepath)

		else:
			# Print infp
			echo_click(" * Failed " + Filepath + " not found", Color="red")

@click.command()
@click.argument('filename', default=None)
def cli(filename):
	try:
		# Process
		process(filename)

	except KeyboardInterrupt:
		print(" * Exit")
	
	except Exception as e:
		echo_click(" * Error: " + str(e), Color="red")