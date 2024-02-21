from rembg import remove
from PIL import Image
input_path="/Users/naveenkumar/Desktop/.vscode/15_2_24_python/my_pic.jpg"
output_path="no_bg.jpg"
input = Image.open(input_path)
output =remove(input)
output.save(output_path)