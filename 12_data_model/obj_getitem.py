# -*- coding: utf-8 -*-


class Events:
    def __init__(self, events):
        self.events = events

    def is_empty(self):
        return not bool(self.events)

    def list_events_by_range(self, start, end):
        return self.events[start:end]

    def __len__(self):
        """自定义长度，将会被用来做布尔判断"""
        return len(self.events)

    def __getitem__(self, index):
        """自定义切片方法"""
        # 直接将 slice 切片对象透传给 events 处理
        return self.events[index]


events = Events(
    [
        'computer started',
        'os launched',
        'docker started',
        'os stopped',
    ]
)

if not events.is_empty():
    print(events.list_events_by_range(1, 3))


if events:
    print(events[1:3])
