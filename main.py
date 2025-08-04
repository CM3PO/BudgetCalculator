from colorama import Fore, Style, init
init(autoreset=True)  # Automatically reset color after each print

def print_header(title):
    print("\n" + "=" * 30)
    print(f"{title:^30}")  # Title centered with a fixed width
    print("=" * 30)

def budget_calculator():
    """
    Budget calculator that:
    1. Asks for monthly income
    2. Asks for various expense categories
    3. Calculates remaining money
    4. Shows percentage spent in each category
    5. Gives budget advice based on remaining amount
    """
    print_header("BUDGET CALCULATOR")
    
    # Step 1: Get monthly income
    income = float(input("Enter your monthly income: $"))
    
    # Step 2: Get expenses
    expenses = {}
    total_expenses = 0
    
    while True:
        # Ask for expense category
        category = input("Enter an expense category (or 'done' to finish): ").strip()
        
        if category.lower() == 'done':
            break
        
        # Ask for expense amount
        amount = float(input(f"Enter the amount for {category}: $"))
        
        # Store in dictionary
        expenses[category] = amount
        total_expenses += amount
    
    # Step 3: Calculate remaining money
    remaining_money = income - total_expenses
    
    # Step 4: Show percentage spent in each category
    print_header("EXPENSE BREAKDOWN")
    for category, amount in expenses.items():
        percentage = (amount / income) * 100
        print(f"{category:<20}: ${amount:,.2f} ({percentage:5.2f}%)")
    
    # Step 5: Give budget advice
    print_header("BUDGET ADVICE")
    if remaining_money > 0:
        print(Fore.GREEN + f"Great job! You have ${remaining_money:,.2f} left over this month.")
    elif remaining_money == 0:
        print(Fore.YELLOW + "You're breaking even this month. Try to save a little next month!")
    else:
        print(Fore.RED + f"You're overspending! You need to cut back by ${-remaining_money:,.2f}.")

# Run the program
budget_calculator()
