<<<<<<< HEAD
#!/usr/bin/env python3
"""
VarLang Interpreter - Main Entry Point

Now expects source files with the .six extension.
"""

=======
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181
import sys
from interpreter import run_varlang

def main():
<<<<<<< HEAD
    """Main entry point for the VarLang interpreter"""
    
    if len(sys.argv) > 1:
        # Run from .six file
        filename = sys.argv[1]
        if not filename.endswith('.six'):
            print("ERROR: Please provide a .six file")
=======
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if not filename.endswith('.six'):
            print("Vro wyd: we need in the 6ix slide the .six file")
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181
            sys.exit(1)
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                code = file.read()
            run_varlang(code)
        except FileNotFoundError:
            print(f"ERROR: File '{filename}' not found")
            sys.exit(1)
        except Exception as e:
<<<<<<< HEAD
            print(f"ERROR: {e}")
            sys.exit(1)
    else:
        # Interactive mode
        print("VarLang Interpreter")
=======
            print(f"Broski fam: {e}")
            sys.exit(1)
    else:
        print("6ix Esolang Interpreter")
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181
        print("Type 'exit' to quit")
        print("-" * 30)
        
        while True:
            try:
                line = input("varlang> ")
                if line.strip().lower() == 'exit':
                    break
                if line.strip():
                    run_varlang(line)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

if __name__ == "__main__":
    main()