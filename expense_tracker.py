import csv
from datetime import date
import calendar

from expenses import Expense

def main():
    print("💖 Expense Tracker! ")
    expense_file="expense.csv"
    expense=get_user_expense()
    print(expense)
    
    save_expenses_to_file(expense,expense_file)
    budget=2000
    summarize_expenses(expense_file,budget)



def get_user_expense():
    
    expense_name=input("Enter the expense name")
    amount=float(input("Enter the cost of item"))
    print(f"You've successfully entered {expense_name}, {amount}")
    expense_cateorgies=[
        "🫕  Food",
        "🏡  Home",
        "🖥️  Work",
        "🎉  Fun",
        "✨  Misc"
    ]
    

    while True:
        print("Select a category")
        for i,category_name in enumerate(expense_cateorgies):
            print(f"  {i+1}. {category_name}")
        
        value_range=f"[1-{len(expense_cateorgies)}]"
        selected_i=int(input(f"Enter category number {value_range}"))-1

        if selected_i in range(len(expense_cateorgies)):
            selected_cat=expense_cateorgies[selected_i]
            new_expense=Expense(name=expense_name,category=selected_cat,price=amount)
            return new_expense
        
        else:
            print("Invalid category. Try Again! ")
        


def save_expenses_to_file(expense:Expense,expense_file):
    f=open(expense_file,"a",encoding="utf-8")
    f.write(f"{expense.name},{expense.price},{expense.category}\n")


    
def summarize_expenses(expense_file,budget):
    f=open(expense_file,encoding="utf-8")
    expenses:list[Expense]=[]
    lines=f.readlines()
    for line in lines:
        exp_name,exp_amt,exp_cat=line.strip().split(',')
        line_expense=Expense(name=exp_name,price=float(exp_amt),category=exp_cat)
        expenses.append(line_expense)
    

    amount_by_category={}
    for expense in expenses:
        key=expense.category
        if key in amount_by_category:
            amount_by_category[key]+=expense.price
        else:
              amount_by_category[key]=expense.price
    
    print("Expense by Category: ")

    for key,item in amount_by_category.items():
        print(key,": $",item)

    total_spent=sum([ex.price for ex in expenses])
    print("💵 Total Spent: $",total_spent)
    rem=budget-total_spent
    print("✅ Budget Remaining: $",rem)
    
    today = date.today()
    days_in_month = calendar.monthrange(today.year, today.month)[1]
    days_left = days_in_month - today.day
    
    Budget_per_day=rem/days_left
    print("👉 Budget Per Day: $")

if __name__=="__main__":
    main()
    
