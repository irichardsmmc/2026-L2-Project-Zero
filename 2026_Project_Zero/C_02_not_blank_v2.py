def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        product_name = input(question)

        if not any(c.isdigit() for c in product_name) and not any(c.isupper() for c in product_name) \
                and any(c.isalnum() for c in product_name):
            return product_name

        print("Sorry, this can't have capital letters, numbers, special characters, or be blank. Please try again.\n")


# main routine
who = not_blank("Please enter your name: ")
print(f"Hello {who}")
