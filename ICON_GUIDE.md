# Adding a Custom Icon to Your Application

Your build is now configured to use `app_icon.ico` as the application icon. Here's how to create or obtain one.

## Option 1: Quick - Use an Online Converter

### Step 1: Find or Create an Image
- Use any PNG, JPG, or other image (square images work best)
- Recommended size: 256x256 pixels or larger
- For Run8, you might use a train or railroad-related image

### Step 2: Convert to .ico Format

Use one of these free online converters:
- **ConvertICO**: https://convertico.com/
- **ICO Convert**: https://icoconvert.com/
- **AnyConv**: https://anyconv.com/png-to-ico-converter/

Instructions:
1. Upload your image
2. Select sizes: 16x16, 32x32, 48x48, 64x64, 128x128, 256x256
3. Download the .ico file
4. Save it as `app_icon.ico` in the `gui` folder

## Option 2: Use Free Icon Resources

Download pre-made icons from:

### Free Icon Sites:
- **Icons8**: https://icons8.com/ (search "train" or "railroad")
- **Flaticon**: https://www.flaticon.com/ (free with attribution)
- **IconArchive**: https://www.iconarchive.com/

### Railroad/Train Icon Suggestions:
- Steam locomotive
- Railroad crossing sign
- Train tracks
- Freight car
- Railway station

Look for icons that offer .ico download or download PNG and convert.

## Option 3: Create Your Own (Windows)

### Using Paint + Online Converter:
1. Open Paint
2. Create a square canvas (256x256)
3. Design your icon or paste an image
4. Save as PNG
5. Use online converter (Option 1) to convert to .ico

### Using GIMP (Free Software):
1. Download GIMP: https://www.gimp.org/
2. Create new image: 256x256 pixels
3. Design your icon
4. Export as .ico:
   - File → Export As
   - Change extension to `.ico`
   - Select all standard sizes in the export dialog

## Option 4: Professional Tools

### If you have Adobe Photoshop:
1. Create 256x256 image
2. Install ICO format plugin
3. Save as .ico with multiple sizes

## Icon Requirements

For best results, your icon should:
- ✅ Be square (same width and height)
- ✅ Have multiple sizes embedded: 16x16, 32x32, 48x48, 256x256
- ✅ Use simple, clear graphics (will be displayed small)
- ✅ Have good contrast
- ✅ Be saved as `app_icon.ico` in the gui folder

## Quick Test Icons

Want to test the build first? Here are some simple ideas:
- Download a free train icon from Icons8
- Use your company logo
- Create text-based icon with your initials

## After Adding the Icon

1. Place `app_icon.ico` in the `gui` folder (same folder as r8it.py)
2. Run `build.bat`
3. The executable will now have your custom icon!

## Verifying the Icon

After building:
- Check `dist/Run8IndustryTool.exe` in File Explorer
- The icon should appear on the .exe file
- Right-click the .exe → Properties → should show your icon
- When you run it, the icon appears in the taskbar

## Troubleshooting

### Icon doesn't appear:
- Make sure file is named exactly `app_icon.ico`
- Make sure it's in the gui folder
- Rebuild with `build.bat`
- Try a different .ico file to rule out corruption

### Icon looks blurry:
- Use larger source image (256x256 minimum)
- Make sure .ico contains multiple sizes
- Ensure source image is sharp and high-quality

## Recommended Free Icon

For a quick professional look, I recommend:
1. Go to https://icons8.com/icons/set/train
2. Search for "freight train" or "railroad"
3. Download as 256px PNG
4. Convert to .ico at https://convertico.com/
5. Save as `app_icon.ico` in gui folder
6. Run build.bat

That's it! Your executable will look professional and recognizable.
