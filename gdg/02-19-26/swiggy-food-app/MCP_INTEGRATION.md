# 📚 MCP Integration Guide

## Understanding MCP Tools

The Swiggy Food Delivery App uses MCP (Model Context Protocol) tools to interact with Swiggy's services. This guide explains how these tools work and how to integrate them.

## Architecture

```
┌─────────────────┐
│   Swiggy App    │ (Python CLI)
│  (swiggy_app.py)│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   MCP Client    │ (Claude Desktop / MCP Host)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Swiggy MCP      │ (MCP Server)
│    Server       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Swiggy API    │ (Swiggy Backend)
└─────────────────┘
```

## Available MCP Tools

### 1. Address Management

#### `mcp_swiggy-food_get_addresses`
**Purpose**: Fetch all saved delivery addresses

**Request**: No parameters required

**Response**:
```json
{
  "addresses": [
    {
      "id": "12345",
      "label": "Home",
      "address": "123 Main Street",
      "area": "Downtown",
      "city": "Bangalore",
      "lat": 12.9716,
      "lng": 77.5946
    }
  ]
}
```

### 2. Restaurant Discovery

#### `mcp_swiggy-food_search_restaurants`
**Purpose**: Search for restaurants

**Request**:
```json
{
  "query": "pizza",
  "address_id": "12345"
}
```

**Response**:
```json
{
  "restaurants": [
    {
      "id": "rest123",
      "name": "Pizza Hut",
      "cuisine": "Pizza, Italian",
      "rating": 4.2,
      "delivery_time": "30-35 mins",
      "cost_for_two": "₹400"
    }
  ]
}
```

#### `mcp_swiggy-food_get_restaurant_menu`
**Purpose**: Get complete menu of a restaurant

**Request**:
```json
{
  "restaurant_id": "rest123",
  "address_id": "12345"
}
```

**Response**:
```json
{
  "restaurant_name": "Pizza Hut",
  "menu": [
    {
      "category": "Pizzas",
      "items": [
        {
          "id": "item456",
          "name": "Margherita",
          "price": 299,
          "description": "Classic cheese pizza",
          "is_veg": true,
          "in_stock": true
        }
      ]
    }
  ]
}
```

### 3. Menu Search

#### `mcp_swiggy-food_search_menu`
**Purpose**: Search for specific dishes

**Request**:
```json
{
  "query": "butter chicken",
  "address_id": "12345",
  "restaurant_id": "rest123"  // Optional
}
```

**Response**:
```json
{
  "items": [
    {
      "id": "item789",
      "name": "Butter Chicken",
      "restaurant_id": "rest456",
      "restaurant_name": "Taj Restaurant",
      "price": 350,
      "description": "Creamy tomato curry",
      "is_veg": false
    }
  ]
}
```

### 4. Cart Management

#### `mcp_swiggy-food_update_food_cart`
**Purpose**: Add or update items in cart

**Request**:
```json
{
  "restaurant_id": "rest123",
  "menu_item_id": "item456",
  "quantity": 2,
  "address_id": "12345"
}
```

**Response**:
```json
{
  "success": true,
  "cart_total": 598,
  "message": "Item added to cart"
}
```

#### `mcp_swiggy-food_get_food_cart`
**Purpose**: View current cart

**Request**:
```json
{
  "address_id": "12345"
}
```

**Response**:
```json
{
  "restaurant_name": "Pizza Hut",
  "items": [
    {
      "name": "Margherita",
      "quantity": 2,
      "price": 299,
      "total": 598
    }
  ],
  "subtotal": 598,
  "taxes": 59.8,
  "delivery_fee": 40,
  "total": 697.8
}
```

#### `mcp_swiggy-food_flush_food_cart`
**Purpose**: Clear the cart

**Request**: No parameters

**Response**:
```json
{
  "success": true,
  "message": "Cart cleared"
}
```

### 5. Coupons & Offers

#### `mcp_swiggy-food_fetch_food_coupons`
**Purpose**: Get available coupons

**Request**:
```json
{
  "restaurant_id": "rest123",
  "address_id": "12345"
}
```

**Response**:
```json
{
  "coupons": [
    {
      "code": "SAVE50",
      "description": "Flat ₹50 off on orders above ₹299",
      "discount": 50,
      "min_order_value": 299
    }
  ]
}
```

#### `mcp_swiggy-food_apply_food_coupon`
**Purpose**: Apply coupon to cart

**Request**:
```json
{
  "coupon_code": "SAVE50",
  "address_id": "12345"
}
```

**Response**:
```json
{
  "success": true,
  "discount": 50,
  "new_total": 647.8,
  "message": "Coupon applied successfully"
}
```

### 6. Order Management

#### `mcp_swiggy-food_place_food_order`
**Purpose**: Place the order

**Request**:
```json
{
  "address_id": "12345"
}
```

