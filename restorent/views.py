from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages


# Dummy data for demonstration
menu_items = [
    {"id": 1, "name": "Burger", "price": 10.99, "Desc": "Try once", "availability": True, "quantity": 10},
    {"id": 2, "name": "Pizza", "price": 12.99, "Desc": "Try once", "availability": True, "quantity": 15},
    # ... more menu items
]


orders = []
order_counter = 1

def add_item_to_menu(request):
    if request.method == "POST":
        data = request.POST  # Replace with your form handling logic
        new_item = {"id": len(menu_items) + 1, "name": data["name"], "price": float(data["price"]),'Desc':data['Desc']}
        menu_items.append(new_item)
        messages.success(request, "Item added to menu successfully")
    return render(request, "add.html")

def show_menu(request):
    return render(request, "menu.html", {"menu_items": menu_items})

def order_item(request):
    global order_counter
    if request.method == "POST":
        data = request.POST  # Replace with your form handling logic
        order = {
            "id": order_counter,
            "item_id": int(data["item_id"]),
            "quantity": int(data["quantity"]),
            "status": "Pending"
        }
        orders.append(order)
        order_counter += 1
        messages.success(request, "Order placed successfully")
    return render(request, "order.html", {"menu_items": menu_items})

def update_order_status(request, order_id):
    if request.method == "POST":
        data = request.POST  # Replace with your form handling logic
        for order in orders:
            if order["id"] == int(order_id):
                order["status"] = data["status"]
                messages.success(request, f"Order {order_id} status updated")
    return render(request, "update.html", {"order_id": order_id})

def view_all_orders(request):
    return render(request, "view_order.html", {"orders": orders})


def edit_item(request, item_id):
    if request.method == "POST":
        data = request.POST  # Replace with your form handling logic
        for item in menu_items:
            if item["id"] == int(item_id):
                item["name"] = data["name"]
                item["price"] = float(data["price"])
                item["availability"] = bool(data["availability"])  # Assuming you have an availability checkbox
                item["quantity"] = int(data["quantity"])
                messages.success(request, f"Item {item_id} edited successfully")
    for item in menu_items:
        if item["id"] == int(item_id):
            return render(request, "edit_item.html", {"item": item})
    messages.success(request, "Item not found")


def remove_item(request, item_id):
    global menu_items
    menu_items = [item for item in menu_items if item["id"] != int(item_id)]
    messages.success(request, f"Item {item_id} removed successfully")
    return redirect('zomotoApp:show_menu')