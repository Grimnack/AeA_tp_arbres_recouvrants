import GraphValue.py

graph1 = GraphValue(
    [
        [False, True , True , False, False, False, False, False],
        [True , False, True , False, True , False, False, True ],
        [True , True , False, True , False, True , False, False],
        [False, False, True , False, False, False, False, False],
        [False, True , False, False, False, False, False, True ],
        [False, False, True , False, False, False, True , True ],
        [False, False, False, False, False, True , False, False],
        [False, True , False, False, True , True , False, False]
    ],
    [
        [-1, 6, 12, -1, -1, -1, -1, -1],
        [6, -1, 5, -1, 14, -1, -1, 8],
        [12, 5, -1, 9, -1, 7, -1, -1],
        [-1, -1, 9, -1, -1, -1, -1, -1],
        [-1, 14, -1, -1, -1, -1, -1, 3],
        [-1, -1, 7, -1, -1, -1, 15, 10],
        [-1, -1, -1, -1, -1, 15, -1, -1],
        [-1, 8, -1, -1, 3, 10, -1, -1]
    ]
)
