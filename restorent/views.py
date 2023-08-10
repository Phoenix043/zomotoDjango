from django.shortcuts import render
from django.http import JsonResponse

# Dummy data for demonstration
menu_items = [
    {"id": 1, "name": "Burger", "price": 10.99},
    {"id": 2, "name": "Pizza", "price": 12.99},
    # ... more menu items
]

orders = []
order_counter = 1

def add_item_to_menu(request):
    if request.method == "POST":
        data = request.POST  # Replace with your form handling logic
        new_item = {"id": len(menu_items) + 1, "name": data["name"], "price": float(data["price"])}
        menu_items.append(new_item)
        return JsonResponse({"message": "Item added to menu successfully"})
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
        return JsonResponse({"message": "Order placed successfully"})
    return render(request, "order.html", {"menu_items": menu_items})

def update_order_status(request, order_id):
    if request.method == "POST":
        data = request.POST  # Replace with your form handling logic
        for order in orders:
            if order["id"] == int(order_id):
                order["status"] = data["status"]
                return JsonResponse({"message": f"Order {order_id} status updated"})
    return render(request, "update.html", {"order_id": order_id})

def view_all_orders(request):
    return render(request, "view_order.html", {"orders": orders})
