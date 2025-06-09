# This finds any file or directory with a "\" in its name, deepest-first.
find mods -depth -name '*\\*' | while IFS= read -r oldpath; do
  # Compute the new path by replacing every "\" with "/"
  newpath="${oldpath//\\/\/}"

  # Make sure the target directory exists
  mkdir -p "$(dirname "$newpath")"

  # Move it into place (this will create nested dirs)
  mv "$oldpath" "$newpath"
done