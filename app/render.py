# Copyright 2017 Google Inc.
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

class Frame:
  def __init__(self):
    self.cursor = None
    self.drawList = []

  def addStr(self, row, col, text, style):
    self.drawList.append((row, col, text, style))

  def setCursor(self, cursor):
    self.cursor = cursor

  def grabFrame(self):
    r = self.drawList, self.cursor
    self.drawList = []
    self.cursor = None
    return r

frame = Frame()
