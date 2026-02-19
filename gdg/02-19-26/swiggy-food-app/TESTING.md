# 🧪 Swiggy App Testing Guide

## Overview

This guide helps you test the Swiggy Food Delivery App with the MCP server.

## Prerequisites

1. **Swiggy MCP Server** must be configured in your MCP client (Claude Desktop)
2. **Valid Swiggy Account** with saved addresses
3. **Python 3.8+** installed

## Testing Checklist

### ✅ Initial Setup

- [ ] App launches successfully
- [ ] Welcome screen displays correctly
- [ ] Main menu shows all options

### ✅ Address Management

- [ ] Can fetch addresses from Swiggy account
- [ ] Can select a delivery address
- [ ] Selected address is displayed in menu

### ✅ Restaurant Discovery

- [ ] Restaurant search returns results
- [ ] Search works with different cuisines (Indian, Chinese, Italian, etc.)
- [ ] Can view restaurant details
- [ ] Can fetch restaurant menu

### ✅ Menu Search

- [ ] Can search for specific dishes
- [ ] Search works across all restaurants
- [ ] Can search within specific restaurant
- [ ] Results show dish details (name, price, veg/non-veg)

### ✅ Cart Operations

- [ ] Can add items to cart
- [ ] Can specify quantities
- [ ] Can view cart contents
- [ ] Cart shows correct prices and totals
- [ ] Can clear cart

### ✅ Coupons & Offers

- [ ] Can fetch available coupons
- [ ] Can apply coupon code
- [ ] Discount is reflected in cart total

### ✅ Order Placement

- [ ] Confirmation prompt appears
- [ ] Cart value validation (< ₹1000 for beta)
- [ ] Order placement succeeds
- [ ] Order ID is provided

### ✅ Order Tracking

- [ ] Can track active orders
- [ ] Order status updates correctly
- [ ] Can view order details
- [ ] Order history is accessible

## Test Scenarios

### Scenario 1: Complete Order Flow

1. Launch app
2. Select delivery address
3. Search for "pizza"
4. Select a restaurant
5. View menu
6. Add 2 items to cart
7. View cart
8. Fetch coupons
9. Apply a coupon
10. Place order
11. Track order

**Expected Result**: Order should be placed successfully and tracking should work

### Scenario 2: Cart Management

1. Add multiple items from same restaurant
2. Add items from different restaurant (should clear previous cart)
3. Update quantities
4. Clear cart
5. Verify cart is empty

**Expected Result**: Cart operations should work correctly

### Scenario 3: Search & Discovery

1. Search restaurants by cuisine
2. Search dishes across restaurants
3. Search dishes within a restaurant
4. View detailed menu

**Expected Result**: All search operations return relevant results

### Scenario 4: Error Handling

1. Try operations without selecting address
2. Enter invalid restaurant/item IDs
3. Cancel order placement
4. Try to place order > ₹1000

**Expected Result**: Appropriate error messages displayed

## Sample Test Data

### Restaurant Search Queries
- "biryani"
- "pizza"
- "chinese"
- "north indian"
- "dessert"

### Menu Item Searches
- "butter chicken"
- "paneer tikka"
- "margherita"
- "gulab jamun"

### Coupon Codes (Examples)
Test with codes from the fetch_coupons response

## Known Limitations (Beta)

⚠️ **Cart Value**: Must be < ₹1000
⚠️ **Address Required**: Most operations need address selection
⚠️ **Restaurant Restriction**: Can only have items from one restaurant in cart

## Debugging Tips

1. **Enable Verbose Logging**: Add print statements to see MCP tool responses
2. **Check Address ID**: Ensure valid address ID is selected
3. **Verify Restaurant ID**: Use search to get correct restaurant IDs
4. **Test Menu Item IDs**: Ensure menu item IDs match restaurant menu

## Reporting Issues

When reporting issues, include:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages (if any)
- MCP tool calls made
- Response received

## Success Criteria

The app is working correctly if:
- ✅ All MCP tools can be invoked
- ✅ Data is displayed correctly
- ✅ Cart operations work smoothly
- ✅ Orders can be placed
- ✅ Tracking works in real-time

---

**Happy Testing! 🧪🍔**
