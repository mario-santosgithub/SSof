import sys
import ast
import json

def main():

    # Receives two arguments
    # - Python file containing the program to be analysed
    # - Name of the JSON file containing the list of vulnerability patterns

    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        print("Usage: python3 file vulnerabilities")
        sys.exit(1)

    pythonFile = sys.argv[1]
    vulFile = sys.argv[2]
    outputFile = "./output/" + pythonFile[:-3] + ".output.json"


    # verify the types of the files
    if pythonFile[-3:] != ".py":
        print("First argument should be a python file")
        sys.exit(1)
    if vulFile[-13:] != "patterns.json":
        print("Second argument should be a JSON file")
        sys.exit(1)

    python_content = None
    vul_content = None
    # try to open the files while checking if they exists
    try:
        with open(pythonFile, 'r') as file:
            python_content = file.read()
    except FileNotFoundError:
        print(f"The file '{pythonFile}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        with open(vulFile, 'r') as file:
            vul_content = json.load(file)
    except FileNotFoundError:
        print(f"The file '{vulFile}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    
    ast_tree = ast.parse(python_content)
    ast_json = json.loads(json.dumps(ast_tree, default=lambda x: x.__dict__))

    vulnerabilities = None
    if (len(vul_content) == 0):
        vulnerabilities = []


    with open(outputFile, "w", encoding="utf-8") as outfile:
        json.dump(vulnerabilities, outfile, indent=1)

    sys.exit(1)

if __name__ == "__main__":
    main()