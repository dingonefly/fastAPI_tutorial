#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2024/1/22
from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}