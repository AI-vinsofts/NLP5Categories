#!/usr/bin/env python
# -*- coding: utf-8 -*-

import en_core_web_sm
nlp = en_core_web_sm.load()

doc = nlp("I had a dream. We were sipping whiskey neat. Highest floor, The Bowery. Nowhere's high enough")

for token in doc:
     print(token.text, token.tag_)