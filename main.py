import PIL.Image
import PIL.ExifTags
import piexif
import os
import time

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
    
  def remove_metadata(self, image_path):
    try:
      img = PIL.Image.open(image_path)
      data = img.get_flattened_data()
      img_without_exif = PIL.Image.new(img.mode, img.size)
      img_without_exif.putdata(data)
      new_path = os.path.splitext(image_path)[0] + "_no_metadata" + os.path.splitext(image_path)[1]
      img_without_exif.save(new_path)
      print(f"[+] METADATA REMOVED. NEW FILE: {new_path}")
    except Exception as e:
      print(f"Error removing metadata: {e}")

  def modify_metadata(self, image_path):
    try:
      exif_dict = piexif.load(image_path)
      modified = False

      # Process each IFD (Image File Directory)
      for ifd_name in ("0th", "Exif", "GPS", "1st", "Interop"):
        ifd = exif_dict[ifd_name]
        print(f"\n[!] {ifd_name} IFD METADATA:")
        
        for tag in list(ifd.keys()):
          tag_name = piexif.TAGS[ifd_name][tag]["name"]
          current_value = ifd[tag]
          
          print(f"\n{tag_name}: {current_value}")
          print("[?] ENTER NEW VALUE (OR PRESS ENTER TO KEEP ORIGINAL): ")
          new_value = input().strip()
          
          if new_value:
            try:
              # Try to convert to bytes if needed
              if isinstance(current_value, bytes):
                ifd[tag] = new_value.encode('utf-8')
              else:
                ifd[tag] = new_value
              modified = True
              print("[+] VALUE UPDATED.")
            except Exception as e:
              print(f"[-] ERROR UPDATING VALUE: {e}")
          else:
            print("[+] KEEPING ORIGINAL VALUE.")
      
      if modified:
        new_path = os.path.splitext(image_path)[0] + "_modified" + os.path.splitext(image_path)[1]
        exif_bytes = piexif.dump(exif_dict)
        img = PIL.Image.open(image_path)
        img.save(new_path, exif=exif_bytes)
        print(f"\n[+] METADATA MODIFIED. NEW FILE: {new_path}")
      else:
        print("\n[-] NO CHANGES MADE.")
    except Exception as e:
      print(f"Error modifying metadata: {e}")

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
        print("\n[+] REMOVING METADATA...")
        time.sleep(2) # Simulate processing time
        hacker.remove_metadata(image_path)
        print("[+] OPERATION COMPLETED.")

      elif choice == '2':
        print("\n[+] MODIFYING METADATA...")
        time.sleep(2) # Simulate processing time
        hacker.modify_metadata(image_path)
        print("[+] OPERATION COMPLETED.")
      elif choice == '3':
        print("\n[+] OPERATION CANCELLED.")
        break
    else:
      time.sleep(1)
      print("[-] NO METADATA FOUND IN THIS FILE.")


if __name__ == "__main__":
  main()