#!/bin/python3

import datetime
curr_date = datetime.datetime.now().isoformat().split("T")[0]
print(curr_date)
template = """
---
title: "<TITLE>"
date: <DATE>
tags: svenska
layout: default
---

![](/assets/images/xxx.jpeg)
"""
title = input("Filename: ").split()[0]

with open("_posts/" + curr_date + "-" + title + ".md", "w") as f:
    f.write(template.replace(
    "<DATE>", curr_date).replace(
        "<TITLE>", title))



