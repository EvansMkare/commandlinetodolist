import argparse

FILENAME = "todo.txt"

def add_strikethrough(item):
    return f"\x1b[9m{item}x1b[0m"

def add_item(item):
    with open(FILENAME, "a") as file:
        file.write(f"{item}\n")
        file.close()
    print(f"Added item: {item}")
    
def list_item():
    lines = None
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: file '{FILENAME}' not found.")
        
    if not lines:
        print("No items found.")
    else:
        print(lines)
        for i, line in enumerate(lines):
            print(f"{i+1}. {line.strip()}")
            
def mark_items_done(item_number):
     with open(FILENAME, "r") as file:
            lines = file.readlines()
            
     if not lines:
        print("No items found.")
     elif item_number < 1 or item_number > len(lines):
        print("Invalid item number")
     else:
         #remove newline character which interrupts escape sequence
         item = lines[item_number-1].rstrip()
         item = add_strikethrough(item)
         with open(FILENAME, "w") as file:
              for i, line in enumerate(lines):
                  if i == item_number-1:
                      file.write(f"{item}\n")
                      print(f"Marked item as done: {item}")
                  else:
                      print(line)
                      file.write(line)
                      
                      
if __name__== "_main_":
    parser = argparse.ArgumentParser(description="Manage your to-do list")
    parser.add_argument("action", choices=["add", "list","done"], help="Action to perform")
    parser.add_argument("--item-text", help="Text of the item to add")
    parser.add_argument("--item-number",type=int, help="Number of the item to mark done")
    args = parser.parse_args()
    
    if args.action == "add":
        add_item(args.item_text)
    elif args.action == "done":
         mark_items_done(args.item_number)
    elif args.action == "list":
        list_item()