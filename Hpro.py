import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("eJztXOtvG9l1v0PqRVKULVmyLHu9HnvXsry2RIl6ejder59rZ/3KWFnvynGUIWcojkTO0DNDy9zKQdsUzQMFgqIBWgQbpP3QLwUK5FPRogWKFkVaoEhQoEVRoA+0my9FGyBB/4C255x778yQHJGSd5MGaFbr4Z3XvXd+99zfPa+ZIhP/9cK/t+CfV0sy1vgOMxgzFFZhbI3JssLWFFlOsLWELCfZWlKWe9hajyz3srVeWe5ja32y3M/W+mV5gK0NyHKKraVkOc3W0rKcYWsZWR5ka4NUTrBKllWH2NoQUx7a51iPeYBtpZn7z0xRFJOxzYPMSLIvKUzu9NCOrbD3xIHe4Oww2xxhRh/ue1l5fT+/nrHwigG6IievSMkrsD9pVjnEqqNsbTRoMdPSwCDd/mfydDbau6HozoHozsHoDu+zMczevimOjPDTCbY5xoxDvEdl1tKoezbRtdG4dkbDdsZi2gFsetnmYWbA/+PsSyAT4/LIEWZM0JEjzBpg5gQzx/Ee4yhbwp0jtHMsuvMSWzKOM+Nl+DnBDBV+TjLjFPy8woxX4ec0MybZ0tpRZh5jpsJ7o7DNl5hxhnd2iq3B/WfZ2svMeI2tQSXn2K+A/KrMOE8FqG+aCqeYMUMFqDpHhVeZMUsFaGWOCpPMyFPhDDPmqTDFjAUqnGXGIhVeY8YSFc4xY5kK55mxQoVpZlygwgwzXqdCjpmzzHiDbSWYW0maJ9mXGBcehT2Y+hTMPOt/4L+7UwoU/TRsVsuuqRv3HafijcFuzarlVcv2fL1SUV3zSd30fM87iGcaftmx8+oVU/f8GdjDuVysmLrrTUEpZ+i+zjdFpzrjm261/ixXsiqml6t7bq5g2TnbMUzvFbhYr/lqvQYXm+rkpIp7skm8ZNNTpxt7rtStFxreWVFp0HM4CJVg7RtmNThccSpF3ecPfwA2Vx3bNou+5djXXddxvQE4tmH5aq1eqXhvd+lA2amauXLNdXIz+B893XrVMep4stDwYWvZhvlsZtPzDkFdpbpnuur0lro4Ozub84s1ddLHnrzijSOShkrVYJftWtBl71jrOWhFlfWqk94SnD/2aO6N+bnqfRgMz1QfmBV4JvVq2YUOqldcZxvbXXVUeFrfsuvmsUezb8znq94K3PrM2Jh2aqatln2/5r2ey21vb8+U9KJZcJytGXjmnGM3TMPa0otla8bZclxnZn55adZC2aEaROMPrA0bxlT1y6Z607HNhrqhW7bqOypIiK1W8dBHv/gnP/rDr8vmX4tr3p0p45V47wzAe0W7fPfatfnLKysbuHz8zYh3mQorH+7wAvvK374lCj94y5vAKqdLheliMLDTBd02ti3DL3uD8qxnVafLthUesE0fD/gpOHD9vavXb9++fneVhqW1tid1vWL5De8kDotZqcxcXdV0w3IuF4um562axbLtVJyNxs0H1+5f9kZjavAbNdODFY/dcT6wKhU9tzgzq069Nzf3hnobRueZ+mxlaX1p4ax6uVarmA/NwjuWn1ucX56ZX1Kn3rm5euf2ebVibZnq22ZxyzmrvmNtW2Kwc0srM7Mz8wvz8KM+0Eu6a4k7PRwulL9pfcO0feq+DvVbMB2gU7ln0zDu0yXHrU7X3YppF0HKDMIHeu7DHdRtmvK3rQ3TJUagJ8OBmzbtDcs2PTxd90vTK15/KBiiPPvGheVqeDxfLUqdIIETEaVpGKclrAMKshWRLQPSwtN3PQVmCoDrqNOmeiqd1q6/e/325dVb9+6qtx6oq9pnr6sfffi1H3/763+aTk/v7790+tFH3/ydx+rlOvCbq76urt66c+d9dfX6tff5mRtiNqh4zqpWG+qqaTTEXQ/Luu/BSKl49lx+fmF5dn5hYXF5bm5ZXPG25d+sF8TNcOe+O3hK3ZHEhVj4uHE8vw8ha3i+WUWmZOHGS+Lgeo7fA78gi84yHsS7mNIO+sVW0KF+XDNA9Xn7Jug2sKFSD2565a6f5BfhAGFH7moKrwdqfBU2KcBDFQJwtQIzWr1jArwG/Nh1KQwoQ4/mHqtXpvWapU7dgHXlrJfFg/nH6m2nqFfK8JxT+BgaNqKh9GjI0f4IbKpU43oValz3iPN2AyLTfPUFPDdCeGSVfqU38kf4KFF8NP5cHJznjO2QVojL6ykG9E3L63k6mqSjK0wAaB9mEdB64kCjZQHmruMAbfMOqm+++aZKy8IcbfMacpJ3pgVTwfFPgYwM1anhHFYFrxJexGSuvr1u2bW6T7JSoGenYoWKGnICXwvxFr30gd6OHV10NQRsEP7S+C8RAaxJoG51EShAYRzgGIdGx6VwEUR9gXD1hjj1B8LFgeiVQJCg3LgCcgLUQ2LlHRDytOpswYpSwRPEKShOt67l7uuex48S+q0ihW0UaXIV8/4gnzqW3UWyeuV1d1tlarhZprCdvkCmlN1k6rAC/dhMSKNCSkyLHDFhRjxXcOjAhkCbIcGeJ9gOaM69bIcDjzt9VEGjwvx+tjmA1gScHMd7kygkm2m2k2SbZEM872E7PWhiTDyHKkDBHhTGBWj3E8/7hDRn2U4fDOAQDp6fZZtD0pAAhQqbevjkrtLjH2T+MCslyFYaAVNJPMLB6CMM89tG6Da46z17hZAYISTOK/4hPo9OiZYPMX8UWoZ//hiJDlV0OJSVMZpTRyJzioYmnFmqhuMakaaTLdMK5IkLD0mVVFRoloL0+KDN4Mmy6ZpA5ySBM6XCOh2d8Z/5JEPb3jnYSn1mw9Vr5WaFqmpe0klb4DdepNln69BLvF21SMCOY89ErwJ53jANUP1U3cPW5bIKPbRQHL1TTQ+TF7fZjqAJuhaW48P0NC60r8K6DpohqGia6bsNVcs2zzB87iai4UBOoV6kDcVMIXwQ1OZoWmy7lm8KIwHGwscrpEHhY4c3TJ/u2PQcW0wk3fDokG8+46TleqCj8Mt8q8qr8yqmWdOQ06nOd8wGKe8+9uPWPSprY/Isn8SlgoZzU8Mn0lApI17RSOHAKmkgqAIqrXs0FC5tn2j4vEQMdjWGILG69/DAWwFBhqvKoHIA9tJKUjmkjMDvITiWhb8MlfAvrQwJOh2WXIH97pFcsa3saX0GRLnvgdPJZg9a13AGaUHBOY9H+uQRThScOvgR4mXuegAekDQM9IGMgYydZuPADuPACD76LBQgE6AJQSFkyCNFDCI7bPUx97gCqy6QBVr/UH0/2+lHQtmhayaIneBAlh4FGyIaEWfHBZ2E/gJyRTQdAXohcngX+QLvO8QmsN33uDuBP0DTDUnpXRCMYx9Dj0IEvqazRCjjLYvPK+10gevK5QcPmgkDFyI8c0e3Krm79SpMV+2IXGOmaHvWGxKs4m07rkHqo/eyIA7gjYpUf14na1EH5fSSZVz0cFJM1uCuiySuZbDdQRun+QS3tFOShtOdTNmOjJQruZZpG96lOjQyBy0uzM7Pzq8sLK7k5yeb2MrC3pO9HUXidkBOXp2uLoEF3ZB4oKLXalfSvDPJ6l5pIa7Por1arQPfPjVdq9RQoQNO3fbVggkWimB1SWdHY+gMyUwn89ObCXg0X4URgcEomG4ugL2qN6BWddt17A1R49ShdmYjtiPAXbNWgafQXsKjSNJEU3wYNBUP4iBqJ3CD1qiG/dOOSXaswYhqSNQayhKRmDaJQjEgOQYs1ST9zInfPP3WxfHatkEVoUtCe03yV1mvxipvWPUHITdFeWmE/gah/CpwFPLUMHDRGFzTS4x1kK7DElf10pybsLVAj/n9XbipMUFswtUYIho4qveyh/bLrAcAAySFbnAH/ahA1DQhFfZe47agFCAzeLJxTmhAJcgdjAhDEYQG/DYhiGxI6ENAZxPAZMBXwGEP7W+1NPYjbAw4DuZ8Cv0/RGqgqqAuMcCVEnyUjCSYwLEZ9PAdqBG6d4htjlKNF1C1kYQ8wNUjWVnT/WPSDSr0FXzWWFanSg7w3h3klNveQ6458WtHuGoEG+K9MdwQrY0HPRkPGe1IwGgxVIGTer/KCy2ORG6kt7Qq6bjC3rqmlkFlKZbN4lbNsWyf3CJuVZ12S2pTDzi35FroYLXu2qqDLqSCVTFVlHz1nqZuWyVLlSxwPIYFuFIjr0jyWol2BVvdslWkGu8yi/gW9mucS9uc9E60Pq66enFLLblOVa3VCxWrCCsBP5lvOllyKhVnG5qnLj2af6y+a5nbXMUkJe3RwmP1hmUbKvlJnZJasFy/zE8tPsbHQ2CEcosGHTl5Hi2h7bzh1H0a7FYim5BMhF5fDc1KDe117TRuUGsKmS3CZERsqCxH1KiAxciNbD4rmmSGelpCEqaG66CPclZostJRPEjYiMA0lDjiNrta4s6NrRgqw7o+xAOreDiBVJZUJkCNykSUK65gDQslC/ck4eFeRhDgGO33tvwRvQ0KeiOF+ls9zWbaBkPqge1X+TZquH1nd8NNnBDBjmYDLsG63dYf3tawcOjAvoNpDbQ3Diw2DgQnrTky8NCaSwktbh89AiZE2y8DytfbNx/ay8BzaaRdwZwzoQk3GDXheJwHrOWA05r6N9Spf73sWTUBmiOw3cS1x1dQfUQ97iBQeD+VoDPP4YYBZH1OeUB2E8/JggXKB/0ReG98J0UNKE82lIf2SwkckVEaES3Z7fnHmkfk8AuMiBM/IkC+aA4ryguNy5E9j8t3E8G4TOxjXI6KXh7r3FMYob9mn+AIpZIP7Q9ozrxEI1ROwtJGPTTo6HE6+sWk1O3v0tGX6eg3klJt506CE3T095KtTgKVOwlOxjoJTjFYC/0jwj8C/6MPY4JtHmXGKxzzVwNXJwUCR8Xelxn7soKgG2fYrwILwBiA9TBFKGXYTgYDhDtpqjchrJXmCoyzuHlNtP8VJts3zkFH+bFIn2J6gKN6PjqqtJxPM+lFTAuPxz3uC3wzxtnxWnSZowX2vlyfVPTRWvaGGvqaSWmHK3w0ZChy9Tqsnrm2Oq7CMoaRDbj5lo0BBAooRCs61lmjoOWvWangBtSq7m6YviraJkXDm8VHjSoHamh5tOkZtPTPV2nxTbcoBxuOWsClmJbTwPppVm3QT6wtNOk3ZLvtcEdJO5435JIeh+eBdjw1tE7IlupST6Sa/SMgjKScVy94RdcC+6flQT00QyYrVtXyL6K1SQ85T9sF2i7Sdqm7a4iUSnXV8fUKaj3wiDw2x/71kneaTpVNteY62Lhqeapbtwkm6DuOxoYLZp5h5STQ00XcInCosWCb3uf7adUVPg25OH+OfBpAYY3FfrgT1uQJoNdx5FowD8g1QsTXK5wYSH79SN3oyOglR0Yf2+yPODIGiOBS3KnwXfSKUgUZXgHMxwHU7ZFoA+9GCi+RV+DaJ70caZqwMOk3M3gJJTV8tY/7O7D6swpwarR6IBDRxIhsgtNsfBMDQRNKtInJPqByJGAg5HYYUvuH4XvoWwn6meoKQ6o7DL/cG8Iwm4jCkNoTDKnuMJzo3SHnzjiydhsM6f3D8HcJUBWCfqa7wpDuDsMv9IQwLCdhTY5WvwcY0t1hONKDMBwBGDIxMGT2D8M/JqPSkOkKQ6Y7DH4yhOHNnqg0ZPYEQ6Y7DMNJ0JSeD8ZAMLh/CP6lB1SpoI+DXSEY7A7Bk0QIweXeKASDe4JgsDsEQwlQ/J5nYyDI7h+Cf+uNSkG2KwTZ7hDYSgjBtT7QFaPV7wGCbHcIMopcJZAeh2KgGNo/FD/si0Ix1BWKoe5QFFkIxb3+qDQM7QmKoe5QMPbQ7kfHGJoJpFQeJx/RW9KyL1mu569TfAqt4rn8vPfrEY2ugMH7Vh8R6gLks54hX22zupGfX15evHBh9sLihbmlxcXT+cX84vLV2dLcwqyuF0yjVFha1Iv5ZX15/oJpzOn5/NJ8YW6S65YXMVo06Rlb609BjwFN82J+0qzqVuUipetMkt/cvPjUWn9qk58c3bwXvZt4Du66aDne5IZpm67um+sedAqqWC9Czy3Tuzg36VkbF+cWjdJiab64UpxfNmf1pfysuVLS50rGnGEszy4WudYW69NGPZt82utVb4P0TlTSLsxVH63euvP+9L13HkuljfwaoNWRQ79YC6KHuofbNAWgo6hRalOkMl6b1AGpFizP8iJ0Byvs4eO1EHPz1fvBzeRBxssWW3vMr5NtkKd91y7wxubyeXKILywsLi4txbcrIaAL8/n5+YWFWKhkzVOIBY/8UTAQASpE3FT5wEO1q+sdW9JrNdDxpw5IbxNYF9Rn1MU1TJHhcT5sB+VmjnvXsTGDZwXUtEvRC/JBaT4oLQSlxaC0FJSWef5OkirjMRtny2vP2QFxtiehYe+f8JTSp4wpSWVImVIOKAeVYdhOoH8+MQjHZTn9Ezvb9zHOdurzaCKpWDhgMiDNjQKyX5xqrWL6piHsQDInrtZy97bAoKARyVGuaqvDlww6oq+46HREYs40CwvJTugFxUa5s1OT4kVE+NQyt/lkpIQi85nv6kV/3XAKPBhNmTXkeY14SS/KEfd8l0fpTDsSAGLydFWvcTmntC6yrMj0FEEgP/SXEgAf0NYiueWhaZ38qNoX5BU17kMlZ+zncbMeETPq1l/hge+TiA2CkOGfDF1nKUQUlpPKMWUksj8cCV9n6BwGj9Df+lKHOk52qON0Sx3p6D8RHO8X4aleJaX0Jke+OEhBqhQdOStK6ZiMpHts7ylu4jrhGpWh4T5+W8/ueUnNoeF8NQwx8DQMmfOW4hKNh17n4REw6pujILEhTeQEcvKr3H0eE58kwd0lUUkrwO93kFNGacCjeW/ZXWD7TBfYYhK5gOoEdOJGAVzfXhK6cBLxyAVP58JpqV5z1IZTV11Tr1Qa6rZuYxKOyqeZekndNZTEEzxaUAqnJeGV6YAX9JX9sSLW+WhOVxrKAVZBJPSbsMGoJzkkeErFJiUH6glG740AWICTcNveoKgnT68QXuD+0FVLGpx4kcTnKptMkPMzpJKO+2Rr8KMinkm+YthkZKqYnw1BR2a5u0vEj4JusQOC0nmds5x67d4V9V4pCGXNPVbfdvWCiGSR96xieT7pYBjnipwMwlyIPoa56Jxn2RsVU7UMyrnHUNcVYO8pGhdavN9gkqhDZg55c6zT6BJbAy13zt3TcBT/AodYJbHn0aRsECUKE/iaokMID/H5F5O7RYeicaF395fQl2CNazKk0M+1/QHhrE+JxBt01HMlP0kaPU/YaY4TLILAZUjUvs8ikRshNi1RgmxrlKC/KXrTqeFe9uwvlb1FCIbaIwQH2iIEWeWh/VQJYzhfS+yO3tgniN7hJvTOBOj9N8W9xkUjRzrjNSGaOtoVs9/YY1RlT5hdTjy0r5DEHSPMfjshoyrnI7GWP0jIqIpMSz4e4CeI4mVMq/YPNUVHjBM8qCJjEvSyVCQqUlIwdCJCIqP4ClUYEhmLhkTa7zZO42ZSNBqGRGKbQvjPRBMoiNamiNZwCUir3eMf51qWaOIh5LUbyFM3AhKTS3XosDekw/4FYhncWuR+cR7QuGUE4QxkK5FBdeuaetfx1RvoASfttjVi8SLhCrLiebRikgVvXqgtTy4ZuunBm6Mv3gnWnPAV7a68r2OcZX8hCA1zMrQrsuNdUt9lB9qiDzwZGIMOUfvC83UXrQtSMOApMJl3tWxRRKLkQLdNj+JZjl1pUDBCuw4bikXI1EyKRaDu3CkW8bsy0pvgBAH6ktCZQp9Sj/Qp9Qhy2OnlmU19SGp0G6z3lIEJVLbDqUy4fdKUqxT1LFEK57gkPrp6MN7D5PPEpFbfT5ZJ38+Lijpl3VKmiqE3aHEPXB6k+9LebMQBEn09aIAv3B4pJ/giAfeGULe0+6zdiOtu+5MRR1aVTbl/lGmnPcANZpKElj9PRnmXCfupIVJSCvwNCb7TbKyTsTUB+jIJtzTUMZ0urRyH7Un4Hd6LmTsUyi3OSgy0HiZSizVwd0u/jsUmzsolDdhmUSuXng8tWTJ+TdyUmLBPNYzhkbZEeqRWDngGOSaSyLOJm60AVHzHLTRKtSqTWhhRshcFEjvz96iK/RYBOdhkjPJ8RW4+DpO1khJG48lYw7P9erg2EWtgipdY+iklSBiWiQMHo4blWLNhiZM/0Pr/SPm/0vphzRbJ2ozteqs4wV8gb2q4cZn5Q6hMoN7IuEvZTxBboPIA1DRML5eMYK4j1wd4qiXojJhh+dDWWx7ufYUncu7LdBmK2CryLZLRFzaEDtKjQGGYMtbl4RFUl0ZlQ2Oh9oB6w/6NIpx4lJUXWkSBomCFigJOtKagPt6Diwre9vGyI4hmNQe7RcSBNeJbHiVSHbrkQ9Mdl0U+NSzi4kUSwTvhajd1OKDSj2GJcZrq7KrFaUVuz6Jjl/jLfiGvbMqTuCrE2HD4xuFiQrymF2/DhT6orGDnIbomauOlm+5I0YRPxb4OiJturwMej30dsJ9F3//rIeE7yUIXh/RtlFC4+GhNNXL2WVV7wsSaZHN4CFRfYsfdPrRIUfJkJQamOvx+AWEaFPwq+e/nOd0/vZxuIKhR6a8Z5n0dacvwbrkuLrG7Nac7fEvlZzene4Y1K/EdcrqlLrj7e2ohS3XK6t49H9syOudjU4b1/O4Z1gtdM6xjOfPFsqs1/GhHXE51pVtOtfYmbi6xWOcXujXLiU8knToV0ZI6pVM/+Xk69U82nfryJ51O/WNlP+nULSMy9gmmUx/+OOnU4y+STn0kOi4Te0+n7tBTGKFvf9Lp1Hdj06lXYtOpZYo0+fnGjRPQ60OhP5jr3Zg/PcZgQWtKkR5nm0eYcZLjeCpwBtInk9pTpE9Lf+AEJjCH/sCjbf7ApgqMM7iZEu2H6dDGWcrlxmNtPsKmCnCkXmtLkT7H/n+nSM91TRDu6rp7YZ9jjAeVu0P3mTrd6ZEsY5dH2t2D8uK+yJ9iAnToc2zKfy53yX++1L9DWvp4lBiJpXpE1nAv2SFg4vdQRhu5BcKMtj6Zbvbn0RAK3cj9jv1tfkdiweCqiL8xFaSbUfY0nqaUs9/s41+RgAVtQuQ/H2hqijdzUDbDOTG+mYGgGdbazCzlPw/z/Oc2KFJ7h+J7Cr5jLvuX2hMUqc5QCA63f623GYqFBFB8tKkuUKQ6QyGbOU050KM8B7oNivTeofiHRFQq0nuCIt0ZirTo4y/1NENxKRmVinRXKNKdoZDNHO2R6eCZGCgye4fiB8koFJk9QZHpDEVG9PFpshmKT/dEpSLTFYrMblBkmpo5kAR1BXOh22AY3DsM/9EThWFwTzAMdoZBnLKdRDMMn+mVmfEDQbp1JxgGO0uEbGYgAdoe5kO3wZClK7oA8J+9UQCyewIg2xmArOiZrTQDoPVFAch2BSDbGQDZTL+COfFDMQAM7V0O/qsvCsPQnmAY6gyDyFy2N1gzDO/3R6fDUFcYhjrDIJtpz4Q+ymQ0TMMvaOzv+xzcTYtLeZAGOx+buxsXCAuTeCNhsNicY2022kJsom0kx1h7p6k/+bb+zFY7JgFrt5mIplHC8JJ2d9fW5fNplH6HmtOnTa/u8RhSSyxvr2E8hEivhYm8sXG8z+LmQuAKQQeI9hA3+JUe7X3crOHmEW4+h5vHrC1Tsj3Q98NES0ZuWnw5I8xoDTNdRxM/ubN9Xc6+/IL3HglClUdbNdVdw5X3tnJXa+rrmo637Z6TSyP4cXJyUfJbcnL5x1MwTy/iNmvgJgxfNifaUiDzE4ph7pJXi+1/AwXluyQoP6N5tXH5tMpu+bQU0F9fxwTU9fWpOTmIPKm54RHGdA1+poI+0oXYuCb/fpduG06Vf6pI98oVq0DvSPj00WEwfGjE6TTYsUibdFfdrcgr+asZsEei4qOXuVqv+JaQTKhipuY4FZ5IjRJxq1pzXJ9/BYw+6EWf3dH9MtVsefjtXv8QC79FNtP66YpXZJew82BQ0vMU+Od3PKsqvp5Rc3lmOD2liZ8uo49SeqZvmCUdukgfUcVHDPMS6TWCeS75JL3oTuZ+YXww+lwPj8Bjfjbl7HIBpzgPRewp7FMPpkRDgr9Ob+jAADEW+6FCvOZT/OPEb1KKOdaWVD5URsm3O6xkMyMw/PjvIOyP0FH+h2J1MHJE7o8o9ykblkQ8kUqk0qkM/DsFf+dT/w7lVGoktZ46lxqA/Y8Glf8FK3Iegg=="))))