**Response**:
```json
{
  "success": true,
  "order_id": "ORDER123456",
  "estimated_delivery": "30-35 mins",
  "total": 647.8
}
```

#### `mcp_swiggy-food_track_food_order`
**Purpose**: Track active orders

**Request**: No parameters

**Response**:
```json
{
  "active_orders": [
    {
      "order_id": "ORDER123456",
      "status": "PREPARING",
      "restaurant": "Pizza Hut",
      "estimated_time": "25 mins"
    }
  ]
}
```

#### `mcp_swiggy-food_get_food_order_details`
**Purpose**: Get specific order details

**Request**:
```json
{
  "order_id": "ORDER123456"
}
```

**Response**:
```json
{
  "order_id": "ORDER123456",
  "status": "DELIVERED",
  "restaurant": "Pizza Hut",
  "items": [
    {
      "name": "Margherita",
      "quantity": 2,
      "price": 598
    }
  ],
  "total": 647.8,
  "placed_at": "2026-02-19T14:30:00Z",
  "delivered_at": "2026-02-19T15:05:00Z"
}
```

#### `mcp_swiggy-food_get_food_orders`
**Purpose**: Get order history

**Request**:
```json
{
  "address_id": "12345",
  "count": 5
}
```

**Response**:
```json
{
  "orders": [
    {
      "order_id": "ORDER123456",
      "restaurant": "Pizza Hut",
      "total": 647.8,
      "status": "DELIVERED",
      "placed_at": "2026-02-19T14:30:00Z"
    }
  ]
}
```

## Integration Patterns

### Pattern 1: Simple Tool Call

```python
# In Claude Desktop or MCP client context
result = await mcp_swiggy_food_get_addresses()
addresses = result['addresses']
```

### Pattern 2: Chained Operations

```python
# 1. Get addresses
addresses = await mcp_swiggy_food_get_addresses()
address_id = addresses[0]['id']

# 2. Search restaurants
restaurants = await mcp_swiggy_food_search_restaurants(
    query="pizza",
    address_id=address_id
)

# 3. Get menu
menu = await mcp_swiggy_food_get_restaurant_menu(
    restaurant_id=restaurants[0]['id'],
    address_id=address_id
)
```

### Pattern 3: Error Handling

```python
try:
    result = await mcp_swiggy_food_place_food_order(
        address_id=address_id
    )
    if result['success']:
        print(f"Order placed: {result['order_id']}")
except Exception as e:
    print(f"Order failed: {e}")
```

## Best Practices

1. **Always Select Address First**: Most operations require a valid address_id
2. **Cache Restaurant IDs**: Store restaurant IDs for frequently ordered places
3. **Validate Cart Value**: Ensure cart < ₹1000 for beta
4. **Confirmation for Orders**: Always confirm before placing orders
5. **Handle Errors Gracefully**: MCP calls can fail, implement retry logic
6. **Track Order States**: Poll tracking API for status updates

## Limitations (Beta)

- ⚠️ **Cart Value**: Maximum ₹1000 per order
- ⚠️ **Single Restaurant**: Cart can only contain items from one restaurant
- ⚠️ **Address Required**: Most operations need address_id
- ⚠️ **Rate Limiting**: May apply to frequent API calls

## Security Considerations

1. **Never Log Credentials**: MCP server handles authentication
2. **Validate Inputs**: Sanitize user inputs before MCP calls
3. **Confirm Payments**: Always require explicit confirmation
4. **Secure Storage**: Don't store sensitive order data locally

## Extending the App

### Add Restaurant Favorites

```python
def save_favorite_restaurant(restaurant_id: str, name: str):
    # Load config
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    # Add to favorites
    config['favorites']['restaurants'].append({
        'id': restaurant_id,
        'name': name
    })
    
    # Save config
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=2)
```

### Add Order Scheduling

```python
async def schedule_order(order_time: str):
    # Wait until order time
    # Then call place_food_order
    pass
```

### Add Price Alerts

```python
async def check_offers(restaurant_id: str):
    coupons = await mcp_swiggy_food_fetch_food_coupons(
        restaurant_id=restaurant_id,
        address_id=current_address_id
    )
    
    # Check for good offers
    for coupon in coupons['coupons']:
        if coupon['discount'] > 100:
            notify_user(f"Great offer: {coupon['code']}")
```

## Troubleshooting

### Issue: "Address not found"
**Solution**: Ensure you've selected a valid address using get_addresses

### Issue: "Restaurant not available"
**Solution**: Check if restaurant delivers to your address

### Issue: "Cart value exceeds limit"
**Solution**: Keep cart under ₹1000 for beta

### Issue: "MCP tool not found"
**Solution**: Ensure Swiggy MCP server is configured in Claude Desktop

---

**For more information, consult the Swiggy MCP Server documentation**
