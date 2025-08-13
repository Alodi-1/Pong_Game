#!/bin/bash
# === Step 1: Build game for web using pygbag ===
echo "🔨 Building Pong game for web..."
pygbag --build main.py

# === Step 2: Move files to root ===
echo "📂 Moving web build files to repository root..."
cp -r build/web/* ./

# Optional: Remove the old build folder to keep repo clean
rm -rf build

# === Step 3: Commit & push to GitHub ===
echo "📤 Pushing to GitHub..."
git add .
git commit -m "Deploy Pong game to GitHub Pages"
git push origin main

# === Step 4: Done ===
echo "✅ Deployment complete! Visit your GitHub Pages link after 1-2 mins."
