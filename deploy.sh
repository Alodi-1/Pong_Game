#!/bin/bash
# Auto-build + move + push Pong game to GitHub Pages
# Make sure you run this inside your Pong project folder

# Step 1: Build with pygbag
echo "🎮 Building Pong game with pygbag..."
pygbag --build .

# Step 2: Move build/web contents to repo root
echo "📂 Moving build/web files to repo root..."
rm -rf tmp_build
mv build/web tmp_build
cp -r tmp_build/* .
rm -rf tmp_build build

# Step 3: Commit & push to GitHub
echo "📦 Committing changes..."
git add .
git commit -m "Deploy Pong game to GitHub Pages"
git push -u origin main

# Step 4: Done
echo "✅ Deployment complete! Enable GitHub Pages in Settings > Pages."
echo "After enabling, your game will be live at: https://<username>.github.io/<repo-name>/"
