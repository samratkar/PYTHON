# 🍔 Swiggy Food Delivery App

A CLI-based food ordering application built using the **Swiggy MCP (Model Context Protocol) Server**. This app demonstrates how to integrate with Swiggy's food delivery services through MCP tools.

## 🌟 Features

This app provides a complete food ordering workflow:

### 🏠 Address Management
- Select and manage delivery addresses
- View saved addresses from your Swiggy account

### 🔍 Discovery
- **Search Restaurants**: Find restaurants by name, cuisine, or location
- **Search Menu Items**: Search for specific dishes across restaurants or within a specific restaurant
- **View Restaurant Menu**: Browse complete menu with dishes, prices, and details

### 🛒 Cart Management
- **Add Items to Cart**: Add dishes with specified quantities
- **View Cart**: See all items, prices, taxes, and total
- **Update Cart**: Modify quantities or remove items
- **Clear Cart**: Empty the cart completely

### 🎫 Offers & Discounts
- **Fetch Coupons**: View available coupons and offers
- **Apply Coupons**: Apply discount codes to your order

### 📦 Order Management
- **Place Order**: Complete the checkout and place your food order
- **Track Orders**: Monitor active order status in real-time
- **View Order Details**: See complete details of any specific order
- **Order History**: Browse your past orders

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Access to Swiggy MCP Server (configured in your Claude Desktop or MCP client)
- Valid Swiggy account with saved addresses

### Installation

1. **Clone or navigate to the app directory:**
   ```bash
   cd /Users/samrat.kar/git/fda/swiggy-food-app
   ```

2. **Make the app executable (optional):**
   ```bash
   chmod +x swiggy_app.py
   ```

3. **Run the app:**
   ```bash
   python3 swiggy_app.py
   ```

## 📖 Usage Guide

### Main Menu

When you launch the app, you'll see the main menu with the following options:

```
1.  Select Delivery Address
2.  Search Restaurants
3.  View Restaurant Menu
4.  Search Menu Items
5.  Add Item to Cart
6.  View Cart
7.  Fetch Coupons
8.  Apply Coupon
9.  Place Order
10. Track Orders
11. View Order Details
12. View Order History
13. Clear Cart
0.  Exit
```

### Typical Ordering Workflow

1. **Select Address** (Option 1)
   - Choose your delivery address from saved addresses

2. **Find Food** (Options 2, 3, or 4)
   - Search for restaurants or specific dishes
   - Browse restaurant menus

3. **Build Your Cart** (Option 5)
   - Add items by providing restaurant ID and menu item ID
   - Specify quantities

4. **Review Cart** (Option 6)
   - Check items, quantities, and prices
   - View total amount

5. **Apply Offers** (Options 7 & 8)
   - View available coupons
   - Apply discount codes

6. **Place Order** (Option 9)
   - Review final order
   - Confirm and place order

7. **Track Delivery** (Option 10)
   - Monitor order status
   - View estimated delivery time

## 🔧 MCP Tools Used

This app integrates with the following Swiggy MCP tools:

| Tool | Purpose |
|------|---------|
| `mcp_swiggy-food_get_addresses` | Fetch saved delivery addresses |
| `mcp_swiggy-food_search_restaurants` | Search for restaurants |
| `mcp_swiggy-food_get_restaurant_menu` | Get complete restaurant menu |
| `mcp_swiggy-food_search_menu` | Search menu items |
| `mcp_swiggy-food_update_food_cart` | Add/update items in cart |
| `mcp_swiggy-food_get_food_cart` | View current cart |
| `mcp_swiggy-food_fetch_food_coupons` | Get available coupons |
| `mcp_swiggy-food_apply_food_coupon` | Apply coupon code |
| `mcp_swiggy-food_place_food_order` | Place the order |
| `mcp_swiggy-food_track_food_order` | Track active orders |
| `mcp_swiggy-food_get_food_order_details` | Get specific order details |
| `mcp_swiggy-food_get_food_orders` | View order history |
| `mcp_swiggy-food_flush_food_cart` | Clear the cart |

## ⚠️ Important Notes

### MCP Beta Restrictions

- **Order Value Limit**: Cart value must be less than ₹1000 (beta restriction)
- **Confirmation Required**: Order placement requires explicit user confirmation
- **Address Required**: Most operations require a valid delivery address to be selected

### Data Requirements

- **Restaurant ID**: Required for menu viewing and adding items to cart
- **Menu Item ID**: Required for adding items to cart
- **Order ID**: Required for viewing order details

### Error Handling

The app includes basic error handling for:
- Missing delivery address
- Invalid input values
- User cancellation of critical operations

## 🎨 Features & Design

### User Experience
- Clear, intuitive CLI interface
- Color-coded sections and headers
- Confirmation prompts for critical actions
- Status indicators (✅, ❌, 📍, 🛒, etc.)

### Code Structure
- Object-oriented design with `SwiggyFoodApp` class
- Dataclasses for type-safe data structures (`Address`, `Restaurant`, `MenuItem`)
- Modular methods for each operation
- Clean separation of concerns

## 🔮 Future Enhancements

Potential improvements for the app:

1. **Rich UI**: Use libraries like `rich` or `textual` for enhanced CLI experience
2. **Configuration File**: Store user preferences and default settings
3. **Favorites**: Save favorite restaurants and dishes
4. **Scheduling**: Schedule orders for later delivery
5. **Dietary Filters**: Filter by veg/non-veg, cuisines, etc.
6. **Price Alerts**: Notify when favorite items have offers
7. **Web Interface**: Build a web-based UI using Flask/FastAPI
8. **Multi-user**: Support multiple user profiles

## 📝 License

This is a demonstration application built for educational purposes.

## 🤝 Contributing

This app is part of the FDA project workspace. For contributions or improvements:

1. Follow the project's coding standards
2. Test thoroughly before committing
3. Update documentation as needed

## 📞 Support

For issues or questions:
- Check the MCP tool documentation
- Review Swiggy API restrictions
- Ensure your Swiggy account is properly configured

## 🙏 Credits

Built using:
- **Swiggy MCP Server**: Food delivery integration
- **MCP (Model Context Protocol)**: Tool invocation framework
- **Python**: Application logic

---

**Happy Ordering! 🍕🍔🍜**
