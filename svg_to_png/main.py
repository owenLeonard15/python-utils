import argparse
import cairosvg

def convert_svg_to_png(input_svg: str, output_png: str, scale: float = 1.0):
    """
    Convert an SVG file to either a PNG or ICO file using cairosvg and Pillow.
    """
    if output_png.lower().endswith('.ico'):
        # Convert SVG to PNG bytes using cairosvg
        png_bytes = cairosvg.svg2png(url=input_svg, scale=scale)
        from io import BytesIO
        from PIL import Image
        image = Image.open(BytesIO(png_bytes))
        image.save(output_png, format='ICO')
    elif output_png.lower().endswith('.png'):
        cairosvg.svg2png(url=input_svg, write_to=output_png, scale=scale)
    else:
        raise ValueError("Unsupported output format. Use .png or .ico")


if __name__ == '__main__':
    '''
    python main.py --input_svg favicon.svg --output_png favicon.png --scale 2
    python main.py --input_svg favicon.svg --output_png favicon.ico
    '''
    parser = argparse.ArgumentParser(
        description="Convert an SVG icon to either a PNG or ICO favicon."
    )
    parser.add_argument(
        "--input_svg", required=True, help="Input SVG file path (e.g., favicon.svg)"
    )
    parser.add_argument(
        "--output_png", required=True, help="Output file path (e.g., favicon.png or favicon.ico)"
    )
    parser.add_argument(
        "--scale", type=float, default=1.0,
        help="Scale factor for output resolution (default is 1.0)"
    )
    
    args = parser.parse_args()
    
    convert_svg_to_png(args.input_svg, args.output_png, args.scale)
    print(f"Successfully converted '{args.input_svg}' to '{args.output_png}' with scale {args.scale}.")
