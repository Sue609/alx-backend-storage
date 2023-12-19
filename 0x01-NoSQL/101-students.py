#!/usr/bin/env python3
"""
top students
"""


def top_students(mongo_collection):
    """
    function that returns all students sorted by average score.
    """
    pipeline = [
        {
            '$addFields': {
                'averageScore': {
                    '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]
    top_students = list(mongo_collection.aggregate(pipeline))
    return top_students

