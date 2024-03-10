from rich.console import Console
from libs import pyess
from libs.APIs import hypixel
import math

console = Console()
skyblock = hypixel.Skyblock()

console.print("What is the Item ID of the item?", style="blue")
item_id = input("ID: ")

pyess.clear()

items = skyblock.get_items()

item_exists = False

for item in items:
    item_new_id = item["id"]
    if item_new_id == item_id:
        console.print("     Item Info     ", style="blue")
        console.print("-------------------", style="dark_blue")
        console.print(f"Item ID: {item_new_id}", style="blue")
        if item['name']:
            console.print(f"Name: {item['name']}", style="blue")
        if item['material']:
            console.print(f"Material: {item['material']}", style="blue")
        if item['npc_sell_price']:
            console.print(f"NPC Sell Price: {item['npc_sell_price']}", style="blue")

        bazaar_data = skyblock.get_bazaar()
        for product_id, product_info in bazaar_data.items():
            # Now product_id is the product ID and product_info is the information about that product
            if product_id == item_new_id:
                console.print("")
                console.print("     Bazaar Info     ", style="blue")
                console.print("---------------------", style="dark_blue")
                item_bazaar = product_info['quick_status']
                console.print(f"Real Selling Price: {round(item_bazaar['sellPrice'])}", style="blue")
                console.print(f"Real Buying Price: {round(item_bazaar['buyPrice'])}", style="blue")
                console.print(f"Sell Orders: {item_bazaar['sellOrders']}", style="blue")
                console.print(f"Buy Orders: {item_bazaar['buyOrders']}", style="blue")
        item_exists = True
    else:
        pass

if item_exists == False:
    console.print(f"Item ID {item_id} does not exist", style="red")

console.print("\nFinished", style="blue")