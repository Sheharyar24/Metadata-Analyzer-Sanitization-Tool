import PIL.Image
import PIL.ExifTags
import os

BANNER = """

███╗   ███╗███████╗████████╗ █████╗ ██████╗  █████╗ ████████╗ █████╗ 
████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
██╔████╔██║█████╗     ██║   ███████║██║  ██║███████║   ██║   ███████║
██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║  ██║██╔══██║   ██║   ██╔══██║
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██████╔╝██║  ██║   ██║   ██║  ██║
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝

"""

class MetadataHacker:
  def __init__(self):
    pass

  def print_banner(self):
    print(BANNER)

  def extract_metadata(self, image_path):
    try:
      img = PIL.Image.open(image_path)
      exif = {PIL.ExifTags.TAGS[key]: value for key, value in img.getexif().items() if key in PIL.ExifTags.TAGS}
      return exif
    except Exception as e:
      print(f"Error extracting metadata: {e}")
      return None

def main():
  hacker = MetadataHacker()
  hacker.print_banner()

  while True:
    print("\n[?] ENTER TARGET FILE PATH (OR 'EXIT' TO ABORT): ")
    image_path = input().strip()

    if image_path.lower() == "exit":
      print("[+] TERMINATING SESSION...")
      break

    if not os.path.isfile(image_path):
      print("[-] ERROR: FILE NOT FOUND. CHECK YOUR PATH.")
      continue

    metadata = hacker.extract_metadata(image_path)
    if metadata:
      print("\n[!] EXTRACTED METADATA:")
      for key, value in metadata.items():
        print(f"{key}: {value}")

      print('\n[?] SELECT OPERATION:')
      print('[1] REMOVE ALL METADATA')
      print('[2] MODIFY METADATA')
      print('[3] CANCEL')
      choice = input().strip()

      if choice == '1':
        pass # Implement metadata removal logic here
      elif choice == '2':
        pass # Implement metadata modification logic here
      elif choice == '3':
        print("\n[+] OPERATION CANCELLED.")
        break


if __name__ == "__main__":
  main()