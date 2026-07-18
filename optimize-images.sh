#!/bin/bash

# תוכנה לאופטימיזציה של תמונות
# המרת JPG ל-WebP עם איכות גבוהה

echo "🖼️  Starting image optimization..."

for img in images/*.jpg; do
    if [ -f "$img" ]; then
        basename="${img%.jpg}"
        webp_file="${basename}.webp"
        
        # המרה ל-WebP עם איכות 85% (איזון מושלם בין איכות לגודל)
        ffmpeg -i "$img" -c:v libwebp -quality 85 -lossless 0 -compression_level 6 "$webp_file" -y 2>/dev/null
        
        if [ -f "$webp_file" ]; then
            original_size=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img")
            webp_size=$(stat -f%z "$webp_file" 2>/dev/null || stat -c%s "$webp_file")
            reduction=$(( (original_size - webp_size) * 100 / original_size ))
            
            echo "✅ $(basename $img) -> $(basename $webp_file) (Saved ${reduction}%)"
        fi
    fi
done

echo "✨ Optimization complete!"
