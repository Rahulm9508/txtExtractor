#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7358697038:AAE3i7YyOhHu6RcFfGXL4zGxrWmGjAJ0lkw")
    API_ID = int(os.environ.get("API_ID", "20346550"))
    API_HASH = os.environ.get("API_HASH", "bc79c3bea7a626887bdc0871eecf0327")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7081036509")
