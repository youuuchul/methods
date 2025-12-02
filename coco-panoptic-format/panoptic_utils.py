"""
Panoptic ID Encoding Utilities.

This module provides helper functions for converting between:
- RGB values used in COCO-style panoptic segmentation masks
- A single integer `panoptic_id` representing (class_id, instance_id)

Functions:
    rgb_to_id(r, g, b): Convert RGB triplet into an integer panoptic_id.
    id_to_rgb(id_):     Convert integer panoptic_id back into (R, G, B).

This is commonly used when encoding/decoding panoptic segmentation PNG masks.
"""

def rgb_to_id(r: int, g: int, b: int) -> int:
    """
    (R, G, B) 값을 하나의 panoptic_id 정수로 인코딩한다.
    각 채널은 0~255 범위여야 한다.
    id 범위: [0, 256^3 - 1]
    """
    return r + g * 256 + b * 256 * 256


def id_to_rgb(id_: int) -> tuple[int, int, int]:
    """
    panoptic_id 정수를 (R, G, B) 튜플로 디코딩한다.
    """
    r = id_ % 256
    g = (id_ // 256) % 256
    b = (id_ // (256 * 256)) % 256
    return r, g, b