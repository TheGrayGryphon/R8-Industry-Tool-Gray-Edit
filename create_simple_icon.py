"""
Simple Icon Generator for Run8 Industry Tool
Creates a basic text-based icon as a placeholder or simple branding

Requirements: pip install pillow
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import os
except ImportError:
    print("ERROR: Pillow library not installed")
    print("Please install it with: pip install pillow")
    input("Press Enter to exit...")
    exit(1)


def create_icon():
    """Create a simple icon with text"""

    # Icon settings
    sizes = [16, 32, 48, 64, 128, 256]
    text = "R8"  # Main text to display
    bg_color = (41, 128, 185)  # Blue background (RGB)
    text_color = (255, 255, 255)  # White text

    print("=" * 50)
    print("Run8 Industry Tool - Icon Generator")
    print("=" * 50)
    print()

    # Ask user for customization
    custom = input("Use default 'R8' text and blue background? (Y/n): ").strip().lower()

    if custom == 'n':
        text = input("Enter text for icon (1-3 characters): ").strip()[:3]
        print("\nChoose background color:")
        print("1. Blue (default)")
        print("2. Green")
        print("3. Red")
        print("4. Orange")
        print("5. Purple")
        choice = input("Enter choice (1-5): ").strip()

        colors = {
            '1': (41, 128, 185),   # Blue
            '2': (39, 174, 96),    # Green
            '3': (192, 57, 43),    # Red
            '4': (230, 126, 34),   # Orange
            '5': (142, 68, 173),   # Purple
        }
        bg_color = colors.get(choice, (41, 128, 185))

    print(f"\nCreating icon with text '{text}'...")

    # Create images for each size
    images = []
    for size in sizes:
        # Create image
        img = Image.new('RGB', (size, size), bg_color)
        draw = ImageDraw.Draw(img)

        # Try to use a nice font, fall back to default if not available
        try:
            font_size = int(size * 0.5)
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()

        # Get text bounding box for centering
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Calculate position to center text
        x = (size - text_width) // 2
        y = (size - text_height) // 2

        # Draw text
        draw.text((x, y), text, fill=text_color, font=font)

        images.append(img)

    # Save as .ico file with multiple sizes
    output_file = 'app_icon.ico'
    images[0].save(
        output_file,
        format='ICO',
        sizes=[(s, s) for s in sizes]
    )

    print(f"\n✓ Icon created successfully: {output_file}")
    print(f"✓ Sizes included: {', '.join([f'{s}x{s}' for s in sizes])}")
    print("\nYou can now run build.bat to create your executable with this icon.")
    print()

    # Show preview
    try:
        images[-1].show()
        print("(Icon preview opened)")
    except:
        pass


if __name__ == "__main__":
    try:
        create_icon()
    except Exception as e:
        print(f"\nERROR: {e}")

    input("\nPress Enter to exit...")
