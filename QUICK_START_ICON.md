# Quick Start - Adding Your Icon

You now have everything set up to build your executable with a custom icon! Here are your options:

## ⚡ FASTEST - Generate a Simple Icon (30 seconds)

1. Install Pillow (if not already installed):
   ```bash
   pip install pillow
   ```

2. Run the icon generator:
   ```bash
   python create_simple_icon.py
   ```

3. Follow the prompts to customize or use defaults

4. Done! `app_icon.ico` is created and ready to use

5. Build your executable:
   ```bash
   build.bat
   ```

## 🎨 CUSTOM - Use Your Own Image

1. Get a square image (PNG, JPG, etc.) - at least 256x256 pixels

2. Go to https://convertico.com/

3. Upload your image

4. Download as `app_icon.ico`

5. Save it in the `gui` folder

6. Build your executable:
   ```bash
   build.bat
   ```

## 📥 DOWNLOAD - Use a Professional Icon

1. Visit https://icons8.com/icons/set/train

2. Search for "train", "railroad", or "freight"

3. Download as 256px PNG (free)

4. Convert to .ico at https://convertico.com/

5. Save as `app_icon.ico` in the `gui` folder

6. Build your executable:
   ```bash
   build.bat
   ```

## ✅ What's Already Done

- ✅ `build.spec` is configured to use `app_icon.ico`
- ✅ Build script is ready
- ✅ Icon generator script is available
- ✅ Instructions are complete

## 🚀 Next Steps

**Just need to:**
1. Create/download `app_icon.ico` (use one of the methods above)
2. Run `build.bat`
3. Your executable will have a custom icon!

## 💡 Recommendations

**For a professional Run8-themed icon:**
- Railroad crossing sign
- Steam locomotive silhouette
- Train tracks
- Freight car icon
- Use blue or railroad-appropriate colors

**For a simple branded icon:**
- Run the `create_simple_icon.py` script
- Use "R8" text with blue background
- Quick and professional-looking

## 📁 File Checklist

After choosing your method, you should have:
- ✅ `app_icon.ico` in the gui folder
- ✅ `build.bat` (ready to run)
- ✅ `build.spec` (configured for icon)

Then just run `build.bat` and you're done! 🎉
