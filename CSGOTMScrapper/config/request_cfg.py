headers = {
    "sec-ch-ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                  "/118.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://market.csgo.com/en/",
    "app-settings": "lang=en",
    "sec-ch-ua-platform": '"Windows"',
}

json_data = {
    "operationName": "items",
    "variables": {
        "filters": [],
        "order": {
            "id": "popularity",
            "direction": "desc",
        },
        "page": 0,
        "count": 60,
    },
    "query": "query items($count: Int, $filters: [FilterInputType], $page: Int, $order: OrderInputType!) "
             "{\n  items(count: $count, filters: $filters, page: $page, order: $order) "
             "{\n    paginatorInfo {\n      count\n      currentPage\n      hasMorePages\n      lastPage\n      "
             "perPage\n      total\n      __typename\n    }\n    filters {\n      id\n      items {\n        "
             "color\n        enabled\n        id\n        name\n        value\n        image\n        __"
             "typename\n      }\n      max\n      min\n      name\n      order\n      type\n      value\n      __"
             "typename\n    }\n    meta {\n      title\n      description\n      __typename\n    }\n    "
             "data {\n      color\n      id\n      currency\n      stattrak\n      slot\n      popularity\n      "
             "features\n      rarity\n      rarity_ext {\n        id\n        name\n        __typename\n      }\n      "
             "ctp\n      quality\n      phase\n      descriptions {\n        type\n        value\n        __"
             "typename\n      }\n      type\n      tags {\n        category\n        category_name\n        "
             "localized_category_name\n        localized_tag_name\n        internal_name\n        name\n        "
             "value {\n          name\n          link\n          __typename\n        }\n        __"
             "typename\n      }\n      image_512\n      image_100\n      image_150\n      image_300\n      "
             "seo {\n        category\n        type\n        __typename\n      }\n      market_hash_name\n      "
             "market_name\n      price\n      stickers {\n        image\n        name\n        __"
             "typename\n      }\n      __typename\n    }\n    paginatorInfo {\n      count\n      currentPage\n      "
             "hasMorePages\n      lastPage\n      "
             "perPage\n      total\n      __typename\n    }\n    __typename\n  }\n}",
}
