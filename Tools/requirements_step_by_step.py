import subprocess
import sys
from tqdm import tqdm
import time

def install(package):
    try:
        # Use `-m` to run the `pip` module, i
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
        return True, None
    except subprocess.CalledProcessError as e:
        return False, str(e)

def main():
    with open("Path of requirements.txt", "r") as f:
        packages = f.readlines()

    # Filter out packages starting with torch, torchaudio, or torchvision
    packages = [package.strip() for package in packages 
                if package.strip() and not package.startswith("#") 
                and not package.startswith("torch") 
                and not package.startswith("torchaudio") 
                and not package.startswith("torchvision")]

    failed_packages = []

    # tqdm() creates a progress bar that iterates over each package in the packages list
    # enumerate() function wraps an iterable object (like a list) into an enumeration object, returning both the index and corresponding element
    for i, package in enumerate(tqdm(packages, desc="Installing packages", unit="pkg")):
        # print(f"\nInstalling {package} ({i + 1}/{len(packages)})...")
        success, error = install(package)
        if not success:
            failed_packages.append( (package, error) )
            print(f"Failed to install {package}")
        else:
            print(f"Successfully installed {package}")
        #time.sleep(0.1)

    if failed_packages:
        print("\nThe following packages failed to install:")
        for package, error in failed_packages:
            print(f"{package}: {error}")
    else:
        print("\nAll packages installed successfully!")

if __name__ == "__main__":
    main()
