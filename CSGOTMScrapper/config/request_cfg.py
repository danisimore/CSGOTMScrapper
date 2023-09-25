cookies = {
        '_ga': 'GA1.1.1328123598.1694624978',
        '_ga': 'GA1.3.1328123598.1694624978',
        '_ym_uid': '1694624979612010922',
        '_ym_d': '1694624979',
        'd2mid': 'Uh6cWyiRPjq0Fic8GyPF5LbkEjIkvL',
        'PHPSESSID': '226406474%3A26c78d19833607a4c17d64d3c2033d52',
        '_csrf': 'cUrrbXNxpf_M4vcTdjujhcjbvdK_wA_c',
        '_gid': 'GA1.3.1466090836.1695398943',
        '_ym_isad': '1',
        '_ga_DP1T9TKX7Z': 'GS1.3.1695665237.15.0.1695665237.60.0.0',
        '_ga_TEWB4TCDHF': 'GS1.1.1695665169.19.1.1695665566.0.0.0',
    }

headers = {
    'authority': 'market.csgo.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'app-settings': 'lang=ru; currency=RUB',
    'content-type': 'application/json',
    'origin': 'https://market.csgo.com',
    'referer': 'https://market.csgo.com/ru/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

json_data = {
    'operationName': 'items',
    'variables': {
        'filters': [],
        'order': {
            'id': 'popularity',
            'direction': 'desc',
        },
        'page': 0,
        'count': 100,
    },
    'query': 'query items($count: Int, $filters: [FilterInputType], $page: Int, $order: OrderInputType!) '
             '{\n  items(count: $count, filters: $filters, page: $page, order: $order) '
             '{\n    paginatorInfo {\n      count\n      currentPage\n      hasMorePages\n      lastPage\n      '
             'perPage\n      total\n      __typename\n    }\n    filters {\n      id\n      items {\n        '
             'color\n        enabled\n        id\n        name\n        value\n        image\n        '
             '__typename\n      }\n      max\n      min\n      name\n      order\n      type\n      value\n      '
             '__typename\n    }\n    meta {\n      title\n      description\n      __typename\n    }\n    '
             'data {\n      color\n      id\n      currency\n      stattrak\n      slot\n      popularity\n      '
             'features\n      rarity\n      rarity_ext '
             '{\n        id\n        name\n        __typename\n      }\n      '
             'ctp\n      quality\n      phase\n      descriptions {\n        type\n        value\n        '
             '__typename\n      }\n      type\n      tags {\n        category\n        category_name\n        '
             'localized_category_name\n        localized_tag_name\n        internal_name\n        name\n        '
             'value {\n          name\n          link\n          __typename\n        }\n        '
             '__typename\n      }\n      image_512\n      image_100\n      image_150\n      image_300\n      '
             'seo {\n        category\n        type\n        __typename\n      }\n      market_hash_name\n      '
             'market_name\n      price\n      stickers {\n        image\n        name\n        '
             '__typename\n      }\n      __typename\n    }\n    paginatorInfo {\n      count\n      '
             'currentPage\n      hasMorePages\n      lastPage\n      perPage\n      total\n      '
             '__typename\n    }\n    __typename\n  }\n}',
}