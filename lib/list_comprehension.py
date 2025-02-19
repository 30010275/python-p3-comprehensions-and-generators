def return_evens(sequence):
    """Returns a list of even numbers from the given sequence."""
    return [num for num in sequence if num % 2 == 0]

def make_exclamation(sentences):
    """Appends an exclamation mark to each sentence in the given list."""
    return [sentence + "!" for sentence in sentences]

# Example test cases
if __name__ == "__main__":
    print(return_evens([0, 1, 3, 5, 7, 8, 9]))  # Output: [0, 8]
    print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
    # Output: ["Hello!", "I'm doing great!", "Python is fun!"]
