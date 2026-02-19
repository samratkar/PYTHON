#!/usr/bin/env python3
"""
Swiggy Food Delivery App
A CLI-based application to order food from Swiggy using MCP tools
"""

import os
import sys
from typing import List, Dict, Optional, Any
from dataclasses import dataclass
import json


@dataclass
class Address:
    """Represents a delivery address"""
    id: str
    label: str
    address: str
    area: str
    city: str


@dataclass
class Restaurant:
    """Represents a restaurant"""
    id: str
    name: str
    cuisine: str
    rating: float
    delivery_time: str
    cost_for_two: str


@dataclass
class MenuItem:
    """Represents a menu item"""
    id: str
    name: str
    price: float
    description: str
    is_veg: bool
    restaurant_id: str
    restaurant_name: str


class SwiggyFoodApp:
    """Main application class for Swiggy Food Delivery"""
    
    def __init__(self):
        self.current_address: Optional[Address] = None
        self.addresses: List[Address] = []
        self.cart_restaurant_id: Optional[str] = None
        self.cart_restaurant_name: Optional[str] = None
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def print_header(self, text: str):
        """Print a formatted header"""
        print("\n" + "=" * 80)
        print(f"  {text}")
        print("=" * 80 + "\n")
    
    def print_section(self, text: str):
        """Print a formatted section header"""
        print("\n" + "-" * 80)
        print(f"  {text}")
        print("-" * 80)
    
    def select_address(self) -> bool:
        """
        Fetch and allow user to select delivery address
        Returns True if address selected successfully
        """
        self.print_section("📍 Select Delivery Address")
        print("\nNote: This requires MCP tool 'mcp_swiggy-food_get_addresses' to be available")
        print("Please select an address from your saved Swiggy addresses.\n")
        
        print("MCP Tool Call: get_addresses")
        print("(In a real implementation, this would call the MCP tool)")
        
        # Placeholder for address selection
        address_id = input("\nEnter your address ID: ").strip()
        if address_id:
            self.current_address = Address(
                id=address_id,
                label="Home",
                address=f"Address {address_id}",
                area="",
                city=""
            )
            print(f"✅ Address selected: {address_id}")
            return True
        return False
    
    def search_restaurants(self, query: str):
        """Search for restaurants"""
        if not self.current_address:
            print("❌ Please select a delivery address first!")
            return
        
        self.print_section(f"🔍 Searching Restaurants: '{query}'")
        print(f"\nMCP Tool Call: search_restaurants")
        print(f"  - Query: {query}")
        print(f"  - Address ID: {self.current_address.id}")
        print("\n(In a real implementation, this would display search results)")
    
    def view_menu(self, restaurant_id: str):
        """View complete menu of a restaurant"""
        if not self.current_address:
            print("❌ Please select a delivery address first!")
            return
        
        self.print_section(f"📋 Restaurant Menu")
        print(f"\nMCP Tool Call: get_restaurant_menu")
        print(f"  - Restaurant ID: {restaurant_id}")
        print(f"  - Address ID: {self.current_address.id}")
        print("\n(In a real implementation, this would display the complete menu)")
    
    def search_menu_items(self, query: str, restaurant_id: Optional[str] = None):
        """Search for specific menu items"""
        if not self.current_address:
            print("❌ Please select a delivery address first!")
            return
        
        self.print_section(f"🔍 Searching Menu Items: '{query}'")
        print(f"\nMCP Tool Call: search_menu")
        print(f"  - Query: {query}")
        print(f"  - Address ID: {self.current_address.id}")
        if restaurant_id:
            print(f"  - Restaurant ID: {restaurant_id}")
        print("\n(In a real implementation, this would display matching menu items)")
    
    def add_to_cart(self, restaurant_id: str, menu_item_id: str, quantity: int = 1):
        """Add item to cart"""
        if not self.current_address:
            print("❌ Please select a delivery address first!")
            return
        
        self.print_section(f"🛒 Adding to Cart")
        print(f"\nMCP Tool Call: update_food_cart")
        print(f"  - Restaurant ID: {restaurant_id}")
        print(f"  - Menu Item ID: {menu_item_id}")
        print(f"  - Quantity: {quantity}")
        print(f"  - Address ID: {self.current_address.id}")
        print("\n✅ Item would be added to cart")
        
        self.cart_restaurant_id = restaurant_id
    
    def view_cart(self):
        """View current cart"""
        if not self.current_address:
            print("❌ Please select a delivery address first!")
            return
        
        self.print_section("🛒 Your Cart")
        print(f"\nMCP Tool Call: get_food_cart")
        print(f"  - Address ID: {self.current_address.id}")
        if self.cart_restaurant_name:
            print(f"  - Restaurant Name: {self.cart_restaurant_name}")
        print("\n(In a real implementation, this would display cart items, prices, and totals)")
    
    def fetch_coupons(self, restaurant_id: str):
        """Fetch available coupons"""
        if not self.current_address:
            print("❌ Please select a delivery address first!")
            return
        
        self.print_section("🎫 Available Coupons")
        print(f"\nMCP Tool Call: fetch_food_coupons")
        print(f"  - Restaurant ID: {restaurant_id}")
        print(f"  - Address ID: {self.current_address.id}")
        print("\n(In a real implementation, this would display available coupons and offers)")
    
    def apply_coupon(self, coupon_code: str):
        """Apply a coupon to cart"""
        if not self.current_address:
            print("❌ Please select a delivery address first!")
            return
        
        self.print_section("🎫 Applying Coupon")
        print(f"\nMCP Tool Call: apply_food_coupon")
        print(f"  - Coupon Code: {coupon_code}")
        print(f"  - Address ID: {self.current_address.id}")
        print("\n✅ Coupon would be applied to cart")
    
    def place_order(self):
        """Place the food order"""
        if not self.current_address:
            print("❌ Please select a delivery address first!")
            return
        
        self.print_section("🚨 Place Order")
        print("\n⚠️  IMPORTANT: Order placement requires explicit confirmation!")
        print("⚠️  Cart value must be less than ₹1000 (MCP beta restriction)")
        print(f"\nDelivery Address: {self.current_address.address}")
        
        confirm = input("\n❓ Do you want to proceed with placing this order? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            print(f"\nMCP Tool Call: place_food_order")
            print(f"  - Address ID: {self.current_address.id}")
            print("\n✅ Order would be placed!")
            print("🎉 In a real implementation: 'Swiggy order placed successfully!'")
        else:
            print("\n❌ Order cancelled")
    
    def track_orders(self):
        """Track active orders"""
        self.print_section("📦 Track Orders")
        print(f"\nMCP Tool Call: track_food_order")
        print("\n(In a real implementation, this would show active order tracking info)")
    
    def view_order_details(self, order_id: str):
        """View specific order details"""
        self.print_section(f"📦 Order Details: {order_id}")
        print(f"\nMCP Tool Call: get_food_order_details")
        print(f"  - Order ID: {order_id}")
        print("\n(In a real implementation, this would display complete order information)")
    
    def view_order_history(self):
        """View order history"""
        if not self.current_address:
            print("❌ Please select a delivery address first!")
            return
        
        self.print_section("📜 Order History")
        print(f"\nMCP Tool Call: get_food_orders")
        print(f"  - Address ID: {self.current_address.id}")
        print(f"  - Order Count: 5")
        print("\n(In a real implementation, this would display recent orders)")
    
    def clear_cart(self):
        """Clear/flush the cart"""
        self.print_section("🗑️ Clear Cart")
        confirm = input("\n❓ Are you sure you want to clear your cart? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            print(f"\nMCP Tool Call: flush_food_cart")
            print("\n✅ Cart would be cleared!")
            self.cart_restaurant_id = None
            self.cart_restaurant_name = None
        else:
            print("\n❌ Cart not cleared")
    
    def show_menu(self):
        """Display main menu"""
        self.print_header("🍔 Swiggy Food Delivery App")
        
        if self.current_address:
            print(f"📍 Current Address: {self.current_address.id}\n")
        else:
            print("📍 No address selected\n")
        
        print("1.  Select Delivery Address")
        print("2.  Search Restaurants")
        print("3.  View Restaurant Menu")
        print("4.  Search Menu Items")
        print("5.  Add Item to Cart")
        print("6.  View Cart")
        print("7.  Fetch Coupons")
        print("8.  Apply Coupon")
        print("9.  Place Order")
        print("10. Track Orders")
        print("11. View Order Details")
        print("12. View Order History")
        print("13. Clear Cart")
        print("0.  Exit")
        print("\n" + "=" * 80)
    
    def run(self):
        """Main application loop"""
        print("\n")
        print("╔════════════════════════════════════════════════════════════════════════════╗")
        print("║                    🍔 Swiggy Food Delivery App 🍔                         ║")
        print("║                                                                            ║")
        print("║  Built using Swiggy MCP (Model Context Protocol) Server                  ║")
        print("║  This is a demonstration app showing MCP tool integration                 ║")
        print("╚════════════════════════════════════════════════════════════════════════════╝")
        
        input("\n\nPress Enter to continue...")
        
        while True:
            self.clear_screen()
            self.show_menu()
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '0':
                print("\n👋 Thank you for using Swiggy Food Delivery App!")
                print("🍔 Happy eating!\n")
                sys.exit(0)
            
            elif choice == '1':
                self.select_address()
                input("\nPress Enter to continue...")
            
            elif choice == '2':
                query = input("\n🔍 Enter restaurant name or cuisine: ").strip()
                if query:
                    self.search_restaurants(query)
                input("\nPress Enter to continue...")
            
            elif choice == '3':
                restaurant_id = input("\n📋 Enter restaurant ID: ").strip()
                if restaurant_id:
                    self.view_menu(restaurant_id)
                input("\nPress Enter to continue...")
            
            elif choice == '4':
                query = input("\n🔍 Enter dish name: ").strip()
                restaurant_id = input("Enter restaurant ID (optional, press Enter to skip): ").strip()
                if query:
                    self.search_menu_items(query, restaurant_id if restaurant_id else None)
                input("\nPress Enter to continue...")
            
            elif choice == '5':
                restaurant_id = input("\n🏪 Enter restaurant ID: ").strip()
                menu_item_id = input("Enter menu item ID: ").strip()
                quantity = input("Enter quantity (default 1): ").strip()
                
                if restaurant_id and menu_item_id:
                    qty = int(quantity) if quantity.isdigit() else 1
                    self.add_to_cart(restaurant_id, menu_item_id, qty)
                input("\nPress Enter to continue...")
            
            elif choice == '6':
                self.view_cart()
                input("\nPress Enter to continue...")
            
            elif choice == '7':
                restaurant_id = input("\n🎫 Enter restaurant ID: ").strip()
                if restaurant_id:
                    self.fetch_coupons(restaurant_id)
                input("\nPress Enter to continue...")
            
            elif choice == '8':
                coupon_code = input("\n🎫 Enter coupon code: ").strip()
                if coupon_code:
                    self.apply_coupon(coupon_code)
                input("\nPress Enter to continue...")
            
            elif choice == '9':
                self.place_order()
                input("\nPress Enter to continue...")
            
            elif choice == '10':
                self.track_orders()
                input("\nPress Enter to continue...")
            
            elif choice == '11':
                order_id = input("\n📦 Enter order ID: ").strip()
                if order_id:
                    self.view_order_details(order_id)
                input("\nPress Enter to continue...")
            
            elif choice == '12':
                self.view_order_history()
                input("\nPress Enter to continue...")
            
            elif choice == '13':
                self.clear_cart()
                input("\nPress Enter to continue...")
            
            else:
                print("\n❌ Invalid choice! Please try again.")
                input("\nPress Enter to continue...")


def main():
    """Entry point"""
    try:
        app = SwiggyFoodApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
