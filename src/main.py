from src.cli import CLI
def main():
    file_path = 'tasks.json'
    cli = CLI(file_path)
    cli.run()

if __name__ == "__main__":
    main()
