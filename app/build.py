import argparse
import subprocess

def run():
    parser = argparse.ArgumentParser(description="dev mode")
    parser.add_argument("--dev", default="false", help="Dev mode")
    args = parser.parse_args()
    dev_arg = "--noconsole" if args.dev == 'false' else ""
    subprocess.run(f'pyinstaller {dev_arg} --icon=favicon.ico ./app/main.py', shell=True)


if __name__ == "__main__":
    run()