def manage_queue(queue, action, person):
    """
    Manage a queue of people.
    """
    if action == "add_end":
        queue.append(person)
        return f"{person} added to end"
    elif action == "add_front":
        queue.insert(0, person)
        return f"{person} added to front"
    elif action == "serve":
        if len(queue) == 0:
            return None
        served_person = queue.pop(0)
        return f"Served: {served_person}"
    
if __name__ == "__main__":
    queue = ["Alice", "Bob"]
    result = manage_queue(queue, "add_end", "Charlie")
    print(f"Test 3.1: {'✅ PASS' if result == 'Charlie added to end' and queue == ['Alice', 'Bob', 'Charlie'] else '❌ FAIL'}")
    print(f"  Expected: 'Charlie added to end', ['Alice', 'Bob', 'Charlie']")
    print(f"  Got: '{result}', {queue}")
