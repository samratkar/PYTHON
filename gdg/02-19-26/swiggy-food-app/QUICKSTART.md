# 🚀 Quick Start Guide

Get started with the Swiggy Food Delivery App in 5 minutes!

## ⚡ Fastest Way to Start

```bash
cd /Users/samrat.kar/git/fda/swiggy-food-app
./run.sh
```

That's it! The script will set up everything automatically.

## 📱 Alternative: Manual Start

```bash
cd /Users/samrat.kar/git/fda/swiggy-food-app
python3 swiggy_app.py
```

## 🎯 Your First Order - 3 Minutes

1. **Launch the app**
   ```bash
   ./run.sh
   ```

2. **Select address** (Option 1)
   - Enter your Swiggy address ID

3. **Search restaurant** (Option 2)
   - Try: "biryani", "pizza", or "chinese"

4. **Browse menu** (Option 3)
   - Enter the restaurant ID from search results

5. **Add to cart** (Option 5)
   - Enter restaurant ID and menu item ID

6. **Place order** (Option 9)
   - Confirm and order!

## 🎬 See It In Action

Run the demo to see the complete workflow:

```bash
./demo.py
```

This shows how all MCP tools work together for a complete order.

## 📚 Learn More

- **Full Documentation**: See [README.md](README.md)
- **MCP Integration**: See [MCP_INTEGRATION.md](MCP_INTEGRATION.md)
- **Testing Guide**: See [TESTING.md](TESTING.md)

## 🆘 Quick Troubleshooting

### App won't start?
```bash
# Check Python version (need 3.8+)
python3 --version

# Try manual start
python3 swiggy_app.py
```

### "MCP tool not found"?
- Ensure Swiggy MCP server is configured in Claude Desktop
- Check MCP server is running

### "Address not found"?
- Make sure you have addresses saved in your Swiggy account
- Use a valid address ID from your account

## 💡 Pro Tips

1. **Save Favorites**: Keep restaurant IDs handy for quick ordering
2. **Check Coupons First**: Always fetch coupons before placing order
3. **Cart Limit**: Keep orders under ₹1000 (beta restriction)
4. **Track in Real-time**: Use option 10 to track delivery

## 🎉 What's Next?

After your first order:
- ✅ Explore order history (Option 12)
- ✅ Try different cuisines
- ✅ Save your favorite restaurants
- ✅ Experiment with coupons to maximize savings!

---

**Need help? Check the full README or run the demo!**

**Happy Ordering! 🍕🍔🍜**
