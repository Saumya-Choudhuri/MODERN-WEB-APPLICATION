from PILL import Image

# Load the image
image = Image.open('/Users/saumyachoudhuri/VS Code/modern web application/icons8-facebook-logo-30.png')

# Convert the image to RGB (if it's not already in RGB format)
rgb_image = image.convert('RGB')

# Split the image into its RGB components
r, g, b = rgb_image.split()

# Save or display the RGB components
r.save('red_component.jpg')
g.save('green_component.jpg')
b.save('blue_component.jpg')

# Optionally, display the RGB components
r.show()
g.show()
b.show()