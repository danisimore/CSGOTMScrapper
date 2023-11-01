import json
from json import JSONDecodeError

import requests
from config.request_cfg import headers, json_data

from config import data_lists


def generate_lists():
    items_data = "It's not None!"

    page_counter = 0

    while items_data:
        print(f"[INFO] Scrapper is working! Parsing {page_counter} page!")

        json_data["variables"]["page"] = page_counter
        page_counter += 1

        try:
            response = requests.post(
                url="https://market.csgo.com/api/graphql",
                headers=headers,
                json=json_data,
            ).json()
        except JSONDecodeError:
            break

        items_data = response.get("data").get("items").get("data")

        if items_data:
            for item in items_data:
                item_category = item.get("seo").get("category")

                if item_category == "Pistol":
                    data_lists.pistol_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "quality": item.get("quality"),
                            "rarity": item.get("rarity"),
                        }
                    )

                elif item_category == "SMG":
                    data_lists.smg_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "quality": item.get("quality"),
                            "rarity": item.get("rarity"),
                        }
                    )
                elif item_category == "Key":
                    data_lists.key_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "rarity": item.get("rarity"),
                        }
                    )
                elif item_category == "Gift":
                    data_lists.gift_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "rarity": item.get("rarity"),
                        }
                    )
                elif item_category == "Sniper Rifle":
                    data_lists.sniper_rifle_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "quality": item.get("quality"),
                            "rarity": item.get("rarity"),
                        }
                    )
                elif item_category == "Collectible":
                    data_lists.collectable_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "rarity": item.get("rarity"),
                        }
                    )
                elif item_category == "Pass":
                    data_lists.pass_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "rarity": item.get("rarity"),
                        }
                    )
                elif item_category == "Knife":
                    data_lists.knife_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "quality": item.get("quality"),
                            "rarity": item.get("rarity"),
                        }
                    )
                elif item_category == "Rifle":
                    data_lists.rifle_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "quality": item.get("quality"),
                            "rarity": item.get("rarity"),
                        }
                    )
                elif item_category == "Container":
                    data_lists.container_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "rarity": item.get("rarity"),
                        }
                    )
                elif item_category == "Sticker":
                    data_lists.sticker_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "rarity": item.get("rarity"),
                        }
                    )
                elif item_category == "Gloves":
                    data_lists.gloves_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "quality": item.get("quality"),
                            "rarity": item.get("rarity"),
                        }
                    )
                elif item_category == "Shotgun":
                    data_lists.shotgun_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "quality": item.get("quality"),
                            "rarity": item.get("rarity"),
                        }
                    )
                elif item_category == "Music Kit":
                    data_lists.music_kit_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "rarity": item.get("rarity"),
                        }
                    )
                elif item_category == "Agent":
                    data_lists.agent_list.append(
                        {
                            "name": item.get("market_hash_name"),
                            "price": item.get("price"),
                            "currency": item.get("currency"),
                            "popularity": item.get("popularity"),
                            "rarity": item.get("rarity"),
                        }
                    )


def record_files():
    print(
        "[INFO] A data from the pages has been successfully collected! Begin recording the data in files!"
    )

    with open("data/pistols_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.pistol_list, file, indent=4, ensure_ascii=False)

    with open("data/smg_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.smg_list, file, indent=4, ensure_ascii=False)

    with open("data/key_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.key_list, file, indent=4, ensure_ascii=False)

    with open("data/gift_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.gift_list, file, indent=4, ensure_ascii=False)

    with open("data/sniper_rifle_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.sniper_rifle_list, file, indent=4, ensure_ascii=False)

    with open("data/collectable_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.collectable_list, file, indent=4, ensure_ascii=False)

    with open("data/pass_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.pass_list, file, indent=4, ensure_ascii=False)

    with open("data/knife_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.knife_list, file, indent=4, ensure_ascii=False)

    with open("data/rifle_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.rifle_list, file, indent=4, ensure_ascii=False)

    with open("data/container_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.container_list, file, indent=4, ensure_ascii=False)

    with open("data/sticker_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.sticker_list, file, indent=4, ensure_ascii=False)

    with open("data/gloves_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.gloves_list, file, indent=4, ensure_ascii=False)

    with open("data/shotgun_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.shotgun_list, file, indent=4, ensure_ascii=False)

    with open("data/music_kit_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.music_kit_list, file, indent=4, ensure_ascii=False)

    with open("data/agent_data.json", "w", encoding="utf-8") as file:
        json.dump(data_lists.agent_list, file, indent=4, ensure_ascii=False)

    print("[INFO] Scrapper successfully completed the work!")
