# -*- coding: utf-8 -*-
# @Author   : liyi
# @Time     : 2023/1/21 23:05
# @File     : edit_active_excel.py
# @Project  : ai_quant_trade
# Copyright (c) Personal 2022 liyi
# Function Description: 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# 导入库
import os
import pandas as pd
import xlwings as xw
import time

file_path = os.path.join(os.getcwd(), '看盘表.xlsx')

wb = xw.Book(file_path)
sht1 = wb.sheets['Sheet1']
for i in range(100):
    i += 1
    print(i)
    sht1.range('B2').value = i
    time.sleep(1)


